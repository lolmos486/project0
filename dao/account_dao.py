import psycopg
from model.account import Account


class AccountDao:

    def get_all_accounts_by_customer_id(self, customer_id):
        with psycopg.connect(host="http://127.0.0.1", port="5432", dbname="project1", password="password") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM todos WHERE customer_id = %s", (customer_id,))

                account_list = []

                for row in cur:
                    account_list.append(Account(row[0], row[1], row[2]))

                return account_list
