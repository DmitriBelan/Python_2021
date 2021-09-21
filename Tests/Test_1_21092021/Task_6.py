users_list = input('Enter your list of items without ",": ').split()
users_list_sorted = sorted(users_list)

new_list = []

cnt = 0
for num in users_list_sorted:
    if num[cnt] == num[cnt + 1]:
        new_list.append(num[cnt])
    cnt += 1

print(new_array)
