from collections import namedtuple

Stock = namedtuple('Stock', 'symbol year month day open high low close')

djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)

# using the _replace instance method to change the values of the tuple
print(djia)

djia = djia._replace(day=26, high=26_459, close=26666636)


print(djia)

# Extending a Named Tuple
# Sometimes we want to create named tuple that extends another named tuple, appending one more fields

print(Stock._fields)

new_fields = Stock._fields + ('previous_close',)
StockExt = namedtuple('StockExt', new_fields)
