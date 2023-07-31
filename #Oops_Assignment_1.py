#Assinment 1

class point:
# Task 1 :
    def __init__(self,x,y,z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z) 
# Task 2 : 
    def sqsum(self):
         return self.x**2+self.y**2+self.z**2
obj1 = point(input(),input(),input())
print('Sum of squared number : ',obj1.sqsum())







