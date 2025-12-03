numbers = [1, 20, 32, 20, 5, 6, 20, 7, 8, 9, 10, 10,4]
tekrar_eden_sayı = True

while tekrar_eden_sayı == True:
    for num in numbers:
        if numbers.count(num) > 1:
            numbers.remove(num)
            tekrar_eden_sayı = True
        else:
            tekrar_eden_sayı = False
numbers.sort()
print(numbers)