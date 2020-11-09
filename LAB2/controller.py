import os
import view
import model
import DATA

def menu(conn, cur):

    while 1:
       number = view.Menu()
       if number == '1':
            mod, table_name, colums = view.task_1()
            if mod == 1:
                model.Insert(conn, cur,table_name,colums)
            elif mod == 2:
                model.DELL(conn,cur,table_name,colums[0],colums[1])
            elif mod == 3:
                model.Update(conn,cur,table_name,colums)
            elif mod == 4:
                continue
       if number == '2':
           mod, colums = view.task_2()
           if mod == 1:
               try:
                test = 0
                test = int(colums[0])
                print(test)
                tmp =  model.Generate(conn, cur,test , colums[1])
                print(tmp)
               except(TypeError):
                   if tmp == 1:
                        continue
                   print('correct N , please')
               finally:
                   print("after generate")
                   for x in DATA.data:
                       if x == colums[1]:
                           print(DATA.data[x])
                           break
                   cur.execute(f'select * from {colums[1]} ')
                   row = cur.fetchall()
                   for x in row:
                       print(x)
                   continue
           elif mod == 2:
               model.generate_big(conn, cur, 100000, "books")
           elif mod == 3:
               model.generate_big(conn, cur, 100000, "author")
           elif mod == 4:
               break
       if number == '3':
            mod, colums = view.task_3()
            if mod == 1 :
               time, views =  model.First_request(conn, cur,colums[0],colums[1])
               print("time",time)
               print('result :',views)
               os.system('pause')
            elif mod == 2:
                time, views = model.Second_request(conn, cur)
                print("time", time)
                print('result :', views)
                os.system('pause')
            elif mod == 3:
                time, views = model.Third_request(conn, cur,colums)
                print("time", time)
                print('result :', views)
                os.system("Pause")
            elif mod == 4:
                break
            else:
                continue

       else :
           break








