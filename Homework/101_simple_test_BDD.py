# name
user_name = str(input('Please your name: '))
user_surname = str(input('Please enter your surname: '))

# years
year_of_birth = int(input('Please enter your year of birth: '))
current_year = int(input('Please enter current year: '))

age = current_year - year_of_birth

# code parts
code_1 = '354'
code_3 = 132

# code 2 data
x = 152
y = 132

a = x % y
b = a * 13
c = b ** 0.5
d = int(c)

secret_code = str(code_1) + '-' + str(d) + '-' + str(code_3)

#output
print('Hello ' + user_name + ' ' + user_surname +
      '. You are ' + str(age) + ' years old. Your secret code is ' +
      secret_code + '.')
