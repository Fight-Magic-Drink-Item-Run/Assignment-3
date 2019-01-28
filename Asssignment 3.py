#Assignment 3


def find_factoral(x):
  pile = x.make_a_pile_to_look_through()
  while pile is not empty:
    box = pile.grab_a_box()
    for item in box:
      if item.is_a_box():
        pile.append(item)
      elif item.is_a_key():
        print "found the key!"

#recursion

def look_for_key(box);:
    for item in box:
        if item.is_a_box():
            look_for_key(item)
        elif item.is_a_key():
            print "found the key"

#Recursion is when a function calls itself.
#Every recursive function has two cases: the base case and the recursive case.
#A stack has two operations: push and pop.
#All function calls go onto the call stack.
#The call stack can get very large, which takes up a lot of memory.

import numpy as np
import pandas as pd
import time
import timeit

from random import seed
from random import random
import string

def fact(x):
  if x == 1:
    return 1
  else:
    return x * fact(x-1)

print(fact(5))

def factorial(x):
    base = 1
    for i in range(x,0,-1):
        base = base * i


print(factorial(5))


#test to make sure values are the same for both methods
#recursive_fact1 = fact(random_list_int[0])
#recursive_fact1 = factorial(random_list_int[0])


random_list_int = list(np.random.randint(100, 500, 10))

print(random_list_int)

#My result [274, 494, 469, 138, 155, 457, 272, 114, 134, 283]

#updating array to add some larger numbers by adding a 0
random_list_int = list([274, 494, 469, 138, 155, 457, 272, 114, 1340, 2830])


#sort array for easier comparison later
def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
      smallest = findSmallest(arr)
      newArr.append(arr.pop(smallest))
  return newArr

random_list_int = selectionSort(random_list_int)

#test to make sure values are the same for both methods
#recursive_fact1 = fact(random_list_int[0])
#recursive_fact1 = factorial(random_list_int[0])

#Recursion

start_time = time.time()
fact(random_list_int[0])
end_time = time.time()
recursive_factorialt1 = (end_time - start_time)

start_time = time.time()
fact(random_list_int[1])
end_time = time.time()
recursive_factorialt2 = (end_time - start_time)

start_time = time.time()
fact(random_list_int[2])
end_time = time.time()
recursive_factorialt3 = (end_time - start_time)

start_time = time.time()
fact(random_list_int[3])
end_time = time.time()
recursive_factorialt4 = (end_time - start_time)

start_time = time.time()
fact(random_list_int[4])
end_time = time.time()
recursive_factorialt5 = (end_time - start_time)

start_time = time.time()
fact(random_list_int[5])
end_time = time.time()
recursive_factorialt6 = (end_time - start_time)

start_time = time.time()
fact(random_list_int[6])
end_time = time.time()
recursive_factorialt7 = (end_time - start_time)

start_time = time.time()
fact(random_list_int[7])
end_time = time.time()
recursive_factorialt8 = (end_time - start_time)

start_time = time.time()
fact(random_list_int[8])
end_time = time.time()
recursive_factorialt9 = (end_time - start_time)

start_time = time.time()
fact(random_list_int[9])
end_time = time.time()
recursive_factorialt10 = (end_time - start_time)



recursive_fact = np.array([recursive_factorialt1, recursive_factorialt2, recursive_factorialt3, recursive_factorialt4, recursive_factorialt5, recursive_factorialt6, recursive_factorialt7, recursive_factorialt8, recursive_factorialt9 ,recursive_factorialt10])

#for loop

start_time = time.time()
factorial(random_list_int[0])
end_time = time.time()
forloop_factorialt1 = (end_time - start_time)

start_time = time.time()
factorial(random_list_int[1])
end_time = time.time()
forloop_factorialt2 = (end_time - start_time)

start_time = time.time()
factorial(random_list_int[2])
end_time = time.time()
forloop_factorialt3 = (end_time - start_time)

start_time = time.time()
factorial(random_list_int[3])
end_time = time.time()
forloop_factorialt4 = (end_time - start_time)

start_time = time.time()
factorial(random_list_int[4])
end_time = time.time()
forloop_factorialt5 = (end_time - start_time)

start_time = time.time()
factorial(random_list_int[5])
end_time = time.time()
forloop_factorialt6 = (end_time - start_time)

start_time = time.time()
factorial(random_list_int[6])
end_time = time.time()
forloop_factorialt7 = (end_time - start_time)

start_time = time.time()
factorial(random_list_int[7])
end_time = time.time()
forloop_factorialt8 = (end_time - start_time)

start_time = time.time()
factorial(random_list_int[8])
end_time = time.time()
forloop_factorialt9 = (end_time - start_time)

start_time = time.time()
factorial(random_list_int[9])
end_time = time.time()
forloop_factorialt10 = (end_time - start_time)

forloop_fact = np.array([forloop_factorialt1, forloop_factorialt2, forloop_factorialt3, forloop_factorialt4, forloop_factorialt5, forloop_factorialt6, forloop_factorialt7, forloop_factorialt8, forloop_factorialt9, forloop_factorialt10])

import prettytable
from prettytable import PrettyTable

t = PrettyTable(['recursive_fact', 'forloop_fact'])
t.add_row([recursive_factorialt1, forloop_factorialt1])
t.add_row([recursive_factorialt2, forloop_factorialt2])
t.add_row([recursive_factorialt3, forloop_factorialt3])
t.add_row([recursive_factorialt4, forloop_factorialt4])
t.add_row([recursive_factorialt5, forloop_factorialt5])
t.add_row([recursive_factorialt6, forloop_factorialt6])
t.add_row([recursive_factorialt7, forloop_factorialt7])
t.add_row([recursive_factorialt8, forloop_factorialt8])
t.add_row([recursive_factorialt9, forloop_factorialt9])
t.add_row([recursive_factorialt10, forloop_factorialt10])
print(t)

plt.plot(recursive_fact)
plt.plot(forloop_fact)
plt.legend(['recursive_fact', 'forloop_fact'], loc='upper left')

#add x and y axis description

#Extra credit 1 - update through github

#extra credit 2  please modify the recursive factorial function to allow numbers greater than this limit set by python without modifying the system recursion limit in python



