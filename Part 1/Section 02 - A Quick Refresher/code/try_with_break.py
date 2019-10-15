a = 0
b = 2
# try:
#     print(a/b)
# except ZeroDivisionError as zd:
#     print('oops, division by Zero')
# finally:
#     print("this always executes")


while a < 4:
    print('....................')
    a += 1
    b -= 1

    try:
        print(a/b)
    except ZeroDivisionError:
        print(f'{a},{b} - division by 0')
        continue
    finally:
        print(f"{a},{b} - this always executes")

    print(f"{a},{b} - , main loop")
else:
    print("Code executed without a zero division error")
