def func_name(name,age):
    print("hello " +name+"You are: " + str(age))

func_name("Mike",12)
func_name("Steve",13)

'''def cube(num):
    return num*num*num
print(cube(3))'''

'''is_male = False
is_tall = True 
if is_male or is_tall:
    print("You are a male and tall")
elif is_male and not(is_tall):
    print("You atre a short male")
else:
    print("You are not a male not tall")'''

'''def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
print(max_num(1,20,3))'''

#calc
'''num1 = float(input("Enter the first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
else: 
    print(num1/num2)'''

#dictionary
#dictionary: key: value
# good cz any data type and can put default value also
'''monthCoverstions = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April"
}

#print(monthCoverstions["Apr"])
print(monthCoverstions.get("Dec", "Not a valid key"))'''
