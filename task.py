
import random
list_var = "~\|/"
list = ""
for i in range(10):
    rand = random.choice(list_var)
    if rand == "~":
        if i == 0 or list[i-1] == "-":
            rand = "-"
    list = list + rand

print(list)

print("Введите изменения в форме \"00\", где:\n"
      "первая цифра - позиция звена электроцепи\n"
      "вторая цифра - количество поворотов по часовой стрелке\n")



while list != "----------":
    ans = input()
    while len(ans) != 2 or not (ans.isdecimal()):
        print("Неверный формат ввода")
        ans = input()

    if list[int(ans[0])] == "-":
        print("это звено уже настроено")
    else:
        while len(ans) != 2 or not (ans.isdecimal()):
            print("Неверный формат ввода")
            ans = input()

        pos = int(ans[0])
        tur = int(ans[1])

        list = list.replace(list[int(ans[0])],"*")
        print(list)

print("end")

