# Create a function that takes a users list and returns
# only the odd values of the given list into a new list. (1,2,3,4,5,6,7,8,9)

def get_odd(list):
    new_list = []

    for i in range(0, len(list)):
        if (i % 2 == 1):
            new_list.append(i)
    return new_list

print(get_odd((1,2,3,4,5,6,7,8,9)))