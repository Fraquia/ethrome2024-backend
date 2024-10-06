from backend.services.digital_reputation.mdb_spam_reputation import get_spam_score
from backend.services.digital_reputation.talent_protocol_passport import extract_talent_protocol_score


def compute_reputation_score(wallet: str, farcaster_id: str):
    spam_score = get_spam_score(farcaster_id)
    talent_score = extract_talent_protocol_score(wallet)

    talent_weight = 0.70
    spam_weight = 0.30

    _score = (talent_weight*talent_score) +(spam_weight*(1-spam_score))


    return _score


wallet = "0xf66c00759467c6524b0c86af132bb52786b37382" #biancotto
farcaster_id = "260770"
test = compute_reputation_score(wallet,farcaster_id)
print(test)

