def func_name(name,age):
    print("hello " +name+"You are: " + str(age))

func_name("Mike",12)
func_name("Steve",13)

def cube(num):
    return num*num*num
print(cube(3))

is_male = False
is_tall = True 
if is_male or is_tall:
    print("You are a male and tall")
elif is_male and not(is_tall):
    print("You atre a short male")
else:
    print("You are not a male not tall")

def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
print(max_num(1,20,3))

#calc
num1 = float(input("Enter the first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
else: 
    print(num1/num2)

#dictionary
#dictionary: key: value
# good cz any data type and can put default value also
monthCoverstions = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April"
}

#print(monthCoverstions["Apr"])
print(monthCoverstions.get("Dec", "Not a valid key"))

#while loop - moves through the specific statement given number of times
i = 1
while i <= 10:
    print(i)
    i += 1 
print("done with loop")

#guessing game 
secret_word = "giraffe"
guess = ""
guess_count = 0 
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    # for answer
    if guess_count < guess_limit: 
        guess = input("Enter guess: ")
        guess_count+=1
    else: 
        out_of_guesses = True

if out_of_guesses: 
    print("You are out of guesses!")
else:
    print("You win!")


secret_word = "Apple"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else: 
        out_of_guesses = True

if out_of_guesses:
    print("You are out of guesses!")
else:
    print("You win!")
   
friends = ["Jim", "Karen", "Kevin"]
for index in range(5):
    if index == 0: 
        print("First")
    else: 
        print("not first")

def raise_to_number(base_num,pow_num):
    result = 1
    for index in range(pow_num):
        result = result*base_num

    return result
print(raise_to_number(3,2))

#2d lists 
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
#print(number_grid[2][2])

for row in number_grid:
    for col in row:
        print(col)

#translator: vowels are "g"

def translate(phrase):
    translation = ""
    for letter in phrase: 
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
             translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a phrase: ")))


#try/except 

try: 
    value = 10/0
    number = int(input("Ener a number: "))
    print(number)

except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")


#reading files "r" "w"write "a"append "r+"read and write
employee_file = open("employee1.txt", "w")
employee_file.write("\nkell - hr")
employee_file.close()

#modules 
#import modeule_name

#classes and objects
