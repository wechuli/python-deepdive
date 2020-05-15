import argparse
from models import make_db_connection, ContactBookModel


# make db connection or raise an error
try:
    conn = make_db_connection()
    # print("Connection to db successful")
except Exception as error:
    print("Unable to connect to the database")

# get the contact book model instance
contact_book = ContactBookModel(conn)

parser = argparse.ArgumentParser(
    description='store, read, update and delete contacts in your contact book')

# action
parser.add_argument('-a', '--action', help='choose the type of action you want to perform, create,read,update,delete',
                    type=str, required=True, dest="action", choices=['create', 'read', 'update', 'delete'])
# id
parser.add_argument('--id', help="choose the id of the user",
                    required=False, type=int, dest="user_id")

# name
parser.add_argument(
    '-n', '--name', help='enter the name of the person', dest='name')

# surname
parser.add_argument('--surname', type=str, help='surname of the user',
                    required=False, dest='surname')

# address
parser.add_argument('--address', type=str, required=False,
                    dest='address', help="address of the user")

# phone
parser.add_argument('--phone', type=int, required=False,
                    dest='phone', help='phone number')


args = parser.parse_args()
# print(args)
if args.action == 'create':
    if not args.name or not args.phone:
        print("To create a record, you must provide a minimum of name and phone values")
        exit()
    else:
        contact_book.create_contact(
            name=args.name, phone=args.phone, address=args.address, surname=args.surname)


elif args.action == 'read':
    contact_book.read_all_contacts()
elif args.action == 'update':
    print("updating")
else:
    print('delete')

