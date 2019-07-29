import base64

from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

with open('/Users/wuhanchu/Dropbox/iwillgoo/appsvr_client20171206Q0001352_pub_esa.pem', 'r') as f:
    pub = f.read()

with open('/Users/wuhanchu/Dropbox/iwillgoo/appsvr_client20171206Q0001352_pri.pem', 'r') as f:
    pri = f.read()


def sign(pri, message):
    key = RSA.importKey(pri)
    cipher = PKCS1_v1_5.new(key)
    byte_list = bytes(message, encoding="utf8")
    ret = cipher.sign(SHA.new(byte_list))

    return base64.encodebytes(ret).decode("utf8").replace("\n", "")


def validate_sign(pub, message, signature):
    # 开始计算签名
    key = RSA.importKey(pub)
    signer = PKCS1_v1_5.new(key)
    digest = SHA.new()
    digest.update(message.encode("utf8"))
    if signer.verify(digest, base64.decodestring(signature.encode("utf8"))):
        return True
    return False


signature = sign(pri, 'tsetet')
print("signature: ", signature)
result = validate_sign(pub, 'tsetet', signature)
print("result: ", result)
