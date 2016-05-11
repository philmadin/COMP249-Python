'''

@author: Steve Cassidy
'''

from bottle import Bottle, template, static_file, request, debug, redirect
import interface
import users
from database import COMP249Db


COOKIE_NAME = 'sessionid'

application = Bottle()
debug()

@application.route('/static/<filename:path>')
def static(filename):
    """Serve static files from the 'static' directory"""
    return static_file(filename=filename, root='static')


@application.route('/about')
def about():
    """generate the about page"""

    return template('about', title="About FlowTow")

@application.route('/')
def index():
    """Main page of the application"""

    db = COMP249Db()

    info = {}

    info['user'] = users.session_user(db)
    info['title'] = "¡Welcome to FlowTow!"
    info['images'] = interface.list_images(db, 3)

    return template('index', info)


@application.post('/like')
def like():
    """Add a like to an existing image"""

    # get filename info from the submitted form
    filename = request.forms.get('filename')

    db = COMP249Db()
    interface.add_like(db, filename, None)

    redirect('/')





if __name__ == '__main__':
    debug()
    application.run()
