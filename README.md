How to get started ?

a) You just need a working postgres server. This server currently connects to postgres on 127.0.0.1:5432//xcnt (xcnt is the database name)

b) Once you have the postgres server running, go inside the main folder and run this command to start the server.    
python3 manage.py runserver

c) then you can get started with 127.0.0.1/home

d) as soon as the django server starts, it uses the file inside service folder to connect to a stream url and starts pushing that data into your postgres server.

e) to fetch new data just reload the page and the table is filled with all the data fetched from the stream.

The frontend is optimised for mobile and desktop so the user can perform the following tasks 

1) search for any field passed in the table. 

   If you have queries to search two or three fields in the same row the use the search bar and separate different keys using space

2) update status as Yes/No realtime and the user is alerted of the changes.

3) Mobile friendly page

4) Description and User Name details is found on expanding each row.
