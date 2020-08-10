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
randomIndication_generation_start = ""
randomIndication_generation_end = ""
aes_extended_encryption_start = ""
aes_extended_encryption_end = ""

start_time = time.time()
for i in range(250000):
    # data = list()
    # data.append(int(input("Enter first Integer : ")))
    # data.append(float(input("Enter first Float 1 : ")))
    # data.append(float(input("Enter first Float 2 : ")))
    # data.append(float(input("Enter first Float 3 : ")))
    # packed_data = pack('ifff',data[0],data[1],data[2],data[3])
    packed_data = pack('ifff',112,0.090909909012,9.2131231239312,6.981237129837)
    aes_key_generation_start = time.time()
    aes_encryption_start = time.time()
    data = packed_data
    key = get_random_bytes(16)
    aes_key_generation_end = time.time() - aes_key_generation_start
    cipher = AES.new(key,AES.MODE_EAX)
    ciphertext = cipher.encrypt(data)
    aes_encryption_end = time.time() - aes_encryption_start
    value = bin(int.from_bytes(ciphertext, byteorder=sys.byteorder))
    spos = value.find('b')
    value = value[spos+1:len(value)]
    while len(value) != 128 :
        key = get_random_bytes(16)
        cipher = AES.new(key,AES.MODE_EAX)
        ciphertext = cipher.encrypt(data)
        value = bin(int.from_bytes(ciphertext, byteorder=sys.byteorder))
        spos = value.find('b')
        value = value[spos+1:len(value)]
    print(len(value))
    count = 0
    binaryValue = list()
    for bits in value:
        binaryValue.append(bits)
        count = count+1
    rows = 16
    columns = 8
    bitArray = []
    for i in range(rows):
        bitArray.append([0]*columns)
    x = 0
    for i in range(rows):
        for j in range(columns):
            if x <= 127:
                bitArray[i][j] = binaryValue[x]
                if x<127:
                    x = x+1
                else:
                    break

    my_timer = 0

    def randomIndication():
        x = random.randint(0,99)
        a = x%14
        if a == 0 :
            x= 14
        else:
            x = 16-a
            x = x-1
        return x
    def session():
        aes_extended_encryption_start = time.time()
        global binaryString
        binaryString = ""
        randomIndication_generation_start = time.time()
        x = randomIndication()
        y = random.randint(1,6)
        randomIndication_generation_end = time.time() - randomIndication_generation_start

        for i in range(y+1):
            if i == 0:
                continue
            elif i == 1:
                if bitArray[x][i] == '0':
                    bitArray[x][i] = '1'
                elif bitArray[x][i] == '1':
                    bitArray[x][i] = '0'
            elif i == 2:
                if bitArray[x][i] == '0':
                    bitArray[x][i] = '1'
                elif bitArray[x][i] == '1':
                    bitArray[x][i] = '0'
            elif i == 3:
                continue
            elif i == 4:
                if bitArray[x][i] == '0':
                    bitArray[x][i] = '1'
                elif bitArray[x][i] == '1':
                    bitArray[x][i] = '0'
            elif i == 5:
                if bitArray[x][i] == '0':
                    bitArray[x][i] = '1'
                elif bitArray[x][i] == '1':
                    bitArray[x][i] = '0'
            elif i == 6:
                continue
            elif i == 7:
                if bitArray[x][i] == '0':
                    bitArray[x][i] = '1'
                elif bitArray[x][i] == '1':
                    bitArray[x][i] = '0'
        aes_extended_encryption_end = time.time() - aes_extended_encryption_start

        for i in range(y+1):
            if i == 0:
                continue
            elif i == 1:
                if bitArray[x][i] == '0':
                    bitArray[x][i] = '1'
                elif bitArray[x][i] == '1':
                    bitArray[x][i] = '0'
            elif i == 2:
                if bitArray[x][i] == '0':
                    bitArray[x][i] = '1'
                elif bitArray[x][i] == '1':
                    bitArray[x][i] = '0'
            elif i == 3:
                continue
            elif i == 4:
                if bitArray[x][i] == '0':
                    bitArray[x][i] = '1'
                elif bitArray[x][i] == '1':
                    bitArray[x][i] = '0'
            elif i == 5:
                if bitArray[x][i] == '0':
                    bitArray[x][i] = '1'
                elif bitArray[x][i] == '1':
                    bitArray[x][i] = '0'
            elif i == 6:
                continue
            elif i == 7:
                if bitArray[x][i] == '0':
                    bitArray[x][i] = '1'
                elif bitArray[x][i] == '1':
                    bitArray[x][i] = '0'
        aes_decryption_start = time.time()
        dcypher = AES.new(key,AES.MODE_EAX,cipher.nonce)
        decryptedtext = dcypher.decrypt(ciphertext)

        # decryptedtext = cipher.decrypt(ciphertext)

        for i in range(rows):
            for j in range(columns):
                binaryString = binaryString+bitArray[i][j]
        abc = int(binaryString, 2).to_bytes(17, byteorder=sys.byteorder, signed=True)
        abc = abc[:16]
        dcypher = AES.new(key,AES.MODE_EAX,cipher.nonce)
        abc = dcypher.decrypt(abc)
        # abc = cipher.decrypt(abc)

        original_data = unpack('ifff',abc)

        print(original_data[0])
        print(original_data[1])
        print(original_data[2])
        print(original_data[3])
        print(original_data)

        print("AES Key generation Time  \t-" , aes_key_generation_end)
        print("AES Encryption Time  \t\t-" , aes_encryption_end)
        print("AES Extended Decryption Time  \t\t-" , aes_encryption_end)
        print("Random random Indication generation time  \t\t-" , aes_encryption_end)
        print("AES Extended Encryption time  \t\t-" , aes_extended_encryption_end )
    session()
    #end of loop
end_time = time.time() - start_time
print("Total execution time \t\t-" , end_time)
#-------------------------------
