def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

num = 3
if is_even(num):
    print(f"{num} є парним числом.")
else:
    print(f"{num} є непарним числом.")
