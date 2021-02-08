from collections import namedtuple
from datetime import datetime, timezone



Data = namedtuple('Data', ('employer', 'department', 'employee_id', 'ssn'))

d = Data('Stiedemann-Bailey', 'Research and Development',
         '29-0890771', '100-53-9824')
d_fields = d._fields


d = datetime(2017, 3, 1, tzinfo=timezone.utc)
print(d)
