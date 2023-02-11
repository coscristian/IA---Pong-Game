from tkinter import Canvas

class Player(Canvas):
    def __init__(self, x1: float, y1: float, x2: float, y2: float, color: str, speed_x: float, speed_y: float):    
        self.__initial_x = x1
        self.__initial_y = y1
        self.__final_x = x2
        self.__final_y = y2   
        self.__speed_x = speed_x
        self.__speed_y = speed_y
        self.__color = color
    
    def get_initial_x(self):
        return self.__initial_x
    
    def get_initial_y(self):
        return self.__initial_y
    
    def get_final_x(self):
        return self.__final_x
    
    def get_final_y(self):
        return self.__final_y
    
    def get_speed_x(self):
        return self.__speed_x
    
    def get_speed_y(self):
        return self.__speed_y
    
    def get_color(self):
        return self.__color
    
    def set_initial_x(self, initial_x: float):
        self.__initial_x = initial_x
        
    def set_initial_y(self, initial_y: float):
        self.__initial_y = initial_y
        
    def set_final_x(self, final_x: float):
        self.__final_x = final_x

    def set_final_y(self, final_y: float):
        self.__final_y = final_y
    
    def set_speed_x(self, speed_x):
        self.__speed_x = speed_x

    def set_speed_y(self, speed_y):
        self.__speed_y = speed_y
        
class Ball(Player):
    def __init__(self, x1: float, y1: float, x2: float, y2: float, player_color: str, speed_x: float, speed_y: float):
        super().__init__(x1, y1, x2, y2, player_color, speed_x, speed_y)
        