import pandas as pd

# Домашнее задание:
# Для опроса на Stack Overflow (https://insights.stackoverflow.com/survey)
# Написать программу, которая по выбору пользователя делает следующее:

# 1. Выводит данные о том сколько программистов является профессионалами и сколько хобби программистами. (столбец 'Hobbyist')
df = pd.read_csv('..//csv_files//survey_results_public.csv')

# pd.set_option('display.max_columns', 9)  # Will set option on how many columns to show
# pd.set_option('display.max_rows', 10)  # WIll set option on hpw many rows to show
cnt1 = 0
cnt2 = 0

for MainBranch in df['MainBranch']:
    if MainBranch == 'I am a developer by profession':
        cnt1 += 1
    elif MainBranch == 'I code primarily as a hobby':
        cnt2 += 1

print('Qty of professionals is', cnt1)
print('Qty of hobbyists is', cnt2)



# 2. Выводит средний, максимальный и минимальный возраст (столбец 'Age') программистов

# print(df.nlargest(1, 'Age'))
# print(df.mean(1, 'Age'))
# print(df.nsmallest(1, 'Age'))



# 3. Выводит таблицу со странами (столбец 'Country'). Группирует, считает кол-во и выводит в порядке убывания.

print(df.sort_values('Country', ascending=True))

# 4. Выводит таблицу с валютами (столбец 'CurrencyDesc'). Группирует и выводит в порядке убывания

print(df.sort_values('Currency', ascending=False))

