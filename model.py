import DATA
import time
from psycopg2 import errors


def DELL_REQUEST(name_table):
    colum = ''
    for x in DATA.data_DELL:
        if x == name_table:
            colum = DATA.data_DELL[x]
            break
    if colum == '':
        return 'error'
    query = f''' DELETE FROM {name_table}  WHERE {colum} = %s ;'''
    return query

def UPDATE_REQUEST(name_table,colum_name_set):
  #  print(colum_name_set)
    for x in DATA.data:
        if x == name_table:
            colums = DATA.data_DELL[x]
           # tmp,count = list_to_other((DATA.data[x]))
    count = len(colum_name_set)
    if count == 3:
        query = f''' UPDATE {name_table} set {colum_name_set[0]}  = %s   WHERE {colums}  = %s ; '''
    if count == 5:
        query = f''' UPDATE {name_table} set {colum_name_set[0]}  = %s, {colum_name_set[2]}  = %s  WHERE {colums}  = %s ; '''
    if count == 7:
        query = f''' UPDATE {name_table} set {colum_name_set[0]}  = %s, {colum_name_set[2]}  = %s , {colum_name_set[4]}  = %s  WHERE {colums}  = %s ; '''

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
       # print(INSERT + name_table + colums + VAL + end)
        return INSERT + name_table + colums + VAL + end
    except (Exception,TypeError):
        print ('error')
        return -1


def Insert(conn,cur,name_table,tmp):
    try:
        data = tmp
        error_test = True
        for x in DATA.data:
            if x == name_table:
                error_test = False
        if   error_test:
            print("error")
            return 4

        postgres_insert_query = INSERT_REQUEST(name_table)
        colums, count = list_to_other(DATA.data[name_table])
        check = count

        if check == 1:
            record_to_insert = (data[0],)
        if check ==  2:
            record_to_insert = (data[0], data[1])
        elif check == 3:
            record_to_insert = (data[0], data[1], data[2])
        #print(INSERT_REQUEST('books'))

        cur.execute(postgres_insert_query, record_to_insert)
    except Exception:
        print("error")
        return -1
    else:
        conn.commit()


def DELL(conn,cur,name_table,id):
    try:
        error_test = True
        for x in DATA.data:
            if x == name_table:
                error_test = False
        if error_test:
            print("error")
            return 4
        postgres_delte = DELL_REQUEST(name_table)
        postgres_delte = str(postgres_delte)
        delete = (id,)
        #print(postgres_delte,delete)

        cur.execute(postgres_delte,delete)
    except Exception:
        print("error")
        return
    else:
        conn.commit()


def Update(conn,cur,name_table,tmp):
    try:
        error_test = True
        for x in DATA.data:
            if x == name_table:
                error_test = False
        if error_test:
            print("error")
            return 4
        postgre_update = UPDATE_REQUEST(name_table,tmp)
        count = len(tmp)
        #print(tmp)
        if count == 3:
            postgre_update_values = (tmp[1], tmp[-1])
        elif count == 5:
            postgre_update_values = (tmp[1], tmp[3], tmp[-1])
        elif count == 7:
            postgre_update_values = (tmp[1], tmp[3],tmp[5], tmp[-1])
       # print(postgre_update)

        cur.execute(postgre_update,postgre_update_values)
    except Exception:
        print("error")
        return
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
        print("input correct data")
        return "input correct data"
    try:
        count = int(count)
    except (TypeError,ValueError):
        print ("input correct data")
        return
    try:
        while i < count:
            cur.execute(sql)
            i +=1
        if i == count :
            end = False
    except errors.ForeignKeyViolation:
          print( "input correct data")
          raise
    finally:
         conn.commit()
         return 1


def generate_big(conn, cur, count,mod):
    end = True
    i = 0
    if mod == '1':
        sql = 'INSERT INTO id_genry (genry) select chr(trunc(65 + random()*25)::int)|| chr(trunc(65 + random()*25)::int)' \
              ' || chr(trunc(65 + random()*25)::int) || chr(trunc(65 + random()*25)::int) ' \
              '|| chr(trunc(65 + random()*25)::int ) limit  1 '
    elif mod =='2':
        sql = "INSERT INTO readers(name,surname,phone_number) select chr(trunc(65 + random()*25)::int)|| chr(trunc(65 + random()*25)::int)||" \
              " chr(trunc(65 + random()*25)::int)," \
              "chr(trunc(65 + random()*25)::int)|| chr(trunc(65 + random()*15)::int) || chr(trunc(65 + random()*30)::int)," \
              "trunc(random()*100000000)::int limit 1"
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

def First_request(conn, cur):
    sql = f'''select j.id_records , r.name , b.name_book ,g.genry
        from public.journal j inner join public.readers r on j.id_readers = r.id_readers 
        inner join public.books b on j.id_books = b.id_boooks 
        inner join  public.id_genry g on b.genry = g.id_genry'''
    try:
        start = int(round(time.time() * 1000))
        cur.execute(sql)
        end = int(round(time.time() * 1000)) - start
        return end, cur.fetchall()
    finally:
        conn.commit()

#shows the date of birth of the reader who took the oldest book
def Second_request(conn, cur):
    sql = f'''select public.readers.name from public.readers where public.readers.id_readers =(
                (select public.journal.id_readers from public.journal where public.journal.data_time in 
                (select  MIN (public.journal.data_time) from public.journal )))'''
    try:
        start = int(round(time.time() * 1000))
        cur.execute(sql)
        end = int(round(time.time() * 1000)) - start
        return end, cur.fetchall()
    finally:
        conn.commit()
#
def Third_request(conn, cur,genry):
    sql = f'''select public.readers.name from public.readers where public.readers.id_readers in (
            (select public.journal.id_readers from public.journal where public.journal.id_books in
            (select public.books.id_boooks from public.books where public.books.genry in
             (select public.id_genry.id_genry from public.id_genry  where public.id_genry.genry LIKE  '{genry}'))))'''
    try:
        start = int(round(time.time() * 1000))
        cur.execute(sql)
        end = int(round(time.time() * 1000)) - start
        return end, cur.fetchall()
    except errors :
        print('error')
    finally:
        conn.commit()



