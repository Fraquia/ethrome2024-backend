import uvicorn

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from backend.endpoints import get_fraud_score


origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://brian-frontend.vercel.app",
    "https://brian-frontend-git-development-brian-knows.vercel.app",
    "https://brianknows.org",
    "https://www.brianknows.org",
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
        return "Backend Endpoints"

    app.include_router(get_fraud_score.router)
    return app


app = create_app()


# if __name__ == "__server__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)