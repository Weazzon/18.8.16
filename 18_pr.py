amount = 0
tickets = int(input("Введитете количество билетов: "))
for age in range (tickets):
    age = (int(input("Введите возраст посетителя:")))
    if age < 18:
        amount+= 0
    elif age >= 18 and age <= 25:
        amount+=990
    elif age >25:
        amount+=1390
    if tickets > 3:
            amount -= amount / 100 * 10
    print("Стоимость ваших билетов", amount)
