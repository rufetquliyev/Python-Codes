# Thermometer adlı bir class hazırlayın. Həmin classdan object yaratmaq üçün argumentə selsi 
# şəklində bir data (Misal: t1 = Thermometer(50) girilir)
#a. Yaranmış objectlər hər üç vahiddə dəyər verə bilməli, hər üç vahiddən istifadə edilərək artırılıb, 
# azaldıla bilməlidir. show_temp dedikdə hər üç vahiddə temperaturu göstərərək print etməlidir
class Thermometer:
    def __init__(self, celsius):
        self.__celsius = celsius
    
    def celsius(self):
        return self.__celsius
    
    def fahrenheit(self):
        return self.__celsius * 9/5 + 32
 
    def kelvin(self):
        return self.__celsius + 273
    
    def show_temp(self):
        print(f"{self.__celsius}°C {self.fahrenheit}°F  {self.kelvin}K")

T1 = Thermometer(50)
T1.show_temp()

