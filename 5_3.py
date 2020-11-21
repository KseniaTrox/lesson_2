# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников
with open('payslip.txt', 'r', encoding='utf-8') as sp_file:
    r_dict = {line.split()[0]: float(line.split()[1]) for line in sp_file}
    print(r_dict)

    sp_r = sum(r_dict.values()) / len(r_dict)
    sp_lit = [i[0] for i in r_dict.items() if i[1] < 20000]
    print(f'Cредний доход: {sp_r}')
    print(f'Ниже 20тыс. получают: {sp_lit}')