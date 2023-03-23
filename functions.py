# number 1
a = int(input("what is a "))
b = int(input("what is b "))
def add_two_nubers(x, y):
    total = a + b
    return total
print("sum of two numbers is:",add_two_nubers(a, b))
# number 2
radius = int(input("what is the radius of circle "))
def area_of_a_circle(r, pi = 3.14):
    area = pi * r**2 
    return area
print("area of circle is:",area_of_a_circle(radius))
# number 3
def sum_of_numbers(*numbers):
    
    for number in numbers:
        if not isinstance(number, int):
            return ("all values must be integers")
    return sum(numbers)
print("sum of numbers is: ",sum_of_numbers(1,2,3,4))
# number 4
def convert_celcius_to_farenheit(C):
    F = (C * 9/5) + 32
    return F
print("farenheit: ", convert_celcius_to_farenheit(5))
# number 5
def check_season(month):
    
    if month in ["october","september","november"]:
        print("Autumn")
    elif month in ["december","january","febuary",]:
        print("winter")
    elif month in ["march", "april", "may"]:
        print("Spring")
    elif month in ["june", "july", "august"]:
        print("Summer")
print(check_season("january"))
#number 6
def calculate_slope(m,x,c):
    y = m*x + c
    return y
print(calculate_slope(2,3,5))
#number 7
def calculate_quadratic_equation(x,y,z):
    square_root = ((y**2) -(4*x*z))**(1/2)
    x_1 = (-y +  square_root)/(2*x)
    x_2 = (-y -  square_root)/(2*x)
    return x_1, x_2

print(calculate_quadratic_equation(1, -5, 6))

def take_list(*lstt):
    lst = []
    for i in lstt:
        lst.append(i)
    return lst
print(take_list("cat","god"))

def reverse_list(arr):
    reverse = []
    for i in range(len(arr)-1,-1,-1):
        reverse.append(arr[i])
    return reverse
my_arr = [1,2,3,4,5]
print(reverse_list(my_arr))
def capitalize_list(list):
    capitalized_list = []
    for item in list:
        
        capitalized_list.append(item.capitalize())
    return capitalized_list
my_liys =["cat", "mlpuse"]
print(capitalize_list(my_liys))
def add_item(list, parameter):
    
     list.append(parameter)
     return list
    
my_list = ["apple","tomato","yam"]
print(add_item(my_list, "Beans"))
def remove_item(lst, item):
    lst.remove(item)
    return lst
my_remove_list = ["ant","dog","yam"]
print(remove_item(my_remove_list,"yam"))
def sum_of_odds(odds):
    total = 0
    for i in range(odds):
        if i % 2 == 1:
            total += i
        
    return total
print(sum_of_odds(10))
def sum_of_even(evens):
    total = 0
    for i in range(evens):
        if i%2 == 0:
            total += i
    return total
print(sum_of_even(10))
# level 2
def sum_of_evens_and_odd(n):
    even_total = 0 
    odd_total = 0
    for i in range(n + 1):
        if i % 2 == 0:
            even_total +=i 
        elif i % 2 == 1:
            odd_total += i 
    return(f"even:{even_total}, odd:{odd_total}")
print(sum_of_evens_and_odd(10))


def factorial(count):
    product = 1
    for i in range(1,count+1):
        product *= i 
    return product
print(factorial(5))

def calculate_mean(list):
    total = 0
    for num in list:
        total += num
    mean = total/len(list)
    return mean 
my_mean = [1,2,3,4,5]
print(calculate_mean(my_mean))
def calculate_median(numbers):
    if len(numbers) == 0:
        return None
    numbers.sort()
    median = len(numbers)//2
    if len(numbers) % 2 == 0:
        return (numbers[median-1] + numbers[median])/2
    else:
        return numbers[median]
        
my_lll = [1,2,3,4,5,67,8,9]
print(calculate_median(my_lll))
        
def calculate_range(numbers):
    
    range = max(numbers) - min(numbers)
    return range
my_range = [1,2,3,4,5,6,7,8]
print(calculate_range(my_range))
def calculate_variance(numbers):
    mean = calculate_mean(numbers)
    lst_variance = []
    for i in numbers:
        sub = (mean - i)**2
        lst_variance.append(sub)
    variance = sum(lst_variance)/len(numbers)
    return variance

my_variance = [1,2,3,4,5]
print(calculate_variance(my_variance))
def calculate_standard_deviation(numbers):
    standard_deviation = calculate_variance(numbers) **0.5 
    return standard_deviation
def check_prime(n):
    for i in range(2, n) :
        if n % i == 0:
            return False
    return True

print(check_prime(11))
def check_unique(lst):
    set_of_list = set(lst)
    if len(set_of_list) == len(lst):
        return True
    return False
my_check = [1,2,3,4,5,6,6,77,8,9,8]
print(check_unique(my_check))
def check_data_type(lst):
    data_type = type(lst[0])
    for i in lst[1:]:
        if type(i) != data_type:
            return False
    return True
my_data = [1,2,3,45,6,"po"]
print(check_data_type(my_data))



        






    



            


