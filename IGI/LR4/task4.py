import math
import matplotlib.pyplot as plt
import numpy as np
from abstractions import GeometricFigure
from misc import input_int, input_float


class FigureColor:
    COLORS = {
        "w": "white",
        "g": "green",
        "b": "blue",
        "y": "yellow"
        }
    def __init__(self, color: str=None):
        self.__color = color
    
    @property
    def color_ch(self):
        return self.__color
    
    @color_ch.setter
    def color_ch(self, color):
        self.__color = color

class Rhombus(GeometricFigure):
    N = 6
    FIGURE_NAME = "Rhombus"

    def __init__(self, a_length: int, b_lenth: int):
        self.__a_length = a_length
        self.__b_length = b_lenth
        self.obj_color = FigureColor()
    
    @classmethod
    def get_figure_name(cls):
        """Function to get figure name

        Returns:
            _type_: str
        """
        return f"Figure name: {cls.FIGURE_NAME}" 

    @property
    def get(self):
        return self.__a_length, self.__b_length
    
    @get.setter
    def get(self, lengths):
        self.__a_length, self.__b_length = lengths
    
    def area(self):
        """Function to calculate rhombus's area

        Returns:
            _type_: str
        """
        return f"Area: {self.__a_length * self.__b_length}"
        
    
    def __str__(self):
        return f"Figure name: {self.get_figure_name()}\nSide a: {self.__a_length}\nSide b: {self.__b_length}\nColor: {self.obj_color.color_ch}"
    
    def plot_rhombus(self):
        """Function to plot rhombus
        """

        x = [0,self.__a_length / 2, self.__a_length, self.__a_length / 2, 0] 
        y = [0, self.__b_length / 2, 0, -self.__b_length / 2, 0]

        plt.figure()
        plt.plot(x, y, linewidth=2)
        color = str(self.obj_color.color_ch)
        plt.fill(x, y, color)  
        plt.axis('equal')
        plt.title(self.FIGURE_NAME)

        plt.savefig("rhombus.jpg")
        plt.show()
        
def task_4(): 
    side_a = int(input_int("Enter side a: "))
    side_b = int(input_int("Enter side b: "))
    is_breaked = False
    obj = Rhombus(side_a, side_b)
    while True:
        step = int(input("Other steps:\n1. Calculate rhombus's area\n2. Plot rhombus\n3. Output class data\n4. Change side len\n5. Change figure color\n6. Exit\n"))
        match step:
            case 1:
                print(obj.area())
            case 2:
                obj.plot_rhombus()
            case 3:
                print(obj)
            case 4:
                new_side_a = int(input_int("Enter new side a: "))
                new_side_b = int(input_int("Enter new side b: "))
                obj.get = new_side_a, new_side_b
            case 5:
                color = input(f"Change color: {FigureColor.COLORS}: ")
                obj.obj_color.color_ch = color
            case 6:
                is_breaked = True
                break
            case _:
                print("Invalid choice. Please try again.")
        if is_breaked:
            break
        continue
