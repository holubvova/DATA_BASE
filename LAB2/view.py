import DATA


menus = '''"Hello,\nselect a menu item and enter the number:"
           
            1 - Task_1
            2 - Tast_2
            3 - Task_3
            4 - exit
Input:'''

TASK1 = '''Select number
        1 - Insert
        2 - DELL
        3 - Update
        4 - back '''
data_views = '''
    'name_table' : [coloms] 

    "genryy" : ['genry_id','genry'],
    "books_details" : ['book_id', 'genry_id'],
    "journal_of_books" : ['id_name', 'book_id','date_from','date_to'],
    "books" : ['book_id', 'name_book'],
    "authors_details" : ['author_id', 'book_id'],
    "author" : ['autor_id', 'author_name'],
    "names_datas" : ['name_id', 'name','prizvishche'],
    "names" : ['id_name', 'birthday','adress'],
    "book_author" : ['book_id', 'author_id'],
    "books_name" : ['book_id','years_print']
'''



def Menu() :
    print(menus)
    while 1:
        number = input()
        if number in ['1', '2', '3']:
            return number
        elif number == '4':
            return 4
        else:
            print("input correct number")
            continue

def task_1():
    print(TASK1)
    while 1:
        number = input()
        if number == '1':
            print(data_views)
            print('please, input for example:\ngenryy 6 test\n')
            while 1:
                table_name = input()
                tmp = table_name.split()
                if tmp[1].isdigit():
                    try:
                        coloms = tuple(tmp[1],tmp[2])
                        return 1, tmp[0] , coloms
                    except (Exception, TypeError):
                        print('input correct data or 4-exit')
                else:
                    print('input correct data or 4-exit')
                    continue
        elif number == '2':
            print(data_views)
            print('please, input for example:\ngenryy genry_id 99\n')
            while 1:
                table_name = input()
                tmp = table_name.split()
                print(tmp)
                if tmp[2].isdigit():
                    try:
                        coloms = (tmp[1],tmp[2],)
                        print(coloms)
                        return 2, tmp[0],coloms
                    except (Exception):
                        print('1input correct data or 4-exit')
                else:
                    print('input correct data or 4-exit')
                    continue
        elif number == '3':
            print(data_views)
            print('please, input for example:\nname_table set_colums   data       where_coloms    id'
                                            '\ngenryy      genry       літопис    genry_id         87\n')
            while 1:
                table_name = input()
                tmp = table_name.split()
                if table_name == '4':
                    return 4, 0, 0
                if len(tmp) > 4:
                    print(tmp)
                    clms = tmp[1:]
                    print(clms)
                    try:
                        coloms = tuple(clms)
                        print(coloms)
                        return 3, tmp[0],coloms
                    except (Exception):
                        print('input correct data or 4-exit')
                else:
                    print('input correct data or 4-exit')
                    continue

        if number == '4':
            return 4 , 0, 0
        else:
            print("input correct number")
            continue

def task_3():
    print('''about request:"
          1.Author of a book that was read over time
          2.Shows the date of birth of the reader who took the oldest book
          3.Displays the genre of books written by the author\n
           1 - First  request 
           2 - Second request 
           3 - Third request  
           4 - exit ''')
    while 1:
        request = input()
        if request == '1':
            print('''about request: Author of a book that was read over time
                    Input data for example:
                      data_from  data_to
            example: 2020-04-10  2020-06-20''')
            data = input()
            tmp =data.split()
            return 1, tmp
        if request == '2':
            print('''about request: shows the date of birth of the reader who took the oldest book''')
            return 2, 0
        if request == '3':
            print('''about request: displays the genre of books written by the author
                             Example: Марк Твен ''' )
            data = input()
            return 3, data
        if request == '4':
            return 4 , 0

def task_2():
    print("""about: data generation
            1 - generation of n rows for a specific table
            2 - generation of 100,000 rows for two tables to choose from""")
    while 1:
        request = input()
        if request == '1':
             #print('''choose table and enter the number of new lines ''')
            for x in DATA.data:
                print(x)
            print('''
                     choose table and enter the number of new lines 
                        example :  N  table_name 
                                   7 genryy      ''')
            data = input()
            tmp = data.split()
            return 1, tmp
        if request == '2':
            print('''choose table
                        1 - books
                        2 - author ''')
            data = input()
            if data == '1':
                return 2 , data
            elif data == '2':
                return 3 , data
            else :
                return 4 , 0

