from ..setup import conn

def get_long_url_by_hash(short_hash: str):
    cur = conn.cursor()
    cur.execute("SELECT long_url FROM shortUrls WHERE short_hash = %s", (short_hash,))
    long_url = cur.fetchone()
    cur.close()
    return long_url[0] if long_url else None

def get_short_url_by_url(long_url: str):
    cur = conn.cursor()
    cur.execute("SELECT short_hash FROM shortUrls WHERE long_url = %s", (long_url,))
    short_hash = cur.fetchone()
    cur.close()
    return short_hash[0] if short_hash else None

def create_short_hash(short_hash: str, long_url: str):
    cur = conn.cursor()
    cur.execute("INSERT INTO shortUrls (short_hash, long_url) VALUES (%s, %s) RETURNING short_hash", (short_hash, long_url,))
    short_hash = cur.fetchone()[0]
    conn.commit()
    cur.close()
    return short_hash

def increment_click_count(short_hash: str):
    cur = conn.cursor()
    cur.execute("UPDATE shortUrls SET clickCount = clickCount + 1 WHERE short_hash = %s", (short_hash,))
    conn.commit()
    cur.close()