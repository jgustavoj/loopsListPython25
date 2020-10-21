list_of_numbers = [4,	80,	85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]


#Your code here:
def merge_two_list(the_list):
    even_array=[]
    odd_array=[]
    new_list=[]
    for x in the_list:
        if x % 2 == 0:
            even_array.append(x)
        else:
            odd_array.append(x) 
    new_list.append(odd_array)
    new_list.append(even_array)
    return new_list

    
print(merge_two_list(list_of_numbers))

