from flask import Flask, request, jsonify, flash, redirect, url_for,Response
import requests
import pytest
import json
import os


def demoapp():
    app = Flask("demoapp")
    app.secret_key = 'xlaksfjoi23iop236'
    @app.route('/manage_file',methods=['GET','POST'])
    def handlerequest():
        arg = request.get_json()
        if arg["action"] == "download":
            print("downloading")
            resp = requests.get("https://www.learningcontainer.com/wp-content/uploads/2020/04/sample-text-file.txt")
            text = resp.text
            print(text)
            with open(os.getcwd()+"\\sample\\sample-text-file.txt",'w') as f:
                f.write(text)
                f.close()
                return "200"
            return 404
        elif arg["action"] == "read":
            print("reading")
            resp = requests.get("https://www.learningcontainer.com/wp-content/uploads/2020/04/sample-text-file.txt")
            text = resp.text
            print(text)
            return Response(text, mimetype='text/plain',)
            #mimetype = 'text/plain'
            #return (text, resp.status_code)
        else : return "Invalid action"
        return "200"
    return app

if __name__ == '__main__':
    print("Running Server")
    app = demoapp()
    app.run()

