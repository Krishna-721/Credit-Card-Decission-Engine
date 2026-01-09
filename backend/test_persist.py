import os
import django
from uuid import UUID
from engine.optimizer.engine import optimize
from engine.persist import persist_recommendations

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()


# ⚠️ THESE MUST EXIST IN DB
USER_ID = UUID("c209c778-11a8-4761-9ae0-6149c86cd2e0")
CATEGORY_ID = UUID("54fe9afd-89d8-454b-b126-2f42633124f7")
CARD_ID = UUID("d7f1641b-28ef-4710-8e06-ae1648d144c2")

cards = [
    {"id": CARD_ID, "card_name": "Test Card"}
]

reward_rules = {
    CARD_ID: {
        CATEGORY_ID: {
            "rate": "0.25",
            "type": "POINTS",
            "cap_amount": None,
            "cap_period": None,
        }
    }
}

spend_map = {CATEGORY_ID: 10000}

recommendations = optimize(spend_map, cards, reward_rules)

persist_recommendations(
    user_id=USER_ID,
    recommendations=recommendations
)

print("Persisted:\n", recommendations)