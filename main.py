from flask import Flask, render_template
import util

app = Flask(__name__)

username='raywu1990'
password='test'
host='127.0.0.1'
port='5432'
database='dvdrental'

@app.route('/api/update_basket_a')

def update_basket_a():
    cursor, connection = util.connect_to_db(username,password,host,port,database)

    record = util.run_and_fetch_sql(cursor, "INSERT INTO basket_a (a, fruit_a) VALUES (5, 'Cherry');")
    record = util.run_and_fetch_sql(cursor, "SELECT * from basket_a;")
    
    if record == -1:
        return('SQL error')
        
    return 'Success!'
    
@app.route('/api/unique')

def unique():
    record = -1	
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    record = util.run_and_fetch_sql(cursor, "select DISTINCT fruit_a as Fruit from basket_a UNION select DISTINCT fruit_b from basket_b;")
    
    if record == -1:
        print('SQL error')
    else:
    	col_names = [desc[0] for desc in cursor.description]
    	log = record[:5]
    	
    util.disconnect_from_db(connection,cursor)
    
    return render_template('index.html', sql_table = log, table_title=col_names)
    

if __name__ == '__main__':
    app.debug = True
    ip = '127.0.0.1'
    app.run(host=ip)

