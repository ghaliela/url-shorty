## INTRO
This is a url shortnener
We could use this to create a short url from long one

## SETUP
Run:
```bash
cp .env.example .env
```

## Test
The api is started on port 8000
if we call the endpoint:
POST /
with the body:
```json
{
  "longUrl": "https://example.com"
}
```

We get 6+ characters string.

If we call the url:
GET /{code}
We get a 302 response redirecting towards the long url.

## Example:
POST /
{
  longUrl: "https://example.com"
}

__Response__ => 201 "hdf2jE"

Then if we call

GET /hdf2jE

__Response__ => 302 https://example.com
