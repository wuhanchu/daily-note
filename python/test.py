import M2Crypto as m2c  
  
key = m2c.RSA.load_key('/Users/wuhanchu/Dropbox/iwillgoo/appsvr_client20171206Q0001352_pub.pem')  
  
# encrypt something:  
data = 'Mochi 麻球'.encode('UTF-8')  
#encrypted = key.public_encrypt(data, m2c.RSA.pkcs1_padding)  
  
# and now decrypt it:  
#decrypted = key.private_decrypt(encrypted, m2c.RSA.pkcs1_padding)  
print(data) 