How to get started ?

a) You just need a working postgres server. This server currently connects to postgres on 127.0.0.1:5432//xcnt (xcnt is the database name)

b) Once you have the postgres server running, go inside the main folder and run this command to start the server.    
python3 manage.py runserver

c) then you can get started with 127.0.0.1/home

d) as soon as the django server starts, it uses the file inside service folder to connect to a stream url and starts pushing that data into your postgres server.

e) to fetch new data just reload the page and the table is filled with all the data fetched from the stream.

The frontend is optimised for mobile and desktop so the user can perform the following tasks 

1) search for any field passed in the table. 

   If you have queries to search two or three fields in the same row the use the search bar and separate different keys using space. ex. pending binny

2) user can easily update the staus of an expense by clicking on Yes/No buttons at the end of each row. This updates the postgres row and the frontend table row. If this action is successfull the user is alerted of the changes on the browser.

3) To check more details about each row expand each row, it displays description and User Name.

### Python Code
1. **Threading Initialization**:
   - The Python snippet starts two threads:
     - One for processing pending transactions (`utils.processPendingTrans`).
     - Another for listening to a data stream (`utils.stream_listener`) from the URL provided.

2. **Database Setup**:
   - `dbutils.createTable()` ensures the required database table is created before any other operations.

---

### Django Template and Frontend Code
1. **Django Static Files**:
   - `{% load static %}` loads static files for Django.
   - CSS (`styles.css`) and JavaScript (`app.js`) files are included via Django's static files system.

2. **HTML Table**:
   - A responsive HTML table is initialized for displaying data dynamically, likely populated by JavaScript.
   - Another static table lists predefined data such as employee details.

3. **JavaScript and DataTables**:
   - `DataTables` is included for advanced table functionalities such as sorting, searching, and pagination.
   - jQuery is used as a dependency for DataTables.
