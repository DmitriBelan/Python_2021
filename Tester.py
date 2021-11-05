import hashlib

password = 'Helloworld'
hashed_pass = hashlib.md5(password.encode()).hexdigest() [0:6]

x = 0

while True:
    pw = password + f'{x}'
    hashed_pw = hashlib.md5(pw.encode()).hexdigest() [0:6 ]
    if hashed_pass == hashed_pw:
        print(pw)
        break
    x +=1







# print(hashed_pass)
#
# user_input = input('Please enter password')
# hashed_user_input = hashlib.md5(user_input.encode()).hexdigest()
#
# if hashed_user_input == hashed_pass:
#     print(hashed_user_input)
#     print(hashed_pass)
#     print('OK')
# else:
#     print(hashed_user_input)
#     print(hashed_pass)
#     print('ERROR')
