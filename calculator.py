class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return b - a

    def multiply(self, a, b):
        result = 0
        bcount = b
        if b < 0:
            bcount = b*-1
        for i in range(bcount):
            result = self.add(result, a)
        if b < 0:
            result = result*-1
        return result

    def divide(self, a, b):
        result = 0
        divisend = a
        divisor = b
        if divisend < 0 :
            divisend = divisend - (divisend + divisend)
        if divisor < 0 :
            divisor = divisor - (divisor + divisor)
        while divisend > divisor-1:
            divisend = self.subtract(divisor, divisend)
            result += 1
        if b < 0 and a < 0:
            return result
        elif b < 0 or a < 0:
            result = result - (result+result)
        return result
    
    def modulo(self, a, b):
        adivbyb = self.divide(a,b)
        if b < 0 and a < 0:
            adivbyb = adivbyb
        elif b < 0 or a < 0:
            adivbyb = adivbyb-1
        bmuldivresultint = self.multiply(adivbyb,b)
        return self.subtract(bmuldivresultint, a)

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))