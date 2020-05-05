import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    nomes = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        emailISP = emailID.split("@")
        
        match = re.search('^gmail.com$', emailISP[1])

        if match:
            nomes.append(firstName)
    nomes.sort()
    for i in nomes:
        print(i)