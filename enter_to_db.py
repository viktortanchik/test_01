import sqlite3

con = sqlite3.connect('sqlite_python.db')

def sql_insert_all(con, entities):
    cursorObj = con.cursor()

    cursorObj.execute('INSERT INTO users VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', entities)

    con.commit()

def sql_insert_one(con, entitie):
    cursorObj = con.cursor()

    cursorObj.execute(
    'INSERT INTO users(original_channel_name,picture_changed) VALUES(?,?)', entitie)

    con.commit()


def sql_update (con):
    cursorObj = con.cursor()

    cursorObj.execute('UPDATE users SET original_channel_name = "Rogers" where ROWID = 1')

    con.commit()

entities = ['original_channel_name', 'previous_channel_names', 'Date_of_submission_to_bot', 'Current_username',
            'Edited_usernames', 'picture_changed', 'How_many_times', 'Current_number_of_users_in_channel',
            'number_of_users_at_the_moment_of_insertion_into_the_bot', 'There_is_an_ad_inside']
entitie = ('test3','test4')

def sql_select(con,name):
    cursorObj = con.cursor()
    #name='original_channel_name'
    query="SELECT "+name+ " FROM users;"
    print(query)
    cursorObj.execute(query)
    one_result = cursorObj.fetchmany(-1)
    print(one_result)


def sql_del(con,name):
    cur = con.cursor()
    query="DELETE FROM users WHERE ROWID= "+str(name)+ " ;"

    cur.execute(query)
    con.commit()

sql_del(con,2)


#sql_select(con)
#sql_update(con)
#sql_insert_one(con,entitie)
#sql_insert(con, entities)