# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных
# числа) для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
# наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
# среднего.
from collections import defaultdict


companies_qty = int(input('Enter quantity of companies: '))
companies_names = [input(f'Enter name of company {i+1}: ') for i in range(companies_qty)]
companies_profit = defaultdict(list)
companies_annual_profit = defaultdict(int)

for name in companies_names:
    for quarter in range(4):
        companies_profit[name] += [int(input(f'Enter profit in quarter {quarter+1} for company {name}: '))]

for name in companies_names:
    companies_annual_profit[name] = sum(companies_profit[name])

ave_company_profit = (sum(companies_annual_profit.values())) / companies_qty
print('_' * 100)
print(f'average annual company profit {ave_company_profit}')
print('_' * 100)
print('Companies with profit less then average:')
for company in [name for name in companies_annual_profit.keys() if companies_annual_profit[name] < ave_company_profit]:
    print(company)
print('_' * 100)
print('Companies with profit more then average:')
for company in [name for name in companies_annual_profit.keys() if companies_annual_profit[name] >= ave_company_profit]:
    print(company)


