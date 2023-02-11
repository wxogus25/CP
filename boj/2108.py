import sys
import math
input = sys.stdin.readline

N = int(input())
numList = []
numDict = {}
for _ in range(N):
    x = int(input())
    numList.append(x)
    numDict[x] = numDict.get(x, 0) + 1

numList.sort()
listSum = sum(numList)
middleValue = numList[N//2]
listRange = max(numList) - min(numList)

sortedList = sorted(numDict.items(), key=lambda item: (-item[1], item[0]))

if len(sortedList) > 1 and sortedList[0][1] == sortedList[1][1]:
    listMode = sortedList[1][0]
else:
    listMode = sortedList[0][0]

print(int(listSum/N + math.copysign(0.5, listSum)))
print(middleValue)
print(listMode)
print(listRange)
