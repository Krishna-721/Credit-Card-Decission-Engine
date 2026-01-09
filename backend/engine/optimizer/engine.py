from engine.optimizer.scorer import score_rule

def optimize(spend_map, cards, reward_rules):

    recommendations = {}

    for category_id, spend in spend_map.items():
        best = None

        for card in cards:
            card_id = card["id"]

            rule = reward_rules.get(card_id, {}).get(category_id)
            if not rule:
                continue

            score = score_rule(spend, rule)

            if not best or score["reward_value"] > best["reward_value"]:
                best = {
                    "card_id": card_id,
                    "card_name": card["card_name"],
                    "reward_value": score["reward_value"],
                    "reward_type": score["reward_type"],
                    "rate": score["rate"],
                }

        if best:
            recommendations[category_id] = best

    return recommendations
