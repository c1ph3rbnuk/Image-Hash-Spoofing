import hashlib
import random
import time
import argparse

def calculate_hash(file_path):
    """Calculating the SHA-1 hash of a given file."""
    with open(file_path, "rb") as f:
        file_data = f.read()
    return hashlib.sha1(file_data).hexdigest()

def random_byte_appending(target_prefix, input_file, output_file):
 
    #Appending random bytes to a file until the SHA-1 hash starts with the target prefix.
   
    with open(input_file, "rb") as f:
        original_data = f.read()

    modified_data = original_data
    attempts = 0
    start_time = time.time()

    while True:
        random_byte = random.randint(0, 255).to_bytes(1, 'big')
        modified_data += random_byte

        with open(output_file, "wb") as f:
            f.write(modified_data)

        file_hash = calculate_hash(output_file)
        attempts += 1

        if file_hash.startswith(target_prefix):
            elapsed_time = time.time() - start_time
            print(f"Success! Hash matched after {attempts} attempts.")
            print(f"Final hash: {file_hash}")
            print(f"Time taken: {elapsed_time:.5f} seconds")
            return

        if attempts % 1000 == 0:
            print(f"Attempt {attempts}: Current hash: {file_hash}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Append random bytes until SHA-1 hash matches prefix.")
    parser.add_argument("target_prefix", type=str, help="Desired prefix for the SHA-1 hash.")
    parser.add_argument("input_file", type=str, help="Path to the input file.")
    parser.add_argument("output_file", type=str, help="Path to the output file.")

    args = parser.parse_args()
    random_byte_appending(args.target_prefix, args.input_file, args.output_file)
