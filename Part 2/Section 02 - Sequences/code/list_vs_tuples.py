from dis import dis
from timeit import timeit

compiled_tuple = compile('(1,2,3,"a")', 'string', 'eval')

print(dis(compiled_tuple))


compiled_list = compile('[1,2,3,["a"]]', 'string', 'eval')

print(dis(compiled_list))


timeit("")