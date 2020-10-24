#Import random

#Create the function below:
def matrix_builder(integer):
    list1 = []
    for i in range(integer):
        list1.append([])
        for n in range(integer):
            list1[i].append(1)
    print(list1)
matrix_builder(5)

        
       
