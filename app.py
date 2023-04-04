import os,json
from bson import json_util
from flask import Flask,request
import modules.user.User as user
import modules.products.Products as products
from threading import Thread
import jobs.Jobs as jobs
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

# scheduler_thread = Thread(target=Jobs.job)
# scheduler_thread.start()

@app.route('/adduser', methods=['POST'])
def addUser():
    return json.loads(json_util.dumps(user.addUser(request.args)))

@app.route('/deleteuser', methods=['DELETE'])
def deletUser():
    return json.loads(json_util.dumps(user.deleteUser(request.args)))

@app.route('/updateuser', methods=['PUT'])
def updateUser():
    return json.loads(json_util.dumps(user.updateUser(request.args)))

@app.route('/getuser', methods=['GET'])
def getUser():
    return json.loads(json_util.dumps(user.getUser(request.args)))

@app.route('/getallusers', methods=['GET'])
def getAllUsers():
    return json.loads(json_util.dumps(user.getAllUsers(request.args)))

@app.route('/addproduct', methods=['POST'])
def addProduct():
    return json.loads(json_util.dumps(products.addProduct(request.args)))

@app.route('/deleteproduct', methods=['DELETE'])
def deleteProduct():
    return json.loads(json_util.dumps(products.deleteProduct(request.args)))

@app.route('/updateproduct', methods=['PUT'])
def updateProduct():
    return json.loads(json_util.dumps(products.updateProduct(request.args)))

@app.route('/deleteallproducts', methods=['DELETE'])
def deleteAllProducts():
    return json.loads(json_util.dumps(products.deleteAllProducts(request.args)))

@app.route('/check', methods=['GET'])
def check():
    return json.loads(json_util.dumps(jobs.check(request.args)))


if __name__== "__main__":
    app.run(debug=True,port=int(os.environ.get('PORT',8000)))