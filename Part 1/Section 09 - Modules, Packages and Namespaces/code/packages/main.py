# import common.validators.boolean
# import common.validators.date
# import common.validators.json
# import common.validators.numeric

#  from common.validators.numeric import is_integer, is_numeric

# common.validators.json.is_json(45)

import common.validators





print('\n\n ******* self ********')


for k in dict(globals()).keys():
    print(k)


print('\n\n***** common ******')

for k in common.__dict__.keys():
    print(k)


print('\n\n***** validators ******')

for k in common.validators.__dict__.keys():
    print(k)


# print('\n\n***** numeric ******')

# for k in common.validators.numeric.__dict__.keys():
#     print(k)


