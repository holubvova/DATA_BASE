data = {
    "books" : [ 'author','name_book','genry'],
    "journal" :['id_readers','id_books','data_time'],
    "id_genry" :['genry'],
    "readers" : ['name','surname','phone_number']
}

data_DELL = {
    "books" : 'id_boooks',
    "journal" :'id_records' ,
    "id_genry" :'id_genry',
    "readers" : 'id_readers'
}

generate = {


    "books" : """INSERT INTO books (author,name_book,genry) select
                    chr(trunc(65 + random()*26)::int)||chr(trunc(65 + random()*26)::int),
                    chr(trunc(65 + random()*26)::int)||chr(trunc(65 + random()*26)::int),
                    id_genry FROM id_genry TABLESAMPLE bernoulli(45) limit 1""",

    "journal" :" INSERT INTO journal (data_time , id_readers, id_books)"
                "select timestamp '2020-01-10 20:00:00' + random() * "
               "(timestamp '2014-01-20 20:00:00' -timestamp '2010-01-10 10:00:00'),"
               " id_readers, id_boooks  from readers TABLESAMPLE bernoulli(33), books TABLESAMPLE bernoulli(33) limit 1 ",


    "id_genry" :"INSERT INTO id_genry (genry) select chr(trunc(65 + random()*25)::int)|| chr(trunc(65 + random()*25)::int) "
                "|| chr(trunc(65 + random()*25)::int)",

    "readers" :"INSERT INTO readers(name,surname,phone_number) select chr(trunc(65 + random()*25)::int)||"
               " chr(trunc(65 + random()*25)::int)|| chr(trunc(65 + random()*25)::int),"
              " chr(trunc(65 + random()*25)::int)|| chr(trunc(65 + random()*15)::int) || chr(trunc(65 + random()*30)::int),"
               "trunc(random()*100000000)::int",

}