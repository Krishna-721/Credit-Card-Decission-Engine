from engine.db.connection import get_conn

def fetch_active_reward_rules(card_ids):
    sql = """ 
    select distinct on (card_id, category_id)
        card_id,
        category_id,
        reward_rate,
        reward_type,
        cap_amount,
        cap_period
    from card_reward_rules 
    where active=true and card_id = ANY(%s::uuid[]) 
    order by card_id, category_id, priority desc;
    """
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute(sql,(card_ids,))
            rows=cur.fetchall()

    rules = {}
    for row in rows:
        rules.setdefault(row["card_id"], {})[row["category_id"]] = {
            "rate": row["reward_rate"],
            "type": row["reward_type"],
            "cap_amount": row["cap_amount"],
            "cap_period": row["cap_period"],
        }
    return rules