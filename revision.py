#day 2 30 of 30 days of python
first_name = input("whats your first name? ")
last_name = input("whast last name? ")
full_name  = first_name + " " + last_name
country = input("what country are you from? ")
age = int(input("whats your age?"))
year = int(input("what year wheere you born? "))
is_married = True
is_light_on = False
brother, younger_bro, father, mother = "abdulqayyum", "habeeb", "abdulhakeem", "bashirat"
print(f"full name is: {full_name},country is: {country}, age is:{age}, year is:{year}, is_married is: {is_married}")
print(type(first_name), type(last_name), type(full_name), type(country), type(age), type(year),type(is_married))
print(len(first_name))
if len(first_name) > len(last_name):
    print("first name is longer than last name")
elif len(first_name) < len(last_name):
    print("last name is longer than firstname")
else:
    print("they re equal in length")
num_1 = 5
num_2 = 4
addition = num_1 + num_2
print(addition)
substraction = num_1 - num_2
print(substraction)
division = num_1 / num_2
print(division)
exponenciation = num_1**num_2
print(exponenciation)
floor_division = num_1//num_2
print(floor_division)
def calculate_area_circumferece():
    pi = 3.14
    r = int(input("whats radius"))
    area = pi * r**2
    circumference  = 2 *pi*r
    return (f"area is {area}, circumference is {circumference}")
print(calculate_area_circumferece())
 #day 3 of 30 days of python
your_age = int(input("whats your age? "))
your_height = float(input("whats your height "))
print("your age is:", age)
print("your height is:", your_height)
complex_no = (2 + 5j)
base = int(input("what is base of triangle? "))
height = int(input("what is height of triangle?"))
area_of_triangle = 0.5* base *height
print("area of triangle is:", area_of_triangle)

side_a = int(input("whats side a? "))
side_b = int(input("whats side b? "))
side_c = int(input("whats side c? "))
perimeter = side_a + side_b + side_c
print(perimeter)
length = int(input("what is length of rectangle?"))
width = int(input("what is width of rectangle?"))
area_of_rectangle = length * width
perimeter_of_rectangle = 2 *(length + width)
print(f"area of rectangle is {area_of_rectangle}, perimeter of rectangle{perimeter_of_rectangle}")
python = len("python")
dragon = len("dragon") 
print(f"the length of pythin is:{python} and the length of dragon is {dragon}")
print("on" in ("python" and "dragon"))
print("jargon" in "i hope this is not full of jargon")
float_python = float(python)
int_python = int(python)
print(float_python, int_python)
def check_if_equal():
    if 7//3 == int(2.7):
        return True
    else:
        return False
print(check_if_equal())
def check_type():
    if type(10) == type("10"):
        return True
    return False
print(check_type())
def check_if_int():
    if int(9.8) == 10:
        return True 
    return False
print(check_if_int())
hours = int(input("how many hours of work? "))
rate = float(input("what is your rate? "))
pay = hours * rate
print(f"your pay is {pay}")
years_lived = int(input("how many years have you lived? "))
seconds = years_lived * 31536000
print(f"youve lived for {seconds} seconds")
print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)
#day 4 of 30 days of code

challenge = "thirty", "days", "of" ,"python"
new = "thirty days of python"
splits = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
company = "Coding For All"
sentence = "You cannot end a sentence with because because because is a conjunction"
somehow = " coding for all "
lst_of_dict = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" ".join(challenge))

print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company[0:6])
contain = "Coding"
print(company.find(contain))
print(new.split(" "))
print(splits.split(","))
print(new[10])

print(company.index("F"))
print(company.rfind("l"))
print(sentence.index("because"))
print(sentence.rindex("because"))
print(sentence[31:54])
print(company.startswith("Coding"))
print(company.endswith("Coding"))
print("# ".join(lst_of_dict))
print(somehow.strip(" "))
print("I am enjoying this challenge.\nI just wonder what is next")
#day 5 of 30 days of python 
mixed_data_types = ["ibrahim", 17, 5.67, "single", "asadam road"]
it_companies = ["Facebook", "google", "Microsoft", "apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print(len(it_companies))
print(it_companies[0:6:3])
print(it_companies[-1])
it_companies[2] = "ram"
it_companies.append("IT")
it_companies.insert(3, "kak media")

new = it_companies[4]
print(new.swapcase())
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#sort ages
ages.sort()
#find maximum and minimum age
min_age = min(ages)
max_age = max(ages)
#add maximum and minimum age to list
ages.append(min_age)
ages.append(max_age)
#find median
middle = len(ages) //2
if len(ages) %2 == 0:
    print((ages[middle] + ages[middle-1])/2)
else:
    print(ages[middle])
print(ages)
# find average
average = sum(ages)/len(ages)
print(f"average of the list is: {average}")
#range of values
range_ages  = max_age - min_age
print(f"the range of ages is {range_ages}")
#Compare the value of (min - average) and (max - average), use abs() method
if abs(min_age - average) > abs(max_age-average):
    print("min - average is greater")
elif abs(min_age - average) < abs(max_age-average):
    print("min - average is smaller")
else:
    print("they are equal")
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
#finding the middle of the country list
first_half = []
second_half = []
midlle_country = len(countries) //2
print(countries[midlle_country])
print(len(countries[0:midlle_country]))
print(len(countries[midlle_country:]))
