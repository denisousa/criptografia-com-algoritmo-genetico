import os
import random
from project import app


def dismake_crossover(crossover_points, block_one, block_two):
    # step 2
    for point in crossover_points:
        temp = block_one[point]
        block_one[point] = block_two[point] 
        block_two[point] = temp
    return block_one, block_two

def dismake_mutation(mutation_points, block_one, block_two):
    # step 3
    for point in mutation_points:
        block_one[point] = 128 - block_one[point]
        block_two[point] = 128 - block_two[point]
    return block_one, block_two

def write_descrypt_file(filename, block_one, block_two):
    text_one = ''.join([chr(byte_in) for byte_in in block_one])
    text_two = ''.join([chr(byte_in) for byte_in in block_two])
    open(f"{app.config['UPLOAD_FOLDER']}\\{filename}", "a").write(f"{text_one}{text_two}")


def apply_descrypt(encrypt_file, keys_file):
    keys = keys_file.read().decode("utf-8").split('$')
    block_one = []
    block_two = []
    insert_one = True

    for i, byte_text in enumerate(encrypt_file.read()):
        if len(block_one) == 8:
            block_two.append(byte_text)
        else:
            block_one.append(byte_text)

        if len(block_two) == 8:
            first_key = keys.pop(0)
            crossover_points = (int(first_key[0]), int(first_key[1]))
            mutation_points = (int(first_key[2]), int(first_key[3]))
            permutation_factor = int(first_key[4])
            block_one, block_two = dismake_mutation(mutation_points, block_one, block_two)
            block_one, block_two = dismake_crossover(crossover_points, block_one, block_two)
            write_descrypt_file("Descrypt.txt", block_one, block_two)
            block_one, block_two = [], []
