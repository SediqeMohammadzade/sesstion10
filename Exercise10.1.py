class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def add(self, other):
        r_denominator = self.denominator * other.denominator
        r_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        result = Fraction(r_numerator,r_denominator )
        result.simplify()
        return result
    
    def multiplay(self, other):
        r_numerator = self.numerator * other.numerator
        r_denominator = self.denominator * other.denominator
        result = Fraction(r_numerator, r_denominator)
        result.simplify()
        return result
    
    def simplify(self):
        gcd = self._gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def find_gcd(self):
        a = self.numerator
        b = self.denominator
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a
    
    def subtract(self, other):
        denominator = self.denominator * other.denominator
        r_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        result = Fraction(r_numerator, denominator)
        result.simplify()
        return result
    
    def divide(self, other):
        r_numerator = self.numerator * other.denominator
        r_denominator = self.denominator * other.numerator
        result = Fraction(r_numerator, r_denominator)
        result.simplify()
        return result

    def __str__(self):
        self.simplify()
        return f"{self.numerator}/{self.denominator}"
