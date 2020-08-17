# Importing flask module in the project
# An object of Flask class is our WSGI application
from flask import Flask,jsonify
import logging
import git
import os
port = os.environ.get('PORT')
version = os.environ.get('VERSION')
debug = os.environ.get('DEBUG')
# Flask constructor takes the name of current module (__name__) as argument.
app = Flask(__name__)
#Initializing object of logging.logger
applog = logging.getLogger(__name__)
git_repo = git.Repo(search_parent_directories=True)
sha_id = git_repo.head.object.hexsha
#Setting the log level as INFO
applog.setLevel(logging.INFO)

#print(applog.getEffectiveLevel())
logging.basicConfig(filename="myapp.log",format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
service = [
    {
        'service': "{}".format(app.name),
        'version': "{}".format(version),
         'git sha': "{}".format(sha_id)
    },
    {
        'port': "{}".format(port),
        'loglevel': "{}".format(logging.getLevelName(applog.level)
    }
]
@app.route('/',methods=['GET'])
def hello_world():
    app.logger.info('Displaying hello')
    return 'Hello, World!:'

@app.route('/info', methods=['GET'])
def get_myapp_info():
    app.logger.info('Displaying the info logs')
    return jsonify({'service': service},200)

app.run(host='0.0.0.0', port="{}".format(port),debug="{}".format(debug))
