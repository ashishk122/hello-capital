from flask import jsonify, Flask, request
from functools import wraps
from flask import jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from support_methods import CONTROLLER #storeData, deletedata, editdata, searchdata
import logging

#logger = getLogger("server_flask.log")
 
APPS = Blueprint('read_authentication', __name__)
CONT = CONTROLLER()
def check_auth(username, password):
    return username == 'capital' and password == 'ashish@123'

def authenticate():
    response = jsonify({"status": False, "msg":"authentication failed"})
    response.status_code = 401
    return response

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@APPS.route('/capital/v1/createrecord', methods=["PUT"])
@requires_auth
def createphone():
    #logger.info("hello")
    if request.method == "PUT":
        data = request.get_json(force=True)
        print data
        res = CONT.storeData(data)
        if res:
            response = jsonify({"status": "success", "message": "successfull create"})
            response.status_code = 200
            return response
        else:
            response = jsonify({"status": "failure", "message": "already present"})
            response.status_code = 409
            return response

    else:
        response = jsonify({"status": False, "message": "method type error"})
        response.status_code = 405
        return response

@APPS.route('/capital/v1/deleterecord', methods=["DELETE"])
@requires_auth
def deletecontact():
    data = request.get_json(force=True)
    res = CONT.deletedata(data['email'])
    if res:
        response = jsonify({"status": "success", "message": "successfull deleted"})
        response.status_code = 200
        return response
    else:
        response = jsonify({"status": "failure", "message": "not found"})
        response.status_code = 404
        return response


@APPS.route('/capital/v1/editrecord', methods=["POST"])
@requires_auth
def editcontact():
    data = request.get_json(force=True)
    res = CONT.editdata(data)
    if res:
        response = jsonify({"status": "success", "message": "successfull updated"})
        response.status_code = 200
        return response
    else:
        response = jsonify({"status": "failure", "message": "not found"})
        response.status_code = 404
        return response


@APPS.route('/capital/v1/fetchdata', methods=["GET"])
@requires_auth
def fetchdata():
    email = request.args.get('email')
    data = CONT.searchdata(email) 
    if data:
        response = jsonify({"status": "success", "result":data})
        response.status_code = 200
        return response
    else:
        response = jsonify({"status": "failure", "message": "not found"})
        response.status_code = 404
        return response

if __name__ == '__main__':
    APPS.run(host="localhost", port=8000)

