"""
Author: Matthew O'Malley-Nichols
Description: Single file hashing and saving hash to file
"""
from hashlib import blake2b

def hash_file_from_absolute_path(filepath):
    blake_hash = blake2b()
    with open(filepath,'rb') as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            blake_hash.update(data)
    return blake_hash

def save_hash_to_absolute_path(blake_hash, filepath):
    print(f"Printing blake2 hash to {filepath}")
    with open(filepath,"w") as f:
        f.write(blake_hash.hexdigest())
