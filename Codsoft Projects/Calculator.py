
class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        sum=self.num1 + self.num2
        return "Output: {}+{}={}".format(self.num1,self.num2,sum)
    
    def subtraction(self):
        sub=self.num1 - self.num2
        return "Output: {}-{}={}".format(self.num1,self.num2,sub)
    
    def multiplication(self):
        mul=self.num1 * self.num2
        return "Output: {}x{}={}".format(self.num1,self.num2,mul)
        
    
    def division(self):
        if self.num2 != 0:
            div=self.num1 / self.num2
            return "Output: {}/{}={}".format(self.num1,self.num2,div)
        else:
            return "Error: Division by zero is not allowed."
    
    def power(self):
        powe=self.num1 ** self.num2
        return "Output: {}^{}={}".format(self.num1,self.num2,powe)   

print("                                               Calculator")
print("                                               Basic Calculations :)")
print("                                               _________________")
print("                                               |_______________|")
print("                                               |_7_|_8_|_9_|_x_|")
print("                                               |_4_|_5_|_6_|_-_|")
print("                                               |+/-|_0_|_._|_=_|")



print("1.Addition(+)")
print("2.Subtraction(-)")
print("3.Multiplication(*)")
print("4.Division(/)")
print("5.Power to the number\n")



while True:
    ch=int(input("Select a number from the menu: "))
    if ch==1:
        a=int(input("Enter a number -> "))
        b=int(input("Enter another number -> "))
        calc=Calculator(a,b)
        print(calc.add())
    
    elif ch==2:
        a=int(input("Enter a number -> "))
        b=int(input("Enter another number -> "))
        calc=Calculator(a,b)
        print(calc.subtraction())
        
    elif ch==3:
        a=int(input("Enter a number -> "))
        b=int(input("Enter another number -> "))
        calc=Calculator(a,b)
        print(calc.multiplication())
        
    elif ch==4:
        a=int(input("Enter a number -> "))
        b=int(input("Enter another number -> "))
        calc=Calculator(a,b)
        print(calc.division())

        
    elif ch==5:
        a=int(input("Enter a number -> "))
        b=int(input("Enter the power to the number -> "))
        calc=Calculator(a,b)
        print(calc.power())
        
    else :
        print("Thank you for using calculator :)")
        print("Select Number from the menu only")
        break