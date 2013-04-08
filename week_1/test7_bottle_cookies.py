from pymongo import MongoClient
import bottle

#this is the handler for the default path of the web server

@bottle.route('/')
def index():

	#connect to database 
	connection = MongoClient('localhost',27020)

	db = connection.test1

	#create a collection
	names = db.names

	#create an array with json objects
	json_list = [
		{'name':'Juan','lastname':'Lopez'},
		{'name':'Carlos','lastname':'Gil'},
		{'name':'Juan','lastname':'Mesa'},
		{'name':'Felipe','lastname':'Lopez'},
		{'name':'Andres','lastname':'Toro'}
	]

	page_content = ''

	#show the data
	for name in names.find():
		page_content = page_content+'<li>'+str(name['name'])+' '+str(name['lastname'])+'</li>'

	page_content = '<ul>'+page_content+'</ul>'

	return page_content

# test with other urls
@bottle.route('/holamundo')
def helloworld():
	return "<html><title>Hello world!</title><body>Hola Mundo</body></html>"

@bottle.route('/holamundo2')
def helloworld2():
	return "<html><title>Hello world 2!</title><body>Hola Mundo 2</body></html>"


# handling templates
@bottle.route('/plantilla')
def firstTemplate():
	mythings = ['Edwin','Hola','Como','Estas']
	return bottle.template('views/plantilla1.tpl', {'username':"edwinfmesa",'things':mythings})


# forms in bottle
@bottle.route('/my_name', method='GET')
@bottle.route('/my_name', method='POST')
def myName():
	name = bottle.request.forms.get('name')
	print name
	if (name == None or name==""):
		message = "Error"
	else:
		message = None
	return bottle.template('views/t2_forms.tpl',{'message':message,'name':name})


# setting and getting cookies
@bottle.route('/what_is_your_color')
def whatIsYourColor():
	return bottle.template('views/t3_forms2_wiyc.tpl',{'username':'Edwin Mesa'})

@bottle.post('/what_is_your_color_form')
def whatIsYourColorForm():
	color = bottle.request.forms.get('color')
	print color
	if (color == None or color==""):
		print "Error"
	else:
		print 'good color'
	bottle.response.set_cookie('color',color)
	return bottle.redirect('/show_your_color')

@bottle.route('/show_your_color')
def showYourColor():
	color = bottle.request.get_cookie('color')
	return 'the color is: '+color
bottle.debug(True)
bottle.run(host='localhost',port=8082)
