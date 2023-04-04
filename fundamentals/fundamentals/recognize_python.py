num1 = 42 # declare variable, int
num2 = 2.3 #declare variable, float
boolean = True #declare variable, boolean
string = 'Hello World' #declare variable, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #declare variable, list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #declare variable, dictionary
fruit = ('blueberry', 'strawberry', 'banana') #declare variable, tuple
print(type(fruit)) #log data type of variable
print(pizza_toppings[1]) #log specific index value of list
pizza_toppings.append('Mushrooms') #add value to lsit
print(person['name']) #access value of dictionary and log
person['name'] = 'George' #change value of dictionary
person['eye_color'] = 'blue' #change value of dictionary
print(fruit[2]) #log specific index value of tuple

if num1 > 45: #conditional
    print("It's greater") #log, string
else: #run if condition is not met
    print("It's lower") #log, string

if len(string) < 5: #conditional 1
    print("It's a short word!") #log, string
elif len(string) > 15: #conditional 2
    print("It's a long word!") #log, string
else: #run if neither condition is met
    print("Just right!") #log, string

for x in range(5): #loop up to 4
    print(x) #log 0-4
for x in range(2,5): #loop from 2-4
    print(x) #log 2-4
for x in range(2,10,3): #loop from 2-9, increment by 3
    print(x) #log 2, 5, 8
x = 0 #declare variable, int
while(x < 5): #loop while x less than 5
    print(x) #log x every loop
    x += 1 #increment by one each loop

pizza_toppings.pop() #remove last index from list
pizza_toppings.pop(1) #remove index of 1 from list

print(person) #logs information held within dictionary
person.pop('eye_color') #removes eye_color key and value from dictionary
print(person) #logs updated dictionary after alteration

for topping in pizza_toppings: #loop through the lsit
    if topping == 'Pepperoni': #conditional 1
        continue #continue to next topping
    print('After 1st if statement') #log sting
    if topping == 'Olives': #conditional 2
        break #end loop

def print_hello_ten_times(): #function
    for num in range(10): #loop from 0 - 9
        print('Hello') #log string each loop

print_hello_ten_times() #calls function to run

def print_hello_x_times(x): #function with arguement
    for num in range(x): #loop for duration of argument value
        print('Hello') #log string each loop

print_hello_x_times(4) #call function, pass argument of x = 4 

def print_hello_x_or_ten_times(x = 10): #funtion with default parameter
    for num in range(x): #loop for duration of argument or default parameter
        print('Hello') #log string each loop

print_hello_x_or_ten_times() #call function, passes no argument
print_hello_x_or_ten_times(4) #call funtion, passes argument of x = 4 (overrides default parameter)


"""
Bonus section
"""

print(num3) #log var, var is undefined
num3 = 72 #declare variable, int

fruit[0] = 'cranberry' #tuples cannot be altered

print(person['favorite_team']) #undefined
print(pizza_toppings[7]) #undefined
  print(boolean) #incorrect indentation, none needed
fruit.append('raspberry') #tuples cannot be altered
fruit.pop(1) #tuples cannot be altered