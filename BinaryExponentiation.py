# AUTHOR: Jackelyn Yii
# NUID: 59601326
# DATE: 7/21/21 (SUMMER 2021)
# ASSIGNMENT 2
import sys

a = int(sys.argv[1])
m = int(sys.argv[2])
n = int(sys.argv[3])
binary_n = (format(n, 'b'))


def binary_exponentiation(a, m, binary_n):
    term = a
    if binary_n[-1] == '1':
        product = a
    else:
        product = 1
    for i in range(len(binary_n)-2, -1, -1):
        term = term * term % m
        if binary_n[i] == '1':
            product = product * term % m
    return product


print(binary_exponentiation(a, m, binary_n))