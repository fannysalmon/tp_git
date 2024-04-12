class Calculator:
    def addition(self, a, b):
        result = a + b
        return result

# Importez la classe Calculator depuis votre fichier calculator.py
from calculator import Calculator

# Créez une instance de la classe Calculator
calc = Calculator()

# Appelez la méthode addition() sur l'instance avec des valeurs d'exemple pour a et b
a = 10
b = 5
result = calc.addition(a, b)
print("Résultat de l'addition :", result)