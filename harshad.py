import math
from random import random, randrange
from array import array

def erat_sieve(n):
    sieve_bound = n//2
    primes = bytearray(sieve_bound)
    max_check = int(math.ceil(math.sqrt(n)))//2
    for i in range(1,max_check):
        if not primes[i]:
            for j in range(2*i*(i+1), sieve_bound, 2*i+1):
                primes[j] = 1
    return primes

def primes_list(n):
    primes = array("L")
    for i,x in enumerate(erat_sieve(n)):
        if not x:
            primes.append(2*i+1)
    primes[0] = 2
    return primes

def is_prime(n,k = None):
    #miller-rabin test
    if n == 2 or n == 3:
        return True
    if n%2 == 0:
        return False
    if k == None:
        k = int(math.log(n,2)) + 1

    s = 0
    t = n-1
    while t%2 == 0:
        t >>= 1 # t//=2
        s+=1
    for i in range(k):
        a = randrange(2, n-1)#randrange excludes endpoint
        x = pow(a,t,n)
        if x == 1 or x == n-1:
            continue
        br = False
        for j in range(s-1):
            x = pow(x,2,n)
            if x == 1:
                return False
            if x == n-1:
                br = True
                break
        if br:
            continue
        return False
    return True

from collections import deque

def right_trunc_harshad(n):
    queue = deque()
    cur_num = (1,1)
    for x in range(2,10):
        queue.appendleft((x,x))
    while cur_num[0]*10 < n:
        for digit in range(10):
            new_num = cur_num[0]*10 + digit
            new_sum = cur_num[1] + digit
            if new_num >= n:
                break
            if new_num % new_sum == 0:
                queue.appendleft((new_num,new_sum))
                yield (new_num,new_sum)
        cur_num = queue.pop()

def digits_sum(n):
  res = 0
  if n < 10:
      res = n
  elif n >= QUANT_SIZE:
      res = digits_sum(n//QUANT_SIZE) + digits_sum(n%QUANT_SIZE)
  elif sums[n] == 0:
      res = digits_sum(n//10) + n%10
      sums[n] = res
  else:
      res = sums[n]       
  return res

# def is_prime(n):
#   res = True
#   if n == 1:
#       return False
#   if n == 2:
#       return True

#   if n < primes_bound:
#       if n%2 == 0:
#           res = False
#       else:
#           if primes_sieve[(n-1)//2]:
#               res = False
#   else:
#       bound = int(math.ceil(math.sqrt(n)))
#       for x in primes:
#           if n%x == 0:
#               res = False
#   return res

# harsad_bound = 10**14
# primes_bound = int(math.sqrt(harsad_bound)) + 1
# primes_sieve = erat_sieve(primes_bound)
# primes = [2*i+1 for i,x in enumerate(primes_sieve) if not x]
# primes[0] = 2 


# rth = list(right_trunc_harshad(harsad_bound))

# for prime in primes:
#   for num_idx,(num,dig_sum) in enumerate(rth):
#       num_to_check = num//dig_sum
#       if num_to_check > prime:
#           if num_to_check%prime == 0:
#               rth[num_idx] = (0,1)

# strong_rth = []

# for num, dig_sum in rth:
#   if num != 0:
#       for digit in range(1,10,2):
#           new_num = num*10 + digit
#           if new_num < harsad_bound:
#               strong_rth.append(new_num)

# for prime in primes:
#   for num_idx, num in enumerate(strong_rth):
#       if num > prime:
#           if num%prime == 0:
#               strong_rth[num_idx] = 0

# print(sum(strong_rth))

#BFS + Miller-rabin
if __name__=="__main__": 
    s = 0
    harsad_bound = 10**14
    for num,dig_sum in right_trunc_harshad(harsad_bound):
      if is_prime(num//dig_sum):
          for digit in range(1,10,2):
              new_num = num*10 + digit
              if new_num < harsad_bound:
                  if is_prime(new_num):
                      s+=new_num
    
    print(s)
