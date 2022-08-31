
# names = ["Alec", "John", "James"]

# def names_start_j(names):
#     for name in names:
#         if name.startswith("J"): 
#             yield name

# names_j = names_start_j(names)
# for name in names_j:
#     print(name)    

# # Output 
# # John
# # James    
# print(list(names_j))    
# # []

def my_range(start,end):
    while start < end:
        yield start
        start += 1

# for i in my_range(10,20):
#     print(i, end=", ")
# 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,


def range2(start,end):
    
    if start < end:
        yield start 
        start += 1

x = range2(10,20)
print(list(x))