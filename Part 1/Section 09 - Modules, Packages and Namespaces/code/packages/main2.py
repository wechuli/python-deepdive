import common.models as models
import common.models.posts as posts
import common.models.users as users
import common
from common.models import User


print('\n\n ******* self ********')


for k in dict(globals()).keys():
    print(k)


print('\n\n***** common ******')

for k in common.__dict__.keys():
    print(k)


print('\n\n***** models ******')

for k in models.__dict__.keys():
    print(k)

print('\n\n***** posts ******')

for k in posts.__dict__.keys():
    print(k)


print('\n\n***** users ******')

for k in users.__dict__.keys():
    print(k)


print(User)
