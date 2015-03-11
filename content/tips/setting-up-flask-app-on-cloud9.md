Title: Setting up flask app on Cloud9
Date: 2014-04-09 11:18
Author: dai
Category: Tips
Tags: cloud9, flask, python
Slug: setting-up-flask-app-on-cloud9

` import os from flask import Flask app = Flask(name) @app.route('/') def hello():  return 'Hello World' app.run(host=os.environ['IP'],port=int(os.environ['PORT']))`
