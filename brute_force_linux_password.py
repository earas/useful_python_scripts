from multiprocessing import Pool
import itertools
import crypt
import time

def hash_and_compare(word):
    password_candidate = ''.join(word)
    password_hash = crypt.crypt(password_candidate, salt)
    if password_hash == target_hash:
        return password_candidate
    return None

def brute_force(target_hash, characters, length, num_processes):
    # Calculate total combinations
    total_combinations = len(characters) ** length
    print(f"Number of characters in set: {len(characters)}")
    print(f"Password length: {length}")
    print(f"Possible candidates: {total_combinations}")

    # Time estimation for a single hash
    sample_size = min(1000, total_combinations)
    for _ in itertools.islice(itertools.product(characters, repeat=length), sample_size):
        _ = crypt.crypt(''.join(_), salt)
    sample_end_time = time.time()
    time_per_hash = (sample_end_time - start_time) / sample_size
    estimated_total_time = time_per_hash * total_combinations
    print(f"Estimated maximum time (in seconds): {estimated_total_time:.2f}")

    # Start brute-force process
    pool = Pool(processes=num_processes)
    try:
        for result in pool.imap_unordered(hash_and_compare, itertools.product(characters, repeat=length)):
            if result is not None:
                pool.terminate()
                return result
    finally:
        pool.close()
        pool.join()

    return None

# Example usage
characters = ['a', 'b', 'c', '1']
#characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
#              'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];

password_length = 4
num_processes = 4  # Adjust based on your CPU
target_hash = "$6$I2kBTChku9dL40Yg$N5XibbECwrHl5DyA232qiybPZ94gFNgdh4mw8FHhSpVGgbKTEdn10yA.u3gFTeCo2p868lb8FnNWMzqH5AAc81"
salt = "$6$I2kBTChku9dL40Yg"

start_time = time.time()
found_password = brute_force(target_hash, characters, password_length, num_processes)
finish_time = time.time()
execution_time = finish_time - start_time

print(f"Execution Time: {execution_time:.2f} seconds")
print("Password found:" if found_password else "Password not found.", found_password or "")
