import psycopg2

def createConnection():
    conn = None
    try:
        conn = psycopg2.connect(
            dbname="neondb",
            user="neondb_owner",
            password="npg_EWe1w3JUxfhF",
            host="ep-black-water-a1sk805z-pooler.ap-southeast-1.aws.neon.tech",
            sslmode="require"
        )
        # print("Connection to the database was successful!")
        return conn
    except Exception as e:
        print("Could not connect to the database:", e)

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
                  uuid varchar,
                  description varchar,
                  created_at timestamp,
                  amount int,
                  currency varchar,
                  status varchar,
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
                  uuid varchar,
                  emp_uuid varchar,
                  first_name varchar,
                  last_name varchar,
                  created_at timestamp default now()
                )
            '''
            cur.execute(sql)
            conn.commit()
            print('Created table expenses')

        conn.close()

        return True
    except Exception as e:
    	print('Exception creating table', e)