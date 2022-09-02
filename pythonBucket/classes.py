
# class Crayon:
#     def __init__(self, color:str):
#         self.color = color

#     def print_color(self):
#         print(self.color)

#     def change_colors(crayon,color):
#         crayon.color = color

# green_crayon = Crayon("green")
# green_crayon.print_color()
# # Ouputs -> green
# green_crayon.change_colors("yellowgreen")
# green_crayon.print_color()
# # "yellowgreen"


class Testing:
    tests = 0

    @classmethod
    def is_equal(cls, a, b):
        try:
            assert a == b
            cls.tests += 1
            print("tests passed: " + str(cls.tests))
        except AssertionError:
            print(f"{a}\n  should = \n{b}")


t = Testing()
t.is_equal(3, 3)
t.is_equal(3, 44)
t.is_equal(2, 2)
t.is_equal(1, 1)

# tests passed: 1
# 3
#   should =
# 44
# tests passed: 2
# tests passed: 3
