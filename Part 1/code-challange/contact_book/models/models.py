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

    def search_contacts(self, *, name=None, surname=None, address=None, phone=None):
        if name and not surname and not address and not phone:
            self.get_single_query_search("name", name)
        elif surname and not name and not address and not phone:
            self.get_single_query_search("surname", surname)
        elif address and not name and not phone and not surname:
            self.get_single_query_search("address", address)
        elif phone and not name and not surname and not address:
            self.get_single_query_search("phone", phone)
        elif not name and not surname and not address and not phone:
            print(
                "Please tell us which column you would like to search from and the search term")
        else:
            print("Only single column searches are supported at the moment")

    def get_single_query_search(self, column: str, search_term: str):
        search_query = f"SELECT * FROM contacts WHERE {column} ILIKE %s"

        self._cur.execute(search_query, (f'%{search_term}%',))
        contacts = self._cur.fetchall()
        print(tabulate(contacts, headers=[
            'id', 'name', 'surname', 'address', 'phone'], tablefmt='orgtbl'))
        self._conn.commit()

    def close_connection(self):
        self._cur.close()
        self._conn.close()
