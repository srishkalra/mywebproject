######Author:Srishti Kalra:##########################################################################
##############A simple Webapplication based on flask which has 2 web pages as Home and Info page##########
################Logging is enabled for this APP as INFO level##############################
##################Logs file will be saved in "myapp.log"###################################################

# Importing flask module in the project
# An object of Flask class is our WSGI application
from flask import Flask,jsonify
import logging
import git
import os
#Defining OS ENV variable passed from DocKer file
port = os.environ.get('PORT')
version = os.environ.get('VERSION')
debug = os.environ.get('DEBUG')
# Flask constructor takes the name of current module (__name__) as argument.
app = Flask(__name__)
#Initializing object of logging.logger
applog = logging.getLogger(__name__)
#Capturing the git information from parent directory where it is cloned
git_repo = git.Repo(search_parent_directories=True)
#Evaluating the SHA id.
sha_id = git_repo.head.object.hexsha
#Setting the log level as INFO
applog.setLevel(logging.INFO)
#Using the basicCOnfig function to format and redirect the logs  to file
logging.basicConfig(filename="myapp.log",format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
service = [
    {
        'service': "{}".format(app.name),
        'version': "{}".format(version),
         'git sha': "{}".format(sha_id)
    },
    {
        'port': "{}".format(port),
        'loglevel': f"{logging.getLevelName(applog.level)}"
    }
]
#Defining Home Page 
@app.route('/',methods=['GET'])
def home():
    app.logger.info('Displaying hello')
    return 'Welcome to Web APP!:'
#Definig /info page
@app.route('/info', methods=['GET'])
def get_myapp_info():
    app.logger.info('Displaying the info logs')
    return jsonify({'service': service},200) #Returning Json object
#Running the app with Port Number,debug information defined from OS Environment and Host Ip is set to run any Host where this app is deployed)
app.run(host='0.0.0.0', port="{}".format(port),debug="{}".format(debug))
