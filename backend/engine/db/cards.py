from engine.db.connection import get_conn

def fetch_active_cards():
    sql = """
    SELECT
        id, 
        card_name,
        issuer,
        network,
        annual_fee
    FROM credit_cards
    WHERE active = true;
    """
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()
