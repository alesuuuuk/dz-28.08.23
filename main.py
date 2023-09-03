if __name__ == "__main__":
    # # task one
    # while True:
    #     try:
    #         x = int(input("введіть х"))
    #         y = int(input("введіть y"))
    #         print(f"{x} в степені {y} = {x**y}")
    #         break
    #     except ValueError:
    #         print("було введено неправильне число ")
    #
    #     # task two
    #     count = 0
    #
    #     for num in range(100, 1000):
    #         if len(set(str(num))) < 3:
    #             count += 1
    #
    #     print("Кількість чисел з двома однаковими цифрами у діапазоні від 100 до 999:", count)
    #
    # # task three
    # count = 0
    #
    # for num in range(100, 10000):
    #     digits = set(str(num))  # Перетворюємо число у рядок і створюємо множину з цифр
    #     if len(digits) == len(str(num)):  # Порівнюємо розмір множини з розміром рядка числа
    #         count += 1
    #
    # print("Кількість чисел у діапазоні від 100 до 9999 з різними цифрами:", count)

    # task four
    print("Введіть ціле число")
    while True:
        try:
            number = int(input())
            break
        except ValueError:
            print("введіть ціле число!")


    number = str(number)

    number = number.replace("3", "")
    number = number.replace("6", "")
    print(number)