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
    "books" : [ 'author','name_book','genry'],
    "journal" :['id_readers','id_books','data_time'],
    "id_genry" :[ 'genry'],
    "readers" : ['name','surname','phone_number']
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
            print('please, input for example:\n'
                  '[name_table new_value new_value  new_value]'
                  '\n books    Mark_tven 15_capitan 12'
                  '\n'
                  '\n ')
            while 1:
                table_name = input()
                tmp = table_name.split()
                try:
                    copy_list = []
                    if tmp[0] == 'journal' and len(tmp) == 5:
                        str = tmp[3] +' '+ tmp[4]
                        tmp[3] = str
                        del tmp[-1]
                    for i in range(0, len(tmp)-1):
                        copy_list.append(tmp[i+1])
                    coloms = tuple(copy_list)
                    if len(coloms) == 0:
                        print("input correct data\nerror")
                        return 4, 0 ,0
                    return 1, tmp[0] , coloms
                except (Exception, TypeError,ValueError):
                    print('input correct data or 4-exit')
                    continue
                else:
                    print('input correct data or 4-exit')
                    continue
        elif number == '2':
            print(""""books" : 'id_books',
                  "journal" :'id_records' ,
                  "id_genry" :'id_genry',
                  "readers" : 'id_readers'""")
            print('please, input for example:\nbooks  99\n')
            while 1:
                table_name = input()
                tmp = table_name.split()
                if table_name == '4': break
                if len(tmp) == 2 and tmp[1].isdigit() :
                    try:
                        # coloms = (tmp[1],)
                        # print(coloms)
                        return 2, tmp[0],int(tmp[1])
                    except (Exception):
                        print('1input correct data or 4-exit')
                else:
                    print('input correct data or 4-exit')
                    continue
        elif number == '3':
            print(data_views)
            print('please, input for example:\nname_table   set_colums   data           id'
                                            '\nid_genry      genry       літопис        87\n')
            while 1:
                table_name = input()
                tmp = table_name.split()
                if table_name == '4':
                    return 4, 0, 0
                if len(tmp) > 3:
                   # print(tmp)
                    clms = tmp[1:]
                    #print(clms)
                    try:
                        coloms = tuple(clms)
                       # print(coloms)
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
          1.displays a table with the reader's name, which book he took and its genre
          2.displays the name of the reader who is reading the book that was taken the oldest
          3.displays the names of readers who have taken books of a certain genre\n
           1 - First  request 
           2 - Second request 
           3 - Third request  
           4 - exit ''')
    while 1:
        request = input()
        if request == '1':
            return 1, 0
        if request == '2':
            print('''displays the name of the reader who is reading the book that was taken the oldest''')
            return 2, 0
        if request == '3':
            print('''displays the names of readers who have taken books of a certain genre
                             Example: Y ''' )
            data = input()
            return 3, data
        if request == '4':
            return 4 , 0

def task_2():
    print("""about: data generation
            1 - generation of n rows for a specific table
            2 - generation of 10,000 rows for two tables to choose from""")
    while 1:
        request = input()
        if request == '1':
             #print('''choose table and enter the number of new lines ''')
            for x in DATA.data:
                print(x)
            print('''
                     choose table and enter the number of new lines 
                        example :  N  table_name 
                                   7 id_genry      ''')
            data = input()
            tmp = data.split()
            return 1, tmp
        if request == '2':
            print('''choose table
                        1 - id_genry
                        2 - readers ''')
            data = input()
            if data == '1':
                return 2 , data
            elif data == '2':
                return 3 , data
            else :
                return 4 , 0