from flask_restx import Api, Resource, fields
from flask import Blueprint, request, jsonify
from libs.shared.data_transfer import UserCreateDTO
from libs.server.services import UserService
from apps.flask_api.middleware import generate_jwt, require_admin

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

user_model = api.model('User', {
    'name': fields.String(required=True),
    'email': fields.String(required=True)
})

@api.route('/users')
class UserResource(Resource):
    @api.expect(user_model)
    def post(self):
        data = api.payload
        user_dto = UserCreateDTO(**data)
        user = UserService.create_user(user_dto)
        return {"id": user.id, "name": user.name, "email": user.email}, 201

@api.route('/generate_key', methods=['POST'])
@require_admin
def generate_key():
    data = request.json
    is_admin = data.get("is_admin", False)
    duration = None if is_admin else 30  # Admin keys never expire; User keys expire in 30 days
    
    api_key = ApiKey.generate_key(is_admin=is_admin, duration=duration)
    db.session.add(api_key)
    db.session.commit()
    
    token = generate_jwt(api_key.key, is_admin)
    return jsonify({"api_key": api_key.key, "jwt": token})