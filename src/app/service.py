import hashlib

from fastapi import HTTPException

# default size
DEFAULT_HASH_SIZE=6

#DB List
DB=[("e149be", 'https://facebook.com'),("a24a5b", 'https://youtube.com'),("7ccc4c", 'https://google.com'),("3a2039", 'https://wikipedia.org')]

#replace with sql_request :
def sql_request(short_hash,DB):
    return next((pair for pair in DB if pair[0] == short_hash), None)

# replace with sql_request
def check_long_url_exists(long_url):
    return next((pair for pair in DB if pair[1] == long_url), None)

def generate_short_hash(url,n):
    md5_hash = hashlib.md5()
    md5_hash.update(str(url).encode('utf-8'))
    full_hash = md5_hash.hexdigest()

    # in case of collision
    while(sql_request(full_hash[:n],DB)):
        n+=1

    short_hash = full_hash[:n]
    return short_hash


def create_short_hash(url):
    if check_long_url_exists(url):
        return check_long_url_exists(url)[0]
    
    short_url = generate_short_hash(url, DEFAULT_HASH_SIZE)

    DB.append((short_url, url))
    print(DB)
    return short_url

def get_long_url(short_hash):
    long_url_tuple = next((url for url in DB if url[0] == short_hash), None)
    if not long_url_tuple:
        return HTTPException(status_code=404, detail="URL not found")
    return long_url_tuple[1]
