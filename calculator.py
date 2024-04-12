class Calculator:

    def addition(self,a, b):
        result = a + b
        return result
    
    def substraction(self,a, b):
        result = a - b
        return result

    
    def division(self, a, b):
        
        if b != 0:
            return a / b
        else:
            
            print("Erreur : Division par zéro !")
            return None
    


