def song():
    print("Line 1")
    yield "I'm a lumberjack and I'm OK"
    print("Line 2")
    yield "I sleep all night and I work all day"


lines = song() # Python does not run the function
print(next(lines))
print(next(lines))
# print(next(lines))
