from services.digital_reputation.compute_reputation import compute_reputation_score
from fastapi import APIRouter


router = APIRouter()


@router.post("/backend/reputation_score")
def identity_reputation(wallet: str, farcaster_id: str):
    try:
        score = compute_reputation_score(wallet,farcaster_id)
        response = {"prediction": float(score), "status_code": 200}

        return response

    except Exception as e:
        return {"error": str(e), "status_code":400}
