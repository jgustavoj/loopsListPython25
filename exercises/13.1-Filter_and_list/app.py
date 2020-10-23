
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def my_funtion(names):
    return names.startswith("R")
resulting_names = list(filter(my_funtion, all_names))

print(resulting_names)




