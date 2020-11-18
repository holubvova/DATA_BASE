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
                continue
            elif mod == 2:
                model.DELL(conn,cur,table_name,colums)
                continue
            elif mod == 3:
                model.Update(conn,cur,table_name,colums)
                continue
            elif mod == 4:
                continue
            else :
                print("input correct data,please")
                continue
       if number == '2':
           mod, colums = view.task_2()
           if mod == 1:
                try:
                    test =int(colums[0])
                    model.Generate(conn, cur,test , colums[1])
                except (ValueError):
                    print("input correct data")
                    continue
                continue
           elif mod == 2:
               model.generate_big(conn, cur, 10000, '1')
               continue
           elif mod == 3:
               model.generate_big(conn, cur, 10000, '2')
               continue
           elif mod == 4:
               continue
       if number == '3':
            mod, colums = view.task_3()
            if mod == 1 :
               time, views =  model.First_request(conn, cur)
               print("time",time)
               print('result :')
               for x in views:
                   print(x)
               os.system('pause')
            elif mod == 2:
                time, views = model.Second_request(conn, cur)
                print("time", time)
                print('result :', views)
                os.system('pause')
                continue
            elif mod == 3:
                time, views = model.Third_request(conn, cur,colums)
                print("time", time)
                print('result :')
                for x in views :
                    print(x)

                os.system("Pause")
                continue
            elif mod == 4:
                continue
            else:
                continue

       else :
           break