def listSum(self, nums):
    return sum(nums)

def listProd(self, nums):
    result = 1
    for i in nums:
        result = result * i
    return result

def main():
    lSize = int (input ("Enter size of list: "))
    list = []
    for i in range (lSize):
        element = int(input())
        list.append(element)
   
    print("sum of list: " + listSum)
    print("product of list: " + listProd)