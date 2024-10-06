from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from backend.endpoints import text_reputation
from backend.endpoints import identity_reputation
from backend.endpoints import compute_user_reputation
from backend.endpoints import compute_weighted_user_reputation


origins = [
    "http://localhost",
    "http://localhost:3000",
]


def create_app(debug=False, **kwargs):
    app = FastAPI(debug=debug, **kwargs)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get(path="/")
    def main_page():
        return "Trusteon API Endpoints"

    app.include_router(text_reputation.router)
    app.include_router(identity_reputation.router)
    app.include_router(compute_user_reputation.router)
    app.include_router(compute_weighted_user_reputation.router)
    return app


app = create_app()

