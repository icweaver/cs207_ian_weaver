import numpy as np

class Complex():

    """A class for creating complex numbers and performing basic algrebraic 
       operations.
    """

    def __init__(self, a, b=0):
        """ Initializes the components of Complex object
        
        INPUTS
        =======
        a: int or float
           real part of Complex object 
        b: int or float, optional, default value is 0
           imaginary part of Complex object
        """
        self.r = a
        self.i = b
        self.mag = self._mag()
        self.ang = self._ang()
    
    def conj(self):
        """ Returns complex conjugate of Complex object

        RETURNS
        ========
        z: Complex object
            complex conjugate of self

        EXAMPLES
        =========
        >>> z = Complex(1, 2)
        >>> z_conj = z.conj()
        >>> print(z_conj.r, z_conj.i)
        1 -2
        """
        real = self.r
        imag = -self.i
        z = Complex(real, imag)
        return z


    def _mag(self):
        """ Internal function to calculate norm of self

        RETURNS
        ========
        mag: float
            magnitude of self

        EXAMPLES
        =========
        >>> z = Complex(3, 4)
        >>> print(z.mag)
        5.0
        """
        mag = np.sqrt(self.r**2 + self.i**2)
        
        return mag

    def _ang(self):
        """ Internal function to calcualte angle of self in complex plane

        RETURNS
        ========
        ang: float
            angle of self

        EXAMPLES
        =========
        >>> z = Complex(2, 2)
        >>> print(round(z.ang, 4))
	0.7854
        """
        ang = np.arctan2(self.i, self.r)
        
        return ang

    def __add__(self, other):
        """ Returns the addition of self and other

        INPUTS
        =======
        self: Complex object
        other: Complex object, float, or int

        RETURNS
        ========
        z: Complex object that is the sum of self and other

        EXAMPLES
        =========
        >>> z = Complex(1, 2) + Complex(3, 4)
        >>> print(z.r, z.i)
        4 6

        >>> z = 2 + Complex(1, 2)
        >>> print(z.r, z.i)
        3 2
        """
        try:
            real = self.r + other.r
            imag = self.i + other.i
        
        except AttributeError:
            real = self.r + other
            imag = self.i 
        
        z = Complex(real, imag)
        return z
    
    __radd__ = __add__	
    
    def __sub__(self, other):
        """ Returns the subtraction of self and other

        INPUTS
        =======
        self: Complex object
        other: Complex object, float, or int

        RETURNS
        ========
        z: Complex object
           difference of self and other

        EXAMPLES
        =========
        >>> z = Complex(1, 2) - Complex(3, 4)
        >>> print(z.r, z.i)
        -2 -2

        >>> z = Complex(1, 2) - 2
        >>> print(z.r, z.i)
        -1 2
        """
        try:
            real = self.r - other.r
            imag = self.i - other.i
        
        except AttributeError:
            real = self.r - other
            imag = self.i 
        
        z = Complex(real, imag)
        return z
    
    def __rsub__(self, other):
        """ Returns the reverse subtraction of self and other

        INPUTS
        =======
        self: Complex object
        other: Complex object, float, or int

        RETURNS
        ========
        z: Complex object
           reverese difference of self and other

        EXAMPLES
        =========
        >>> z = 2 - Complex(1, 2)
        >>> print(z.r, z.i)
        1 -2
        """
        real = other - self.r
        imag = -self.i
        
        z = Complex(real, imag)
        return z
    
    def __mul__(self, other):
        """ Returns the product of self and other

        INPUTS
        =======
        self: Complex object
        other: Complex object, float, or int

        RETURNS
        ========
        z: Complex object that is the product of self and other

        EXAMPLES
        =========
        >>> z = Complex(1, 2) * Complex(3, 4)
        >>> print(z.r, z.i)
        -5 10

        >>> z = 2 * Complex(1, 2)
        >>> print(z.r, z.i)
        2 4
        """
        try:
            real = self.r*other.r - self.i*other.i
            imag = self.r*other.i + self.i*other.r
        except AttributeError:
            real = self.r*other
            imag = self.i*other
        
        z = Complex(real, imag)
        return z

    __rmul__ = __mul__	
    
    def __truediv__(self, other):
        """ Returns the quotient of self and other

        INPUTS
        =======
        self: Complex object
        other: Complex object, float, or int

        RETURNS
        ========
        z: Complex object that is the quotient of self and other

        EXAMPLES
        =========
        >>> z = Complex(1, 2) / 2
        >>> print(z.r, z.i)
        0.5 1.0

        >>> z = Complex(3, 4) / Complex(1, 2)
        >>> print(z.r, z.i)
        2.2 -0.4
        """
        try:
            conj = other.r**2 + other.i**2
            real = (self.r*other.r + self.i*other.i)/conj
            imag = (self.i*other.r - self.r*other.i)/conj
        except AttributeError:
            real = self.r/other
            imag = self.i/other
        
        z = Complex(real, imag)
        return z
    
    def __rtruediv__(self, other):
        """ Returns the quotient of other and self

        INPUTS
        =======
        self: Complex object
        other: Complex object, float, or int

        RETURNS
        ========
        z: Complex object that is the product of self and other

        EXAMPLES
        =========
        >>> z = 2 / Complex(1, 2)
        >>> print(z.r, z.i)
        0.4 -0.8
        """
        conj = self.r**2 + self.i**2
        real = (other*self.r)/conj
        imag = -(other*self.i)/conj
        
        z = Complex(real, imag)
        return z

    def __repr__(self):
        """ Prints self in the form a + bi, where self = Complex(a, b)

        RETURNS
        ========
        z: Complex object that is the product of self and other

        EXAMPLES
        =========
        >>> z = Complex(1, 2)
        >>> print(z)
        1 + 2i
        """
        if self.i >= 0:
            s = f'{self.r} + {self.i}i' 
        else:
            s = f'{self.r} - {np.abs(self.i)}i'

        return s

