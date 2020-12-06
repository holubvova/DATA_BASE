import psycopg2
import controller



def main():
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(database='library',
                                user="postgres",
                                password='1705',
                                host="localhost",
                                port="5432")

        cur = conn.cursor()
        controller.menu(conn, cur)

    except (Exception, psycopg2.DatabaseError) as error:
         print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


main()