"""
Завдання 2:
Напишіть програму, яка запитує користувача ввести число,
а потім конвертує його в ціле число і виводить його.
Обробіть виняток, якщо введені дані не можна конвертувати в число.
"""

try:
    number = int(input("Input number: "))
    print(number)
except ValueError as er:
    print(f"You should input number!\n{er}")
except Exception as exp:  #На всяк випадок пошук інших помилок
    print(f"Unexpected error! {exp}\nTry again next time.")
finally:
    print("Good buy!")
