try:
    10/0
except ZeroDivisionError:
    print('Zero division exception occured')
finally:
    print('finally ran!')


def my_func():
    try:
        10/0
    except ZeroDivisionError:
        return True
    finally:
        print('finally ran!')


my_func()


try:
    f = open('test.txt', 'w')
    f.write("Hi there")
    a = 1/0

except:
    print('an exception occurred')

finally:

    f.close()
    print('Closing file...')
