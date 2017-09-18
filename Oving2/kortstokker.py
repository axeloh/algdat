#!/usr/bin/python3

from sys import stdin
from itertools import repeat

def merge(list):
    res = ""
    sorted_list = split(list)
    for i in range(len(sorted_list)):
        res += sorted_list[i][1]
    return res

def split(list):
    if len(list) < 2:
        return list[0]
    sorted_l = split(list[:len(list) // 2])
    sorted_r = split(list[len(list) // 2:])
    return merge2(sorted_l, sorted_r)

def merge2(l, r):
    res = []
    i, j = 0, 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1
    while i < len(l):
        res.append(l[i])
        i += 1
    while j < len(r):
        res.append(r[j])
        j += 1
    return res

def main():
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    print(merge(decks))

if __name__ == "__main__":
    main()

