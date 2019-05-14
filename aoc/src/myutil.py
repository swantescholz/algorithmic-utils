from pprint import pprint

from bitarray import bitarray
from typing import List, Set, Tuple, TypeVar, Iterable

T = TypeVar('T')


def grayCodeBitFlips(numberOfBits: int) -> List[int]:
    """returns the indices (bits) needed to be flipped in each step"""
    if numberOfBits == 0:
        return []
    res = [0]
    for i in range(1, numberOfBits):
        res += [i] + list(reversed(res))
    return res


def exactSublistSum(numbers: List[int], desiredSum: int) -> List[List[int]]:
    """
    returns all multi-subsets that sum to the given desired sum
    positive! numbers list must be sorted in ascending order, duplicates are okay
    """
    numbers = sorted(numbers)
    if len(numbers) == 0:
        return []
    if numbers[0] < 0:
        raise RuntimeError("numbers must be non-negative")
    size = len(numbers)
    maxSum = sum(numbers)
    if maxSum < desiredSum:
        return []
    neccessaryTopNumbersCount = 0
    while maxSum - numbers[-1 - neccessaryTopNumbersCount] < desiredSum:
        neccessaryTopNumbersCount += 1
    reducedSize = size - neccessaryTopNumbersCount
    reducedSum = desiredSum - sum(numbers[size - neccessaryTopNumbersCount:])
    if reducedSize > 64:
        raise RuntimeError("too many numbers to handle the subset sum problem!")

    def createListOfAllSublistSums(elements: List[int]) -> List[Tuple[int, bitarray]]:
        if len(elements) > 25:
            raise RuntimeError("too many elements")
        bits = bitarray([False] * len(elements))
        currentSum = 0
        res = [(0, bitarray(bits))]
        for bitFlipIndex in grayCodeBitFlips(len(elements)):
            if bits[bitFlipIndex]:
                currentSum -= elements[bitFlipIndex]
            else:
                currentSum += elements[bitFlipIndex]
            bits[bitFlipIndex] = not bits[bitFlipIndex]
            res.append((currentSum, bitarray(bits)))
        res.sort()
        return res

    lefts = numbers[:reducedSize // 2]
    rights = numbers[reducedSize // 2:]
    leftSums = createListOfAllSublistSums(lefts)
    rightSums = createListOfAllSublistSums(rights)
    a = 0
    b = len(rightSums) - 1
    res = []
    while True:
        currentSum = leftSums[a][0] + rightSums[b][0]
        if currentSum > reducedSum:
            b -= 1
            if b < 0:
                break
        elif currentSum < reducedSum:
            a += 1
            if a >= len(leftSums):
                break
        else:
            aAtStartOfGoodRun = a
            while leftSums[a][0] + rightSums[b][0] == reducedSum:
                sublist = []
                sublist.extend(numbers[size - neccessaryTopNumbersCount:])
                for i in range(len(lefts)):
                    if leftSums[a][1][i]:
                        sublist.append(numbers[i])
                for i in range(len(rights)):
                    if rightSums[b][1][i]:
                        sublist.append(numbers[i + len(lefts)])
                res.append(sublist)
                a += 1
                if a >= len(leftSums):
                    break
            a = aAtStartOfGoodRun
            b -= 1
            if b < 0:
                break
    return res


def prod(iterable: Iterable[T]) -> int:
    res = 1
    for factor in iterable:
        res *= factor
    return res


if __name__ == '__main__':
    nn = [1, 2, 5, 2, 8, 11, 13, 17, 15]
    res = exactSublistSum(nn, 23)
    pprint(res)
