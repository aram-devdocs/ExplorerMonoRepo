# Flask Monorepo Project with OpenAPI, PostgreSQL/SQLite, and Notebook Integration

This project is a monorepo designed for scalable API and data exploration workflows, using shared libraries in `libs` for models, services, and utilities. It supports PostgreSQL/SQLite, OpenAPI documentation, and Jupyter notebooks.

## Project Structure

```
/explorer_mono_repo
├── apps/
│   └── flask-api/               # Flask API application
│       ├── init.py              # Initializes the Flask app
│       ├── app.py               # Main entry point for Flask API
│       ├── routes/              # API route handlers with OpenAPI support
│       ├── config.py            # API-specific configuration settings
│       └── middleware.py        # JWT and Auth middleware
├── libs/                        # Shared libraries for server and client
│   ├── shared/                  # Cross-cutting shared code (DTOs, utils)
│   │   ├── data_transfer/       # Data Transfer Objects (DTOs) using Pydantic
│   └── utils/                   # Shared utility functions
│   └── server/                  # Server-specific logic (models, services)
│       ├── data_access/         # Database models (SQLAlchemy)
│       └── services/            # Business logic layer
├── notebooks/                   # Jupyter notebooks for data exploration
├── tests/                       # Unit and end-to-end tests
├── migrations/                  # Database migrations
├── install.sh                   # Installs dependencies and initializes migrations
├── dev.sh                       # Runs the development server
├── migrate.sh                   # Handles database migrations
├── test.sh                      # Runs unit and end-to-end tests
├── pyproject.toml               # Poetry configuration
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

## Setup

### First-Time Setup

#### Step 1: Fork the Repository

```sh
git clone <your-repo-url>
cd explorer_mono_repo
```

#### Step 2: Set Up Virtual Environment with Poetry

```sh
poetry install
poetry shell
```

#### Step 3: Make Shell Scripts Executable

```sh
chmod +x *.sh
```

#### Step 4: Install Dependencies

```sh
./install.sh
```

### Recurring Setup

- **Start Development Server:** `./dev.sh`
- **Database Migrations:** `./migrate.sh {migrate –name “desc”|upgrade|downgrade}`
- **Run Tests:** `./test.sh`
- **Jupyter Notebook:** Run `jupyter notebook` in `notebooks/`.

### Reset Instructions

If you need to reset the database:

1. Stop the server.
2. Delete the SQLite database file.
3. Restart the server.

**Note:** This will delete all data.

## Jupyter Notebook Integration

The installation script sets up Jupyter and configures the Poetry environment as a kernel. To use the Poetry environment in Jupyter:

1. After running poetry shell, you will see `Spawning shell within {path}`.
2. In VS Code or Jupyter Notebook, select the Poetry environment as the kernel by find by path

## API Key Management

On initial startup, an admin-level API key with an infinite expiry date is generated and logged. Make sure to save this key securely. API keys are stored in the database and managed as follows:

- **Admin API Key:** Created on first server run; does not expire.
- **User API Key:** Generated on request and expires after 30 days.
- **Admin-Only Access:** Only admins can create new API keys.

If you lose your admin API key, you will need to reset the database to generate a new one. In local development we use SQLite so recovery is straightforward:

1. Stop the server.
2. Delete the SQLite database file.
3. Restart the server.
   **Note:** This will delete all data.

## Example API Usage

To generate a new user-level API key:

1. Use the `/generate_key` endpoint with `is_admin` set to `false` (admin API key required for authorization).
2. A JWT token and the API key are returned for use in authenticated requests.

**Example:**

```
POST /generate_key
Authorization: Bearer <admin_jwt_token>
{
    "is_admin": false
}
```

## Example Directory Structure

```
/explorer_mono_repo
├── apps/
│   └── flask-api/               # Flask API application
│       ├── __init__.py          # Initializes the Flask app
│       ├── app.py               # Main entry point for Flask API
│       ├── routes/              # API route handlers with OpenAPI support
│       ├── config.py            # API-specific configuration settings
│       └── middleware.py        # JWT and Auth middleware
├── libs/                        # Shared libraries for server and client
│   ├── shared/                  # Cross-cutting shared code (DTOs, utils)
│   │   ├── data_transfer/       # Data Transfer Objects (DTOs) using Pydantic
│   └── utils/                   # Shared utility functions
│   └── server/                  # Server-specific logic (models, services)
│       ├── data_access/         # Database models (SQLAlchemy)
│       └── services/            # Business logic layer
├── notebooks/                   # Jupyter notebooks for data exploration
├── tests/                       # Unit and end-to-end tests
├── migrations/                  # Database migrations
├── install.sh                   # Installs dependencies and initializes migrations
├── dev.sh                       # Runs the development server
├── migrate.sh                   # Handles database migrations
├── test.sh                      # Runs unit and end-to-end tests
├── pyproject.toml               # Poetry configuration
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

## Requirements

Dependencies are listed in `requirements.txt`. If you did not run `install.sh`, you can install them manually with:

```sh
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License. See `LICENSE` for more details.
