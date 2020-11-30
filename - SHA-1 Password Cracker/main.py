import hashlib


def crack_sha1_hash(hash,salt=False):
    file1 = open("top-10000-passwords.txt", "r")

    with open('known-salts.txt', 'r') as file:
        data = file.read().replace('\n', '')
    saltsUsed = str(data)
    


    def encodetoSha1(temp):
        # encode the string
        encoded_str = temp.encode()
        
        # create a sha1 hash object initialized with the encoded string
        hash_obj = hashlib.sha1(encoded_str)
        
        # convert the hash object to a hexadecimal value
        hexa_value = hash_obj.hexdigest()
        
        # print
        return (hexa_value)

    encoded_passwords = {}

    while(True):
        #read next line
        line = file1.readline()
        #check if line is not null
        if not line:
            break

        if(salt):
            saltedLine = saltsUsed + line.strip() +saltsUsed
            #you can access the line
            encoded_passwords.update({encodetoSha1(saltedLine):line.strip()})
        
        else:
            #Add to the dicionary
            encoded_passwords.update({encodetoSha1(line.strip()):line.strip()})

    #close file
    file1.close



    


    if encoded_passwords.get(hash) is not None:
        print(encoded_passwords[hash])
    else:
        print("PASSWORD NOT IN DATABASE")
    if salt :
        print("no")
    
    
    


crack_sha1_hash("53d8b3dc9d39f0184144674e310185e41a87ffd5",True)
