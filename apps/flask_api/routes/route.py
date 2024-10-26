from flask_restx import Resource, fields
from flask import request, jsonify
from libs.shared.data_transfer import UserCreateDTO, ApiKeyCreateDTO
from libs.server.services import UserService, ApiKeyService
from apps.flask_api.middleware import generate_jwt, require_admin
from libs.server.data_access.model import ApiKey
from libs.server.data_access.database import db
from libs.shared.utils.json import JSON
from . import api

# Define API models // TODO: Consolidate with DTOs
user_model = api.model(
    "User",
    {"name": fields.String(required=True), "email": fields.String(required=True)},
)

api_key_model = api.model(
    "ApiKey",
    {
        "is_admin": fields.Boolean(required=False, default=False),
        "user_id": fields.String(required=True),
    },
)


# Define routes
@api.route("/users")
class UserResource(Resource):
    @api.expect(user_model)
    def post(self):
        data: UserCreateDTO = JSON.parse(api.payload)
        # user_dto = UserCreateDTO(**data)
        # TypeError: libs.shared.data_transfer.dto.UserCreateDTO() argument after ** must be a mapping, not Response
        user_dto = UserCreateDTO(email=data["email"], name=data["name"])
        user = UserService.create_user(user_dto, "mock_user_id")
        return {"id": user.id, "name": user.name, "email": user.email}, 201


@api.route("/generate_key", methods=["POST"])
class GenerateKeyResource(Resource):
    # @require_admin
    @api.expect(api_key_model)
    def post(self):

        data: ApiKeyCreateDTO = JSON.parse(api.payload)
        print(data)
        api_key = ApiKeyService.create_api_key(
            data=data,
            requester_user_id="mock_user_id",
        )

        return {"api_key": str(api_key.key)}, 201


@api.route("/health", methods=["GET"])
class HealthCheck(Resource):
    def get(self):
        return {"status": "healthy"}, 200
