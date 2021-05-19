import os
import random

def clean_files():
    try:
        os.remove("Encrypt.txt")
        os.remove("Key.txt")
    except:
        pass

def crossover(crossover_points, block_one, block_two):
    # step 2
    for point in crossover_points:
        temp = block_one[point]
        block_one[point] = block_two[point] 
        block_two[point] = temp
    return block_one, block_two

def mutation(mutation_points, block_one, block_two):
    # step 3
    for point in mutation_points:
        block_one[point] = 128 - block_one[point]
        block_two[point] = 128 - block_two[point]
    return block_one, block_two

def write_encrypt_file(filename, block_one, block_two):
    text_one = ''.join([chr(byte_in) for byte_in in block_one])
    text_two = ''.join([chr(byte_in) for byte_in in block_two])
    open(filename, "a").write(f"{text_one}{text_two}")

def write_key_file(filename, key):
    key_text = ''.join([str(number_key) for number_key in key])
    open(filename, "a").write(f"{key_text}$")

def get_block_bytes(file_path):
    return open(file_path, "rb")

if __name__ == "__main__":
    clean_files()

    text_file = get_block_bytes("ga.txt")
    block_one = []
    block_two = []
    insert_one = True

    for i, byte_text in enumerate(text_file.read()):
        if len(block_one) == 8:
            block_two.append(byte_text)
        else:
            block_one.append(byte_text)

        if len(block_two) == 8:
            crossover_points = (random.randint(0, 7), random.randint(0, 7))
            mutation_points = (random.randint(0, 7), random.randint(0, 7))
            permutation_factor = random.randint(0, 3)

            key = [crossover_points[0], 
                   crossover_points[1],
                   mutation_points[0],
                   mutation_points[1],
                   permutation_factor]

            block_one, block_two = crossover(crossover_points, block_one, block_two)
            block_one, block_two = mutation(mutation_points, block_one, block_two)
            write_encrypt_file("Encrypt.txt", block_one, block_two)
            write_key_file("Key.txt", key)
            block_one, block_two = [], []
