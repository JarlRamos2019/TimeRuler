#!usr/bin/env python
# ==============================================================================
# NAME: Jarl Ramos
# ASGT: TimeRuler
# ORGN: N/A
# FILE: timeruler_2.py
# DATE: 14 February 2023
# ==============================================================================
# Description:
# This program can be modified to take in any Python 3 code. It will then record
# the time the code takes to execute in seconds. The program will then use the
# elapsed time to calculate the code's TimeRuler score. A higher TimeRuler score
# generally means that the code is faster and can reach a maximum of around
# 225,000. It will repeat this step 100 times and find the average of all 100
# TimeRuler score values.

import time
# number of iterations the code will go through
m = 100

def mc91(n):
    if n > 100:
        return n - 10
    else:
        return mc91(mc91(n + 11))
# raw TimeRuler scores
scores = []
for i in range(m):
    # stopwatch zone that records time elapsed
    start = time.time()
    mc91(5)
    end = time.time()
    elapsed = end - start
    # calculation of the TimeRuler score
    try:
        time_ruler_score = 0.225 / elapsed
    except:
        time_ruler_score = 225000
    scores.append(time_ruler_score)
average = 0
# finds the average of 100 TimeRuler scores
for i in scores:
    average = average + i
average = average / m
avgr = round(average)
print(f"The aggregate TimeRuler score for the algorithm provided is {avgr}")
