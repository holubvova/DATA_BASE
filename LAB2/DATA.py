data = {
    "genryy" : ['genry_id','genry'],
    "books_details" : ['book_id', 'genry_id'],
    "journal_of_books" : ['id_name', 'book_id','date_from','date_to'],
    "books" : ['book_id', 'name_book'],
    "author_details" : ['author_id', 'book_id'],
    "author" : ['autor_id', 'author_name'],
    "names_datas" : ['name_id', 'name','prizvishche'],
    "names" : ['id_name', 'birthday','adress'],
    "book_author" : ['book_id', 'author_id'],
    "books_name" : ['book_id','years_print']
}

generate = {
    "genryy" : "INSERT INTO genryy (genry_id, genry)"
            "select trunc(random()*100)::int, chr(trunc(65 + random()*25)::int)||"
            "chr(trunc(65 + random()*25)::int)",

    "books_details" : 'insert into public.books_details (book_id, genry_id) '
                      'select book_id , genry_id FROM books TABLESAMPLE bernoulli(100), genryy TABLESAMPLE bernoulli(100)',

    "journal_of_books" :  "INSERT INTO journal_of_books (date_from, date_to,id_name, book_id ) "
                          "select '01.01.2000'::date -(random() * ('01.01.2000'::date -'01.01.1975'::date))::int,"
                          " '01.01.2000'::date -(random() * ('01.01.2000'::date -'01.01.1975'::date))::int, "
                          " id_name , book_id FROM  public.names TABLESAMPLE bernoulli(20),"
                          " books TABLESAMPLE bernoulli(20)",

    "books" :'INSERT INTO books ( name_book) select '
             'chr(trunc(65 + random()*20)::int)||chr(trunc(65 + random()*20)::int)',

    "author_details" : 'insert into author_details (book_id, author_id) '
                      'select book_id , autor_id FROM books TABLESAMPLE bernoulli(5), author TABLESAMPLE bernoulli(5)',

    "author" : 'INSERT INTO author ( author_name)'
                'select chr(trunc(65 + random()*20)::int)||chr(trunc(65 + random()*20)::int)',

    "names_datas" : 'INSERT INTO names_datas (name_id , name, prizvishche)'
             'select trunc(random()*100)::int,'
             'chr(trunc(65 + random()*26)::int)||chr(trunc(65 + random()*26)::int),'
             'chr(trunc(65 + random()*26)::int)||chr(trunc(65 + random()*26)::int)',

    "names" : "INSERT INTO names (id_name, birthday, adress)"
              "select trunc(random()*100)::int,"
              "'01.01.2000'::date -(random() * ('01.01.2000'::date -'01.01.1975'::date))::int,"
              " chr(trunc(65 + random()*25)::int)||chr(trunc(65 + random()*25)::int)",
            
    "book_author" : 'insert into book_author (book_id, author_id) '
                      'select book_id , autor_id FROM books TABLESAMPLE bernoulli(1), author TABLESAMPLE bernoulli(1)',

    "books_name" : "INSERT INTO books_name (years_print , book_id ) "
                   "select '01.01.2020'::date -(random() * ('01.01.2020'::date -'01.01.1950'::date))::int,"
                   " book_id  FROM books TABLESAMPLE bernoulli(1)"
}