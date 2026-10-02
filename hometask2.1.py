#!/usr/bin/python3
import random

def rand_DNA_seq(length):
    nucleotides = ['A', 'T', 'G', 'C']
    seq = [random.choice(nucleotides) for _ in range(length)]
    return ''.join(seq)

l = 1000
print(rand_DNA_seq(l))

