# def sum_two_num(num1,num2):
#     print(num1+num2)


# sum_two_num(1,2)

# def print_name(name='ali'):
#     print(name)


# print_name()
# print_name('alex')

# def give_squre_two(num):
#     return num**2

'''

def sum_nums(num1,num2):
    return num1+num2

def mines_nums(num1,num2):
    return num1-num2
def div_nums(num1,num2):
    return num1/num2

def multi_nums(num1,num2):
    return num1*num2


def pow_nums(num1,num2):
    return num1**num2


def fac_num(num):
    f = 1
    for n in range(num,0,-1):
        f = f*n
    return f




# start the calc
greeding = """
hi welcome 
ops are:
+   sum
-   mines
/   divide
*   multiple
**  pow
!   factoreal


"""
print(greeding)
while True:
    op = input('_>enter opreation: ')
    if op == '+':
        n1 = int(input('enter first number: '))
        n2 = int(input('enter second number: '))
        print(f'sum is: {sum_nums(n1,n2)}')
    elif op == '-':
        n1 = int(input('enter first number: '))
        n2 = int(input('enter second number: '))
        print(f'mines is: {mines_nums(n1,n2)}')
    elif op == '*':
        n1 = int(input('enter first number: '))
        n2 = int(input('enter second number: '))
        print(f'multiple is: {multi_nums(n1,n2)}')
    elif op == '/':
        n1 = int(input('enter first number: '))
        n2 = int(input('enter second number: '))
        print(f'devide is: {div_nums(n1,n2)}')
    elif op == '!':
        n1 = int(input('enter number: '))
        print(f'factorail is: {fac_num(n1)}')
    else:
        print('i dont get it \ntry again!!')
        

'''


# a person with name - age - height -wieght

class Person:
    def __init__(self,name,age,hight,wight):
        self.name = name
        self.age = age
        self.hight = hight
        self.wight = wight
        print(f'{name} has created')
    
    def bmi(self):

        # wight/hight**2
        bmi = self.wight/(self.hight**2)

        return bmi
    
    def seconds(self):
        year = 60 * 60 * 24 * 365
        return self.age * year
    
    def change_name(self,new_name):
        self.name = new_name


    

a = Person('ali',21,170,60)
# print(a.age)
# print(a.seconds())
print(a.name)

a.change_name('alex')

print(a.name)



