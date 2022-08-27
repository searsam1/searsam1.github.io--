
# import math
# print('The value of e is approximately %5.5f.' % math.e)
# # The value of e is approximately 2.71828.

# message = "hello world!"
# print('Message : %s' % message)
# # Message : hello world!

# first_name, last_name = "john", "sullivan"
# full_name = f"{first_name.title()} {last_name.title()}"
# print(full_name)
# # john sullivan

# # import string
# import numpy as np

# prntable = r"""0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0000"""

# arr = [] 
# for i in prntable:
#     arr.append([str(ord(i)).rjust(3,'0'), i])

# arr = np.array(arr)
# arr = arr.reshape((14,14))
# print(arr)


import string
r = string.printable

print("<table>")
print(f"<tr>")

for idx,i in enumerate(r):
    if (idx + 1) % 6 == 0:
        print(f"</tr>")
        print(f"<tr>")
        print(f"<td>{i}</td><td>{ord(i)}</td>")
    else:
        print(f"<td>{i}</td><td>{ord(i)}</td>")
print("</table>")