# coding=utf-8
import M2Crypto as m2c  
  
m2c.Rand.rand_bytes(10)

key = m2c.RSA.load_key('/Users/wuhanchu/Dropbox/iwillgoo/appsvr_client20171206Q0001352_pri.pem')  
  
# encrypt something:  
data = 'Mochi 麻球'.encode('UTF-8')  
encrypted = key.public_encrypt(data, m2c.RSA.pkcs1_padding)  
  
# and now decrypt it:  
# decrypted = key.private_decrypt(encrypted, m2c.RSA.pkcs1_padding)  
print(data) 