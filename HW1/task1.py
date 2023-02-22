n = int(input("Введите трехзначное число:"))
print(n)
sum_ = 0

while n > 0:
    sum_ += n % 10
    n //= 10
print(f"сумма цифр введенного вами числа = {sum_}")