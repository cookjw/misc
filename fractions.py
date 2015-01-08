class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        
    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)
        
    def decimal(self):
        return float(self.numerator / self.denominator)  

    def __add__(self, other):
        a = self.numerator
        b = self.denominator
        c = other.numerator
        d = other.denominator
        return Fraction(a*d + b*c, b*d)    
    
    
    

x = Fraction(3,4)
print x

x = Fraction(1,2)
y = Fraction(1,3)
print x + y