#!/usr/bin/python3

from sys import stdin

def radixSort(list):
    radix = 10
    maxLength = False
    tmp, placement = -1, 1
    while not maxLength:
        maxLength = True
        buckets = [[] for _ in range(radix)]
        for i in list:
            tmp = i//placement
            buckets[tmp % radix].append(i)
            if maxLength and tmp > 0:
                maxLength = False
        a = 0
        for b in range(radix):
            buck = buckets[b]
            for i in buck:
                list[a] = i
                a += 1
        placement *= radix
    return list

def find(list, lower, upper):
    lower = binarySearch(list, lower, True)
    upper = binarySearch(list, upper, False)
    return [lower, upper]

def binarySearch(list, item, goLower):
    first = 0
    last = len(list) - 1
    while first <= last:
        mid = (first + last) // 2
        if item < list[mid]:
            last = mid - 1
        elif item > list[mid]:
            first = mid + 1
        else:
            return item
    if item < list[0]:
        return list[0]
    if item > list[-1]:
        return list[-1]
    if goLower:
        return list[first-1]
    return list[first]

list = [1,3,7,8,10]
binarySearch(list,5,True)



def main():
    input_list = []
    for x in stdin.readline().split():
        input_list.append(int(x))
    sorted_list = radixSort(input_list)
    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        result = find(sorted_list, minimum, maximum)
        print(str(result[0]) + " " + str(result[1]))

if __name__ == "__main__":
    main()