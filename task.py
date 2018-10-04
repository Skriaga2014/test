
import random
list_var = "~\|/"
list = []
for i in range(10):
    rand = random.choice(list_var)
    if rand == "~":
        if i == 0 or list[i-1] == "-":
            rand = "-"
    list.append(rand)

print(list[0]+list[1]+list[2]+list[3]+list[4]+list[5]+list[6]+list[7]+list[8]+list[9])

print("Введите изменения в форме \"00\", где:\n"
      "первая цифра - позиция звена электроцепи\n"
      "вторая цифра - количество поворотов по часовой стрелке\n")



while list != ["-","-","-","-","-","-","-","-","-","-"]:
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

        #print((list_var.index(list[pos])+tur)%len(list_var))
        list[pos] = list_var[(list_var.index(list[pos])+tur)%len(list_var)]
        s = 0
        if list[pos] == "~":
            while pos+s < len(list) and list[pos+s] == "~":
                list[pos+s] = "-"
                s +=1
        print(list[0] + list[1] + list[2] + list[3] + list[4] + list[5] + list[6] + list[7] + list[8] + list[9])
        #print(list)

print("!!!!!END!!!!!")

