from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from time import *
from struct import *
import sys
import random
import threading
import time
start_time = ""
end_time = ""
aes_key_generation_start = ""
aes_key_generation_end = ""
aes_encryption_start = ""
aes_encryption_end = ""
aes_decryption_start = ""
aes_decryption_end = ""
aes_extended_encryption_start = ""
aes_extended_encryption_end = ""
aes_extended_decryption_start = ""
aes_extended_decryption_end = ""
start_time = time.time()
for i in range(1):
    # data = list()
    # data.append(int(input("Enter first Integer : ")))
    # data.append(float(input("Enter first Float 1 : ")))
    # data.append(float(input("Enter first Float 2 : ")))
    # data.append(float(input("Enter first Float 3 : ")))
    packed_data = pack('ifff',112,0.090909909012,9.2131231239312,6.981237129837)


    aes_key_generation_start = time.time()
    aes_encryption_start = time.time()
    data = packed_data
    key = get_random_bytes(16)
    aes_key_generation_end = time.time() - aes_key_generation_start
    cipher = AES.new(key,AES.MODE_EAX)
    ciphertext = cipher.encrypt(data)
    aes_encryption_end = time.time() - aes_encryption_start
    def session():
        aes_decryption_start = time.time()
        dcypher = AES.new(key,AES.MODE_EAX,cipher.nonce)
        decryptedtext = dcypher.decrypt(ciphertext)
        #decryptedtext = cipher.decrypt(ciphertext)

        original_data = unpack('ifff',decryptedtext)
        aes_decryption_end = time.time() - aes_decryption_start
        print(original_data[0])
        print(original_data[1])
        print(original_data[2])
        print(original_data[3])
        print(original_data)

        print("AES Key generation Time  \t-" , aes_key_generation_end)
        print("AES Encryption Time  \t\t-" , aes_encryption_end)
        print("AES Decryption Time  \t\t-" , aes_encryption_end)
    session()
end_time = time.time() - start_time
print("Total execution time \t\t-" , end_time)
#-------------------------------
