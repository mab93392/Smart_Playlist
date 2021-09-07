import requests # allows communication w/API
import base64 # allows for conversion to base 64
# calls the client Ids
# this allows for usable to code to be public w/o giving Ids out
from client_id import client_id 
from client_secret_id import client_secret_id

def spot_auth():
    c = client_id()
    sc_id = client_secret_id()

    url = 'https://accounts.spotify.com/api/token' 
    header = {}
    data = {}

    
    # encodes to base64
    stmt = f'{c}:{sc_id}' 
    stmt_bytes = stmt.encode('ascii') 
    base64_bytes = base64.b64encode(stmt_bytes)
    base64_stmt = base64_bytes.decode('ascii')

    header['Authorization'] = "Basic " + base64_stmt
    data['grant_type'] = "client_credentials"

    req = requests.post(url, headers=header, data=data)

    # converts to json and retrieves the token
    resp = req.json()
    token = resp['access_token']

    return token

