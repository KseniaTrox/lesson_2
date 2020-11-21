import json

with open('company.txt', 'w', encoding='utf-8') as f_w:
    with open('company_1.txt', 'r', encoding='utf-8') as f:
        pr = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f}

    res = [pr, {f"средняя прибыль": round(
        sum([int(i) for i in pr.values() if int(i) > 0]) / len([int(i) for i in pr.values() if int(i) > 0]))}]

    json.dump(res, f_w, ensure_ascii=False, indent=4)
    print(res)
