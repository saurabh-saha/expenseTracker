How to get started ?

Use: python 3, install requirements.txt
Start Server: python manage.py runserver
Navigate to home: 127.0.0.1:8000/home

The frontend is optimised for mobile and desktop so the user can perform the following tasks 
1) search for any field passed in the table.
   If you have queries to search two or three fields in the same row the use the search bar and separate different keys using space. ex. pending binny
2) user can easily update the staus of an expense by clicking on Yes/No buttons at the end of each row. This updates the postgres row and the frontend table row. If this action is successfull the user is alerted of the changes on the browser.
3) To check more details about each row expand each row, it displays description and User Name.
