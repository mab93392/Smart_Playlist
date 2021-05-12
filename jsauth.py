import sys
import json
from client_id import client_id
from client_secret_id import client_secret_id

dict = {
    'client': client_id(),
    'secret': client_secret_id()
}

print(json.dumps(dict,indent=1))