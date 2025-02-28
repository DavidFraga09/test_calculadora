#Importar del módulo unittest para poder realizar pruebas unitarias
import unittest

#Importacion de la clase Calculadora desde el archivo calculadora.py
from calculadora import Calculadora

#Definición de la clase de pruebas que hereda unittest.TestCase
class testCalculadora(unittest.TestCase):
    #Método que se ejecita antes de cada prueba
    def setUp(self):
    # Creamos una instancia de Calculadora para usar en las pruebas
        self.calc = Calculadora()

    #Prueba del método suma
    def test_suma(self):
    #Prueba la suma de dos números positivos
        self.assertEqual(self.calc.sumar(5, 4), 9) #failUnlessEqual assertEquals
    # Prueba la suma de un número positivo y un número negativo
        self.assertEqual(self.calc.sumar(1, -1), 0)
    # Prueba la suma de dos ceros
        self.assertEqual(self.calc.sumar(0, 0), 0)

    #Prueba del método resta
    def test_resta(self):
    # Prueba la resta de dos números positivos
        self.assertEqual(self.calc.restar(5, 4), 1)
    #Prueeba la resta de dos números iguales
        self.assertEqual(self.calc.restar(5, 5), 0)
    #Prueba la resta de dos números negativos
        self.assertEqual(self.calc.restar(-5, -5), 0)

    #Prueba del método multiplicación
    def test_multiplicacion(self):
    #Preuba la multiplicacion de dos números positivos
        self.assertEqual(self.calc.multiplicar(5, 4), 20)
    #Prueba la multiplicacion de dos números positivos (debe dar cero)
        self.assertEqual(self.calc.multiplicar(5, 0), 0)
    #Preuba la multiplicación de dos números negativos
        self.assertEqual(self.calc.multiplicar(-5, -5), 25)
    #Prueba la multiplicación de un número negativo por uno positivo
        self.assertEqual(self.calc.multiplicar(-5, 5), -25)

    #Prueba del método división
    def test_division(self):
        #Prueba la división exacta
        self.assertEqual(self.calc.division(10, 2), 5)
        #Prueba la división con resultado decimal
        self.assertEqual(self.calc.division(10, 4), 2.5)
        #Prueba con división periódica usando assertAlmostEqual para comparar la precisión limitada
        self.assertAlmostEqual(self.calc.division(22, 7), 3.142857142857143, places=15)
        #Prueba especifica para verificar el manejo de la división por cero
        with self.assertRaises(ValueError):
            self.calc.division(5, 0)

    #Bloque condicional que permite ejecutar las pruebas directamente
    if __name__ == '__main__':
        #Inicializar ejecución de todas las pruebas definidas en la clase
        unittest.main()