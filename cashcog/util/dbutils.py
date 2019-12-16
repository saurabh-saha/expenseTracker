import psycopg2

def createConnection():
    conn = None
    try:
        conn = psycopg2.connect('dbname=xcnt host=127.0.0.1')
        return conn
    except Exception as e:
    	print('Could not connect to db', e)

    return conn

def isTableExists(cur,tableName):
    try:
        sql =   '''
                    SELECT EXISTS
                    (
                        SELECT 1 FROM information_schema.tables WHERE
                        --table_schema = 'schema_name' AND 
                        table_name = '{}'
                    )
                '''
        cur.execute(sql.format(tableName))
        row = cur.fetchone()[0]
        print(tableName, row)
        return row
    except Exception as e:
        print('Error in checking table', tableName, e)
    return False

def createTable():
    try:
        conn = createConnection()
        cur = conn.cursor()

        if not isTableExists(cur,'all_transactions'):
            sql = '''
            	create table all_transactions (
                  id bigserial,
                  data varchar,
                  created_at timestamp default now(),
                  read boolean default 'f'
	            )
            '''
            cur.execute(sql)
            conn.commit()
            print('Created table all_transactions')

        if not isTableExists(cur,'expenses'):
            sql = '''
                create table expenses (
                  id bigserial,
                  uuid varchar unique,
                  description varchar,
                  created_at timestamp,
                  amount int,
                  currency varchar,
                  updated_at timestamp default now()
                )
            '''
            cur.execute(sql)
            conn.commit()
            print('Created table expenses')

        if not isTableExists(cur,'users'):
            sql = '''
                create table users (
                  id bigserial,
                  uuid varchar references expenses(uuid),
                  emp_uuid varchar unique,
                  first_name varchar,
                  last_name varchar,
                  created_at timestamp default now()
                )
            '''
            cur.execute(sql)
            conn.commit()
            print('Created table expenses')

        conn.close()
    except Exception as e:
    	print('Exception creating table', e)