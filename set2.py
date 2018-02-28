class Polynomial:
                
        def __init__(self,coef):
                """
                The constructor takes an argument coef,
                which is a list of coefficients of the polynomial.
                Pre-condition: coef is the list of numbers
                """
                self.coef=coef		
                

        def __str__(self):
                poly=''
                for i in range(len(self.coef)):
                        poly=poly+str(self.coef[i])+'x^'+str(i)
                        if(i!=len(self.coef)-1):
                                poly=poly+'+'
                return poly

        def add(self,p):
                """
                The function should add the polynomial with another
                polynomial p, passed as argument.
                Return the Polynomial object representing the sum.
                Pre-condition: p is an object of Polynomial type
                """
                deg1=len(self.coef)
                deg2=len(p.coef)
                l2=[]
                if deg1<deg2:
                        for x in range(deg2):
                                if x<deg1:
                                        k=self.coef[x]+p.coef[x]
                                        l2.append(k)
                                else:
                                        l2.append(p.coef[x])
                if deg2<=deg1:
                        for x in range(deg1):
                                if x<deg2:
                                        k=self.coef[x]+p.coef[x]
                                        l2.append(k)
                                else:
                                        l2.append(self.coef[x])
                p2=Polynomial(l2)
                return p2
        def multiply(self,p):
                """
                The function should multiply the polynomial with another
                polynomial p, passed as argument.
                Return the Polynomial object representing the product.
                Pre-condition: p is an object of Polynomial type
                """
                deg1=len(self.coef)
                deg2=len(p.coef)
                l2=[]
                for x in range((deg1-1)+(deg2-1)+1):
                        l2.append(0)
                for x in range(deg1):
                        for y in range(deg2):
                                k=self.coef[x]*p.coef[y]
                                index=x+y
                                l2[index]=l2[index]+k
                p2=Polynomial(l2)
                return p2
if __name__=="__main__":
        p1=Polynomial([1,-2,3,4])
        print("p1 is "+str(p1))
        p2=Polynomial([2,2])
        a=p1.add(p2)
        print()	
        print(str(p1)+" + "+str(p2)+" is ")
        print(str(a))
        p3=Polynomial([2,2,4,4,5])
        a=p1.add(p3)
        print()
        print(str(p1)+" + "+str(p3)+" is ")
        print(str(a))
        a=p1.multiply(p2)
        print()	
        print(str(p1)+" * "+str(p2)+" is ")
        print(str(a))
        p4=Polynomial([1,-2,3])
        p5=p2.multiply(p4)
        print()	
        print(str(p2)+" * "+str(p4)+" is ")
        print(str(p5))
        p5=p1.multiply(p4)
        print()	
        print(str(p1)+" * "+str(p4)+" is ")
        print(str(p5))

