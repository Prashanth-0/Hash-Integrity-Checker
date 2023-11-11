import hashlib

import os

def calculate_file_hash(file_path):

    try:

         hasher = hashlib.sha256()

         with open(file_path, 'rb') as f:

             while True:

                  chunk = f.read(8192)

                  if not chunk:

                      break

                  hasher.update(chunk)

         return hasher.hexdigest()

    except Exception as e:

        print(f"Error calculating hash for file {file_path}: {e}")

        return None


file_path = input("Enter the path to the file: ")

expected_hash = input("Enter the expected hash: ")

computed_hash = calculate_file_hash(file_path)

if computed_hash is not None:

    print(f"Computed hash: {computed_hash}")

    if computed_hash == expected_hash:

        print("File integrity is intact.")

    else:

        print("Warning: File integrity check failed. Possible compromise")

else:

    print("Error computing hash. check the provided file path.")



