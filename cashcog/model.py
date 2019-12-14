from cashcog import utils
import json

def getMessage(body):
	body = json.loads(body)
	uuid = body['uuid']
	description = body.get('description')
	createdAt = body.get('created_at')
	amount = int(body.get('amount'))
	currency = body.get('currency')
	employee = getUser(body.get('employee'),uuid)
	return (uuid, description, createdAt, amount, currency),employee

def getUser(employee,uuid):
	empUuid = employee.get('uuid')
	firstName = employee.get('first_name')
	lastName = employee.get('last_name')
	return (uuid,empUuid, firstName, lastName)
