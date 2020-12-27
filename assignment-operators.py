year = 2019
print(year)
year = 2020
print(year)
year = year + 1
print(year)
city_rout = 23
print(city_rout)
city_rout2 = 64
print(city_rout2)
city_rout3 = 64 - 3
print(city_rout3)

Raam = 20
Laxman = Raam
Raam = 40 #Updating Raam
print(Raam, Laxman) #Laxnam remain unchanged

#Other Assignments
num = 120
print(num)
num += 100
print(num)
num -= 60
print(num)
num *= 20
print(num)
num /= 12
print(num)
num **= 2
print(num)
num //= 3
print(num)
num %= 10
print(num)

#Logical Expression
# Or, And, Not
my_number = True or False
print(my_number)
my_number = True and False
print(my_number)
my_number = False
print(not my_number)

#Bit Values True = 1, False = 0
print(100*True)
print(100*False)

#String Operation
#Comparison Operations, Concatenation, Search
#When two string have diffrent length, first one will always be < to second one
print('a'<'b')
name = 'seema'
my_name = 'seema'
print(name == my_name)
print(my_name < name)
print(name > my_name)
print(name < my_name) 

#Concatenation
# + operator can be use to add two string
first_name = "Seema"
last_name = "Chaturvedi"
fullname = first_name + " " + last_name
print(fullname)
# * allow us to multiply string in repeating pattern
print(first_name * 5)

#Search
# The in keyword can be use to find any substring in any string, if you find the substring
# it comes true
my_location = "We live in London"
print("London" in my_location)
print('mumbai' in my_location)

my_thesis = "Basically I have written two thesis one of them was on Insurance and the other one was on the stock market."
print('on the' in my_thesis)
print('finance' in my_thesis)

#Grouping Values
#List [enclose all the elements in a square bracate and seprate them with commas],
# List can be indexed and scliced
Grosary_list = ["cauliflawer2", 'lemon5', 20, 110.5, True ]
print(Grosary_list)
print(Grosary_list [4])
print(len(Grosary_list))

#Conditional Statements in Python
#if
#if-else
#if-elif-else
#if


num = 12

if num % 2 == 0 and num % 3 == 0 and num % 4 == 0:
    # Only works when num is a multiple of 2, 3, and 4
    print("The number is a multiple of 2, 3, and 4")

num = 30

if num % 2 == 0 and num % 3 == 0 and num % 5 == 0:
    #only works when num is a multiple of 2, 3, and 5
    print("The number is a multiple of 2,3, and 5")

num = 28

if num / 2 == 14 and num / 4 == 7 and num / 7 == 4:
    print("The number is a multiple of 2, 4, and 7")