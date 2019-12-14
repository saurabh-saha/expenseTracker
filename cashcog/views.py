from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse

from cashcog import dbutils, utils

columns = ['expense_id','user_id','uuid','description','currency','amount','first_name','last_name','created_at', 'status']

def render(request):
	template = loader.get_template('main.html')
	return HttpResponse(template.render())

def expense(request):
	params = request.GET
	expenseId = params['expense_id']
	status = params['action']
	response = {}
	success = False
	try:
		conn = dbutils.createConnection()
		cur = conn.cursor()
		cur.execute('''
			update expenses set status = '{}' where id = {}
		'''.format(status, expenseId))
		rowCount = cur.rowcount
		conn.commit()
		conn.close()
		response['message'] = str(rowCount) + ' expense updated'
		success = True
	except Exception as e:
		response['message'] = e
	response['success'] = success
	print(response)
	return JsonResponse(response)

def getAllExpenses(request):
	response = {}
	success = False
	try:
		conn = dbutils.createConnection()
		cur = conn.cursor()
		cur.execute('''
		select e.id as expense_id, u.id as user_id, e.uuid, description, currency, amount, 
		first_name, last_name, e.created_at , status
		from expenses e join users u on e.uuid = u.uuid
		''')
		rows = cur.fetchall()
		conn.close()
		response['expenses'] = utils.convertTableFormat(columns, rows)
		success = True
	except Exception as e:
		response['message'] = e
	response['success'] = success
	return JsonResponse(response)
