# -*- coding: utf-8 -*-
"""Assignment 0: Deep dive with python coding

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12V2Nw2JuXUbZFjbkSTAKVnJTFqsDVr0x

# **Assignment 0: Deep dive with python coding**

1.Consider a sequence of n Bernoulli trials with success probabilty p per trial. A string of consecutive successes is known as a success run. Write a function that returns the counts for runs of length k for each k observed in a dictionary.

Expected Result:

count_runs([0, 1, 0, 1, 1, 0, 0, 0, 0, 1],)

Counter({1: 2, 2: 1})

or

count_runs(np.random.randint(0,2,1000000))

Counter({1: 124950,

2: 62561,

3: 31402,

4: 15482,

5: 7865,

6: 3856,

7: 1968,

8: 971,

9: 495,

10: 233,

11: 140,

12: 71,

13: 32,

14: 13,

15: 9,

16: 3})
"""

from collections import Counter

def count_runs(sequence):
    runs = []
    current_run = 0

    for value in sequence:
        if value == 1:
            current_run =  current_run+1
        elif current_run > 0:
            runs.append(current_run)
            current_run = 0

    # check ตัวสุดท้าย
    if current_run > 0:
        runs.append(current_run)

    return Counter(runs)


result = count_runs([0, 1, 0, 1, 1, 0, 0, 0, 0, 1])
print(result)

import numpy as np

result2 = count_runs(np.random.randint(0,2,1000000))
print(result2)

"""2.Continuing from Part 1, what is the probability of observing at least one run of length 5 or more when n=100 and p=0.5?. Estimate this from 100,000 simulated experiments. Is this more, less or equally likely than finding runs of length 7 or more when p=0.7 ?

Expected Result

run_prob(expts=100000, n=100, k=5, p=0.5)

0.80704

run_prob(expts=100000, n=100, k=7, p=0.7)

0.94881
"""

import numpy as np

def run_prob(expts, n, k, p):
    # สร้างลำดับตัวเลขแบบสุ่มจากการเลือก 0 หรือ 1 โดยให้น้ำหนักตามความน่าจะเป็นของ "1" และ "0" ที่กำหนดใน p
    xxs = np.random.choice([0, 1], size=(expts, n), p=[1-p, p])

    # นับจำนวนลำดับที่มี run ความยาว k หรือมากกว่า
    success_run_count = sum(max(count_runs(row).keys()) >= k for row in xxs)

    # คำนวณความน่าจะเป็นตามสูตร: (จำนวน success runs ที่พบ) / (จำนวนการทดลองทั้งหมด)
    probability = success_run_count / expts

    return probability

# ทดลองสำหรับ k=5, p=0.5
result  = run_prob(expts=100000, n=100, k=5, p=0.5)
print(result)


# ทดลองสำหรับ k=7, p=0.7
result2 = run_prob(expts=100000, n=100, k=7, p=0.7)
print(result2)