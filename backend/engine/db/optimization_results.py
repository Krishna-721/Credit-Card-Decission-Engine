from engine.db.connection import get_conn

def insert_optimization_result(
    user_id,
    category_id,
    recommended_card_id,
    expected_reward,
    valid_until=None,
):
    sql = """
    INSERT INTO optimization_results (
        user_id,
        category_id,
        recommended_card_id,
        expected_reward,
        valid_until
    )
    VALUES (%s, %s, %s, %s, %s);
    """

    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                sql,
                (
                    user_id,
                    category_id,
                    recommended_card_id,
                    expected_reward,
                    valid_until,
                )
            )
        conn.commit()
