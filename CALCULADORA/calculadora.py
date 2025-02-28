#Definicion de clase calculadora que proporciona operaciones de matématicas básicas
class Calculadora:
    #Método para sumar dos números
    def sumar(self, a, b):
        return a + b
    
    #Método para restar dos números
    def restar(self, a, b):
        return a - b
    
    #Método para multiplicar dos números
    def multiplicar(self, a, b):
        return a * b
    
    #Método para dividir el primer número entre el segundo e incluye validación para evitar división por cero
    def division(self, a, b):
        if b == 0:
            raise ValueError ("No se puede dividir por cero")
        return a / b