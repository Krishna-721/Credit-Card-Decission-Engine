from decimal import Decimal, ROUND_HALF_UP

# Centralized normalization values
REWARD_MULTIPLIERS = {
    "CASHBACK": Decimal("1.0"),
    "POINTS": Decimal("0.25"),   # 1 point = ₹0.25 (assumption for now)
    "MILES": Decimal("0.15"),    # 1 mile = ₹0.15
}

def score_rule(spend, rule):

    spend = Decimal(spend)
    rate = Decimal(rule["rate"])
    reward_type = rule["type"]

    multiplier = REWARD_MULTIPLIERS[reward_type]

    effective_spend = spend
    cap_applied = False

    if rule["cap_amount"] is not None:
        cap = Decimal(rule["cap_amount"])
        if spend > cap:
            effective_spend = cap
            cap_applied = True

    reward_value = (effective_spend * rate * multiplier).quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )

    return {
        "reward_value": reward_value,
        "effective_spend": effective_spend,
        "reward_type": reward_type,
        "rate": rate,
        "cap_applied": cap_applied,
    }
