from model.customer import Customer
import psycopg
import copy


class CustomerDao:

    def get_all_customers(self):

        with psycopg.connect(host="http://127.0.0.1", port="5432", dbname="project1", password="password") as conn:

            with conn.cursor() as cur:
                cur.execute("SELECT * FROM customer")

                my_list_of_customer_objs = []

                for customer in cur:
                    u_id = customer[0]
                    customer_name = customer[1]
                    active = customer[2]

                    my_customer_objs = Customer(u_id, customer_name, active)
                    my_list_of_customer_objs.append(my_customer_objs)

                    return my_list_of_customer_objs

    def delete_customer_by_id(self, customer_id):
        with psycopg.connect(host="http://127.0.0.1", port="5432", dbname="project1", password="password") as conn:
            # Automatically close the cursor
            with conn.cursor() as cur:
                cur.execute("DELETE FROM users WHERE id = %s", (customer_id,))

                rows_deleted = cur.rowcount

                if rows_deleted != 1:
                    return False
                else:
                    conn.commit()
                    return True

    def add_customer(self, customer_object):
        customer_name_to_add = customer_object.customer_name

        with psycopg.connect(host="http://127.0.0.1", port="5432", dbname="project1", password="password") as conn:

            with conn.cursor() as cur:
                cur.execute("INSERT INTO customers (customer_name) VALUES (%s, %s) RETURNING *",
                            customer_name_to_add)

                customer_row_that_was_just_inserted = cur.fetchone()

                return Customer(customer_row_that_was_just_inserted[0], customer_row_that_was_just_inserted[1])

    def get_customer_by_id(self, customer_id):
        with psycopg.connect(host="http://127.0.0.1", port="5432", dbname="project1", password="password") as conn:

            with conn.cursor() as cur:
                cur.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))

                customer_row = cur.fetchone()
                if not customer_row:
                    return None

                u_id = customer_row[0]
                customer_name = customer_row[1]
                active = customer_row[2]

                return Customer(u_id, customer_name, active)

    def update_customer_by_id(self, customer_object):
        with psycopg.connect(host="http://127.0.0.1", port="5432", dbname="project1", password="password") as conn:

            with conn.cursor() as cur:
                cur.execute("UPDATE customers SET customer_name = %s, active_user = %s WHERE id = %s RETURNING *",
                            (customer_object.customer_name, customer_object.active, customer_object.id))

            conn.commit()

            updated_customer_row = cur.fetchone()
            if updated_customer_row is None:
                return None

            return Customer(updated_customer_row[0], updated_customer_row[1], updated_customer_row[2],)
