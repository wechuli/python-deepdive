import psycopg2
from tabulate import tabulate


def make_db_connection():
    try:
        conn = psycopg2.connect(user="bookuser", password="password",
                                host="127.0.0.1", port="5432", database="contactbook")

        return conn

    except (Exception, psycopg2.Error) as error:
        raise Exception(error)


class ContactBookModel:
    def __init__(self, conn):
        self._conn = conn
        self._cur = conn.cursor()

    def create_contact(self, *, name, surname=None, address=None, phone):
        insert_query = f"INSERT INTO contacts(name, surname, address, phone) VALUES (%s,%s,%s,%s)"
        self._cur.execute(insert_query, (name, surname, address, phone))
        self._conn.commit()

    def read_all_contacts(self):
        self._cur.execute("SELECT * FROM contacts")
        all_contacts = self._cur.fetchall()
        print(tabulate(all_contacts, headers=[
              'id', 'name', 'surname', 'address', 'phone'], tablefmt='orgtbl'))
        self._conn.commit()

    def delete_contact(self, id: int):
        pass

    def update_contact(self, id: int):
        pass

    def search_contacts(self, *args):
        pass

    def close_connection(self):
        self._cur.close()
        self._conn.close()
