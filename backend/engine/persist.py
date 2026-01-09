from engine.db.optimization_results import insert_optimization_result

def persist_recommendations(user_id, recommendations, valid_until=None):
    """
    recommendations:
      {
        category_id: {
            card_id,
            reward_value,
            ...
        }
      }
    """

    for category_id, rec in recommendations.items():
        insert_optimization_result(
            user_id=user_id,
            category_id=category_id,
            recommended_card_id=rec["card_id"],
            expected_reward=rec["reward_value"],
            valid_until=valid_until,
        )
