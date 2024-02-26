class c2dvec:
    def __init__(self,i,j) :     #This is 2d vector
        self.icap=i
        self.jcap=j

    def __str__(self) -> str:
        return (f"{self.icap}i + {self.jcap}j")    
    
class c3dvec(c2dvec):
    def __init__(self,i,j,k) -> None:# This is 3d vector
        super().__init__(i,j)
        self.kcap=k
    
    def __str__(self) -> str:
        return (f"{self.icap}i + {self.jcap}j +{self.kcap}k")
    
vector2=c2dvec(3,4)
vector3=c3dvec(3,4,2)
print(vector2)
print(vector3)       