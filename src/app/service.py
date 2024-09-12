import hashlib

from fastapi import HTTPException

from . import repository

# default size
DEFAULT_HASH_SIZE=6

def check_short_hash_collision(short_hash):
    return repository.get_long_url_by_hash(short_hash) is not None

def check_long_url_exists(long_url):
    return repository.get_long_url_by_url(long_url)

def generate_short_hash(url):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(str(url).encode('utf-8'))
    full_hash = sha256_hash.hexdigest()

    n = DEFAULT_HASH_SIZE
    # in case of collision
    while(check_short_hash_collision(full_hash[:n])):
        n+=1

    short_hash = full_hash[:n]
    return short_hash


def create_short_hash(url):
    if check_long_url_exists(url):
        return check_long_url_exists(url)
    
    short_url = generate_short_hash(url)

    repository.create_short_hash(short_url, url)
    return short_url

def get_long_url(short_hash):
    long_url_tuple = repository.get_long_url_by_hash(short_hash)
    if not long_url_tuple:
        raise HTTPException(status_code=404, detail="URL not found")
    repository.increment_click_count(short_hash)
    return long_url_tuple
