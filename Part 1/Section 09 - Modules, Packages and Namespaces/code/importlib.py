import importlib
import sys


importlib.import_module('math')
importlib.import_module('fractions')

print('math' in globals())
print(sys.modules['math'])
print(sys.modules['fractions'])


globals['math2'] = sys.modules['math']
