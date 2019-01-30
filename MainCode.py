from flask import Flask, render_template,request,redirect, url_for,send_from_directory
#from metric_concept import QueryService
from metric_concept_area_summary import QueryService
from flask_restful import Api, Resource, reqparse

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'Landmark' or request.form['password'] != '123':
            error = 'Invalid Credentials. Please try again.'
        else:
            
            return render_template("colorindex2.html")
            #return render_template("ios.html")  ###for chat
    return render_template('login.html', error=error)


#app = Flask(__name__)
api = Api(app)
api.add_resource(QueryService, '/lm_query')


@app.route("/favicon.ico")
def favicon():
    from os import path
    return send_from_directory(path.join(app.root_path, "static"), "favicon.ico", mimetype = "image/vnd.microsoft.icon")
    return None


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host="0.0.0.0",port=443,debug=True,ssl_context=('cert.pem', 'key.pem'))
