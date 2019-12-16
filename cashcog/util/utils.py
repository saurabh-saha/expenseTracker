import json
import requests
import time

from cashcog.util import dbutils
from cashcog import model

import traceback

def processPendingTrans():
    while True:
        try:
            conn = dbutils.createConnection()
            cur = conn.cursor()
            cur.execute("select id,data,created_at from all_transactions where read = 'f' limit 1000")
            rows = cur.fetchall()

            expenses = []
            users = []
            transactionsIds = []
            for tid,data,created_at in rows:
                exp,user = model.getMessage(data)
                expenses.append(exp)
                users.append(user)
                transactionsIds.append(tid)

            print('Fetched', len(expenses), len(users))

            try:
                sql = 'insert into expenses(uuid, description, created_at, amount, currency) values '
                sql += ','.join(cur.mogrify("(%s,%s,%s,%s,%s)", x).decode('utf-8') for x in expenses)
                sql += ' on conflict do nothing'
                cur.execute(sql)
                conn.commit()
            except Exception as e:
                print('Error saving expense',e, traceback.format_exc())

            try:
                sql = 'insert into users(uuid, emp_uuid, first_name, last_name) values '
                sql += ','.join(cur.mogrify("(%s,%s,%s,%s)", x).decode('utf-8') for x in users)
                sql += ' on conflict do nothing'
                cur.execute(sql)
                conn.commit()
            except Exception as e:
                print('Error saving user',e, traceback.format_exc())

            try:
                sql = "update all_transactions set read = 't' where id in "
                sql += "(" + ','.join([str(x) for x in transactionsIds]) + ")"
                cur.execute(sql)
                conn.commit()
            except Exception as e:
                print('Error updating all_transactions',e, traceback.format_exc())

            cur.close()
            conn.close()

        except Exception as e:
                print("exception while parsing transactions", e, traceback.format_exc())

        time.sleep(10)

def save(line):
    decoded_line = line.decode('utf-8')
    try:
        conn = dbutils.createConnection()
        cur = conn.cursor()
        sql = '''
            insert into all_transactions(data) values('{}')
        '''.format(decoded_line)
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print('failed saved stream', e)

def stream_listener(url):
    count = 0
    while True:
        print(count)
        try:
            resp = requests.get(url, stream = True)
            if resp.status_code == 200:
                for line in resp.iter_lines():
                    if line:
                        save(line)
                    else :
                        print("Unhandled status `{}` retreived, exiting.".format(resp.status_code))
                        continue
        except requests.exceptions.Timeout as e:
            print('timeout errors - reconnect',e)
            continue
        except requests.exceptions.RequestException as e:
            print("Request exception {} exiting".format(e))
            continue
        count += 1

def convertTableFormat(columns, rows):
    table = []
    for row in rows:
        tableRow = {}
        for c, r in zip(columns, row):
            tableRow[c] = r
        table.append(tableRow)
    return table