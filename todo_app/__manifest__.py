{
'name': 'To-Do App',
'description': 'Manage To-Do tasks.',
'author': 'Rolando',
'depends': ['base'],
'data': [
	'security/ir.model.access.csv',
	'security/todo_access_rules.xml',
	'views/todo_view.xml',
	'views/todo_menu.xml',
],
'application': True,
}
