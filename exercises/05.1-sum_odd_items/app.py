arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
def sumOdds():
    total = 0
    for num in arr: 
        if num % 2 != 0:
            total = total + num
    return total   
print(sumOdds())
