
class Crayon:
    def __init__(self, color:str):
        self.color = color

    def print_color(self):
        print(self.color)
        
    def change_colors(crayon,color):
        crayon.color = color

green_crayon = Crayon("green")
green_crayon.print_color()
# Ouputs -> green
green_crayon.change_colors("yellowgreen")
green_crayon.print_color()
# "yellowgreen"


