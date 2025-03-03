from tokenize import String


def addTwoNumbers(num1, num2):
  return num1 + num2

def addAllNumbers(myList):
  sum = 0
  for item in myList:
    sum+=item
  print("Print before return")
  return sum


def printAllNumbers(*myList):
  for item in myList:
    print(item)




def checkifNumeric(*numList):
  """ This is checking whether all the params are integers of not. If any param is not integer, return False."""
  for item in numList:
    print(item)
    if not isinstance(item, (int, float)):
      return False
  return True



def findMinIndex(myList, i):
  minValue = myList[i]
  idxMin = i
  for x in range(i, len(myList)):
    if myList[x] < minValue:
      minValue = myList[x]
      idxMin = x
  return idxMin


def swapValues(myList, i, j):
  tmp = myList[i]
  myList[i] = myList[j]
  myList[j] = tmp
  return myList


def sortList(myList):
  print("Print before sort", myList)
  for i in range(0, len(myList)):
    idxMin = findMinIndex(myList, i)
    swapValues(myList, i, idxMin)
  return myList

