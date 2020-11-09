import DATA
import time
from psycopg2 import errors


def DELL_REQUEST(name_table,colum):
    query = f''' DELETE FROM {name_table}  WHERE {colum} = %s ;'''
    return query

def UPDATE_REQUEST(name_table,colum_name_set):
    for x in DATA.data:
        if x == name_table:
            colums,count = list_to_other(DATA.data[x])
    if count == 2:
        query = f''' UPDATE {name_table} set {colum_name_set[0]}  = %s   WHERE {colum_name_set[2]}  = %s ; '''
    if count == 3:
        query = f''' UPDATE {name_table} set {colum_name_set[0]}  = %s, {colum_name_set[2]}  = %s  WHERE {colum_name_set[6]}  = %s ; '''
    if count == 4:
        query = f''' UPDATE {name_table} set {colum_name_set[0]}  = %s, {colum_name_set[2]}  = %s , {colum_name_set[6]}  = %s  WHERE {colum_name_set[8]}  = %s ; '''

    return query


def list_to_other(tmp):
    total = ""
    for i in range(0, len(tmp)):
        total = total + tmp[i] + ','
    #print(total)
    total = '(' + total[:-1] + ')'
    return total, len(tmp)



def INSERT_REQUEST(name_table):
    INSERT = """INSERT INTO """
    VAL = """VALUES """
    for x in DATA.data:
        if x == name_table:
            colums,count = list_to_other(DATA.data[x])
    end = ''
    try :
        for i in range(0,count):
            end =  end +'%s,'
        end ='(' + end[:-1]+')'
        return INSERT + name_table + colums + VAL + end
    except (Exception,TypeError):
        print ('error')


def Insert(conn,cur,name_table,tmp):
    data = tmp
    postgres_insert_query = INSERT_REQUEST(name_table)
    colums, count = list_to_other(DATA.data[name_table])
    check = count
    if check ==  2:
        record_to_insert = (data[0], data[1])
    elif check == 3:
        record_to_insert = (data[0], data[1], data[2])
    elif check == 4:
        record_to_insert = (data[0], data[1], data[2], data[3])
    # print(INSERT_REQUEST('journal_of_books'))
    try:
        cur.execute(postgres_insert_query, record_to_insert)
    except Exception:
        print("error")
    else:
        conn.commit()

def DELL(conn,cur,name_table,name_colum,id):
    postgres_delte = DELL_REQUEST(name_table,name_colum)
    postgres_delte = str(postgres_delte)
    delete = (id,)
    try:
        cur.execute(postgres_delte,delete)
    except Exception:
        print("error")
    else:
        conn.commit()


def Update(conn,cur,name_table,tmp):
    postgre_update = UPDATE_REQUEST(name_table,tmp)
    count = len(tmp)
    print(tmp)
    if count == 4:
        postgre_update_values = (tmp[1], tmp[3])
    elif count == 6:
        postgre_update_values = (tmp[1], tmp[3], tmp[5])
    elif count == 8:
        postgre_update_values = (tmp[1], tmp[3],tmp[5], tmp[7])
    print(postgre_update)
    try:
        cur.execute(postgre_update,postgre_update_values)
    except Exception:
        print("error")
    else:
        conn.commit()


def Generate(conn ,cur,count, table_name):
    end = True
    i = 0
    sql = ""
    for x in DATA.generate:
        if x == table_name:
            sql = DATA.generate[x]
            break
    if sql == "":
        return
    while end:
        try:
            while i < int(count):
                cur.execute(sql)
                i +=1
            if i == count :
                end = False
        except errors.ForeignKeyViolation:
               print(errors.ForeignKeyViolation)
        finally:
             conn.commit()
             if end == False:
                 cur.execute(f'select * from {table_name}')
                 row = cur.fetchall()
                 print("after generate")
                 for x in DATA.data:
                     if x == table_name:
                         print(DATA.data[x])
                         break

                 for x in row:
                     print(x)
                 return 1
             continue

def generate_big(conn, cur, count,mod):
    end = True
    i = 0
    if mod == '1':
        sql = 'INSERT INTO author ( author_name) select chr(trunc(65 + random()*20)::int)||chr(trunc(65 + random()*20)::int)' \
              ' || chr(trunc(65 + random()*20)::int)||chr(trunc(65 + random()*20)::int) || chr(trunc(65 + random()*20)::int)||chr(trunc(65 + random()*20)::int)' \
              '|| chr(trunc(65 + random()*20)::int)||chr(trunc(65 + random()*20)::int)|| chr(trunc(65 + random()*20)::int)||chr(trunc(65 + random()*20)::int)||' \
              'chr(trunc(65 + random()*20)::int)||chr(trunc(65 + random()*20)::int)|| chr(trunc(65 + random()*20)::int)||chr(trunc(65 + random()*20)::int)'
    elif mod =='2':
        sql = 'INSERT INTO books ( book_id ) select chr(trunc(65 + random()*20)::int)||chr(trunc(65 + random()*20)::int)' \
              ' || chr(trunc(65 + random()*20)::int)||chr(trunc(65 + random()*20)::int) || chr(trunc(65 + random()*20)::int)||chr(trunc(65 + random()*20)::int)' \
              '|| chr(trunc(65 + random()*20)::int)||chr(trunc(65 + random()*20)::int)|| chr(trunc(65 + random()*20)::int)||chr(trunc(65 + random()*20)::int)||' \
              'chr(trunc(65 + random()*20)::int)||chr(trunc(65 + random()*20)::int)|| chr(trunc(65 + random()*20)::int)||chr(trunc(65 + random()*20)::int)'
    else :
        return -1
    while end:
        try:
            while i < count:
                cur.execute(sql)
                i += 1
            if i == count:
                end = False
        except errors.ForeignKeyViolation:
            print("errors")
        finally:
            conn.commit()
            continue

    #author of a book that was read over time
def First_request(conn, cur,date_from,date_to):
    sql = f'''select public.author.author_name from public.author where public.author.autor_id in
                ( select public.author_details.author_id from public.author_details where public.author_details.book_id in
                ( select public.journal_of_books.book_id from public.journal_of_books 
                    where public.journal_of_books.date_from > '{date_from}' and public.journal_of_books.date_to < '{date_to}'))'''
    try:
        start = int(round(time.time() * 1000))
        cur.execute(sql)
        end = int(round(time.time() * 1000)) - start
        return end, cur.fetchone()
    finally:
        conn.commit()

#shows the date of birth of the reader who took the oldest book
def Second_request(conn, cur):
    sql = f'''select public.names.birthday from public.names where public.names.id_name in
                (select public.journal_of_books.id_name from public.journal_of_books where public.journal_of_books.book_id in
                (select public.books_name.book_id from public.books_name where public.books_name.years_print in  
                (select MIN(public.books_name.years_print) from public.books_name)))'''
    try:
        start = int(round(time.time() * 1000))
        cur.execute(sql)
        end = int(round(time.time() * 1000)) - start
        return end, cur.fetchone()
    finally:
        conn.commit()
#displays the genre of books written by the author
def Third_request(conn, cur,author):
    sql = f'''select public.genryy.genry from public.genryy where public.genryy.genry_id in
                (select public.books_details.genry_id from public.books_details where public.books_details.book_id in
                (select public.author_details.book_id from public.author_details where public.author_details.author_id in 
                (select public.author.autor_id from public.author where public.author.author_name like '{author}')))'''
    try:
        start = int(round(time.time() * 1000))
        cur.execute(sql)
        end = int(round(time.time() * 1000)) - start
        return end, cur.fetchone()
    finally:
        conn.commit()





