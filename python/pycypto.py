from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto import Random
from Crypto.Cipher import AES

with open('/Users/wuhanchu/Dropbox/iwillgoo/appsvr_client20171206Q0001352_pub.pem', 'r') as f:
    pub = f.read()

with open('/Users/wuhanchu/Dropbox/iwillgoo/appsvr_client20171206Q0001352_pri.pem', 'r') as f:
    pri = f.read()

def encrypt(pub, message):
    # RSA/ECB/PKCS1Padding
    # 128字节搞一次
    ret = []
    input_text = message[:128]
    while input_text:
        # h = SHA.new(input_text)
        key = RSA.importKey(pri)
        cipher = PKCS1_v1_5.new(key)
        # ret += cipher.encrypt(input_text + h.digest())
        byte_list = input_text.encode("utf8")
        ret.append(byte_list)
        message = message[128:]
        input_text = message[:128]
    return ret

def decrypt(pri, ciphertext):
    key = RSA.importKey(pri)
    dsize = SHA.digest_size
    input_text = ciphertext[:256]
    ret = ''
    while input_text:
        sentinel = Random.new().read(15 + dsize)
        cipher = PKCS1_v1_5.new(key)
        _message = cipher.decrypt(input_text, sentinel)
        # ret += _message[:-dsize]
        ret += _message
        ciphertext = ciphertext[256:]
        input_text = ciphertext[:256]
    return ret

msg = encrypt(pub, 'ab12121cd' )
msg = decrypt(pri, msg)
print(msg)