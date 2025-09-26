import secrets
BASE62_CHARS="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE = len(BASE62_CHARS)
SALT_PRIME = 3571

def generate_salt():
    return secrets.randbelow(1_000_000)

def encode(num):
    if num==0:
        return BASE62_CHARS[0]
    arr=[]
    while num:
        num,rem=divmod(num,BASE)
        arr.append(BASE62_CHARS[rem])
    return "".join(reversed(arr))
    
def decode(s):
    num=0
    for char in s:
        num=num*BASE+BASE62_CHARS.index(char)
    return num
    
def create_unique_id_from_pk_and_salt(pk,salt):
    return(salt*SALT_PRIME)+pk