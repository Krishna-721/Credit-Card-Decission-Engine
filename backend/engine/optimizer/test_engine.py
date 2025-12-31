from uuid import UUID
from engine.optimizer.engine import optimize

cards=[
    {
        'id': '1',
        'card_name': 'HDFC Millennia '
    },
    {
        'id': '2',
        'card_name':'AXIS Burgundy'
    }
]

category='travel'

reward_rules = {
    cards[0]["id"]: {
        category: {
            "rate": "0.05",
            "type": "MILES",
            "cap_amount": None,
            "cap_period": None,
        }
    },
    cards[1]["id"]: {
        category: {
            "rate": "0.02",
            "type": "POINTS",
            "cap_amount": None,
            "cap_period": None,
        }
    },
}

spend_map={
    category: 10000
}

result=optimize(spend_map,cards,reward_rules)

print(result)