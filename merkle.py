#importing hashlib for SHA1 hashing
import hashlib
import os

def hash_em_up(filenames): #computes first level of hash on a set of files
    hashes = []
    for filename in filenames:
        hash_obj = hashlib.sha1() #specify SHA1 for hashing 
        with open('test/' + filename, 'rb') as file:
            while True:
                data = file.read(4096)
                if not data:
                    break
                hash_obj.update(data)
        hashes.append(hash_obj.hexdigest())
    return hashes

                                                  
filenames = os.listdir(path='test')

#compute the top hash using the hash values of each file in the test directory
top_hash = hash_em_up(filenames)
while len(top_hash) > 1:
    top_hash = [hashlib.sha1((top_hash[i] + top_hash[i+1]).encode('utf-8')).hexdigest() for i in range(0, len(top_hash), 2)]
print("Top Hash:", top_hash[0])

#testing that top hash will change when a file is modified
with open('test/a.txt', 'a') as mod:
    mod.write('Z')

top_hash = hash_em_up(filenames)
while len(top_hash) > 1:
    top_hash = [hashlib.sha1((top_hash[i] + top_hash[i+1]).encode('utf-8')).hexdigest() for i in range(0, len(top_hash), 2)]
print("Top Hash after file changed:", top_hash[0])