import hashlib

# default size
DEFAULT_HASH_SIZE=6

#DB List
DB=["e149be","a24a5b","7ccc4c","3a2039","677ae3","a24a5be"]

#replace with sql_request :
def sql_request(short_hash,DB):
    return short_hash in DB

def generate_short_hash(url,n):
    md5_hash = hashlib.md5()
    md5_hash.update(url.encode('utf-8'))
    full_hash = md5_hash.hexdigest()
    
    # in case of collision
    while(sql_request(full_hash[:n],DB)):
        n+=1

    short_hash = full_hash[:n]
    return short_hash


def create_short_hash(url):
    short_url = generate_short_hash(url, DEFAULT_HASH_SIZE)

    DB.append(short_url)
    return short_url

def get_long_url(short_hash):
    return next((url for url in DB if url == short_hash), None)
