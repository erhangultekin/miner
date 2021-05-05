import hashlib
import random
import string
import requests


def id_generator(size=6, chars=string.ascii_uppercase + string.digits+"*/-\}][{½$#£><é!'^^+%&/()=?_-:,."):
    return ''.join(random.choice(chars) for _ in range(size))

def hash():
    randomNumber=random.randint(1,20)
    s=id_generator(randomNumber)
    hs = hashlib.sha256(s.encode('utf-8')).hexdigest()
    myData={"id": str(s),"hash": str(hs)}
    r=requests.post("http://localhost:5000/hash", json=myData)


for x in range(10):
    hash()