class Complex:
        def __init__(self,real, imag):
                """
                The constructor takes real part a 
                and imaginary part b as the arguments
                representing complex number a+bi
                Pre-condition: a and b are numeric values
                """
                self.real=real
                self.imag=imag


        def __str__(self):
                """
                Displays the complex number in the form a+bi
                """
                return( str(self.real)+'+'+str(self.imag)+'i')

        def reciprocal(self):
                """
                Spec: The function should find the reciprocal of this complex number. 
                Reciprocal of complex number a+bi is 1/(a+bi)
                The function should return an object of type Complex, representing the reciprocal
                of the form c+di. Think of rationalizing the denominator.
                Pre-condition: a,b,c and d are numeric values
                """
                a=self.real
                b=self.imag
                c=a/(a**2+b**2)
                d=(-1)*b/(a**2+b**2)
                C=Complex(c,d)
                return C
        def multiply(self,comp):
                """		
                Spec: The function takes an argument, comp, representing another 
                object of type Complex.
                The function should multiply two complex numbers, 
                the current complex number with comp
                and return the resultant object of type Complex	
                Pre-condition: comp is another Complex object		
                """
                c=self.real*comp.real-comp.imag*self.imag
                d=self.imag*comp.real+self.real*comp.imag
                C=complex(c,d)
                return C
if __name__=="__main__":
        c1=Complex(5,6)
        print("c1 is "+str(c1))
        c2=Complex(-3,4)
        print("c2 is "+str(c2))
        print()	
        c3=c1.reciprocal()
        print("Reciprocal of "+str(c1)+" is "+str(c3))
        c4=c1.multiply(c2)
        c6=Complex(2,-11)
        c7=c6.reciprocal()
        print("Reciprocal of "+str(c6)+" is "+str(c7))
        print()	
        print("Product of "+str(c1)+" and "+str(c2)+" is "+ str(c4))
        c5=c2.multiply(c1)
        print("Product of "+str(c2)+" and "+str(c1)+" is "+ str(c5))
        c8=c6.multiply(c2)
        print("Product of "+str(c6)+" and "+str(c2)+" is "+ str(c8))
        
