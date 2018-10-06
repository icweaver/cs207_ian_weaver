class RealExtension():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
class Complex(RealExtension):        
    def _magnitude(self):
        return np.sqrt(self.a**2 + self.b**2)
    
    def _angle(self):
        return np.arctan2(self.b, self.a)
    
    def polar(self):
        z, theta = self._magnitude(), self._angle()
        return f"polar form: {z} e^(i {theta})"
        
class Dual(RealExtension):
    def _magnitude(self):
        return np.abs(self.a)
    
    def _angle(self):
        try:
            return self.b/self.a
        except ZeroDivisionError:
            return "Can't computer angle. Undefined when a=0"
    
    def polar(self):
        mag, theta = self._magnitude(), self._angle()
        if theta == "Can't computer angle. Undefined when a=0":
            return "Can't compute polar form. Angle undefined when a=0"
        else:
            return f"polar form: {mag} * (1 + {theta} epsilon)"
