year = int(input("Введите год: "))
sum = 0
if year % 4 == 0:
    for i in range(1,13):
        if i == 1 or i == 3 or i == 12 or i == 5 or i == 7 or i == 8 or i == 10:
            for i in range(1,32):
                if i > 9:
                    sum = sum + int((i/10))
                    sum = sum + (i%10)
                else:
                    sum = i + sum
        elif i == 2:
            for i in range(1,30):
                if i > 9:
                    sum = sum + int((i/10))
                    sum = sum + (i%10)
                else:
                    sum = i + sum
        else:
            for i in range(1,31):
                if i > 9:
                    sum = sum + int((i/10))
                    sum = sum + (i%10)
                else:
                    sum = i + sum
else:
    for i in range(1,13):
        if i == 1 or i == 3 or i == 12 or i == 5 or i == 7 or i == 8 or i == 10:
            for i in range(1,32):
                if i > 9:
                    sum = sum + int((i/10))
                    sum = sum + (i%10)
                else:
                    sum = i + sum
        elif i == 2:
            for i in range(1,29):
                if i > 9:
                    sum = sum + int((i/10))
                    sum = sum + (i%10)
                else:
                    sum = i + sum
        else:
            for i in range(1,31):
                if i > 9:
                    sum = sum + int((i/10))
                    sum = sum + (i%10)
                else:
                    sum = i + sum
print(sum)