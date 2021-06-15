from flask import Flask, request, Response
import requests
import json
import os
import time

# global variable to store download directory
downloadDIR = "downloads"


# appending epoch time to fileName to make it unqiue and won't replace the existing files
def prepareFileName(fileName):
    return str(time.time())+"_"+fileName

# function creates the downloadDIR if not exists
def handleDownloadDirectory():
    if not os.path.exists(downloadDIR):
        os.makedirs(downloadDIR)

# main app hanlder
def mainapp():
    app = Flask("mainapp")
    app.secret_key = 'xlaksfjoi23iop236'
    # invoking directory handler on server start
    handleDownloadDirectory()

    @app.route('/manage_file', methods=['POST'])
    def handlerequest():
        arg = request.get_json()
        response = {}
        FileURL = "https://www.learningcontainer.com/wp-content/uploads/2020/04/sample-text-file.txt"
        FileName = "downloads"
        # error handler if argument not included in body
        if "action" not in arg:
            response["error"] = "action is required, expected values: read, download"
            return Response(json.dumps(response), status=400, mimetype='application/json')
        # optional feature to fetch data of dynamic file url
        if "url" in arg:
            FileURL = arg["url"]
        if "file_name" in arg:
            FileName = arg["file_name"]
        # condition to handle file download
        if arg["action"] == "download":
            try:
                resp = requests.get(FileURL)
                text = resp.text
                fileName = prepareFileName(FileName)
                filePath = "\\downloads\\"+fileName+".txt"
                with open(os.getcwd()+filePath, 'w') as f:
                    f.write(text)
                    f.close()
                    response["status"] = "success"
                    response["filePath"] = filePath.replace("\\", "/")
                    return Response(json.dumps(response), status=200, mimetype='application/json')

            except Exception as e:
                response["error"] = str(e)
                return Response(json.dumps(response), status=500, mimetype='application/json')
         # condition to handle file download
        elif arg["action"] == "read":
            try:
                resp = requests.get(FileURL)
                text = resp.text
                response["status"] = "success"
                response["text"] = text
                return Response(json.dumps(response), status=200, mimetype='application/json')
            except Exception as e:
                response["error"] = str(e)
                return Response(json.dumps(response), status=500, mimetype='application/json')
        else:
            # condition handles if action key value is invalid
             response["error"] = "Invalid action, expected values: read, download"
             return Response(json.dumps(response), status=400, mimetype='application/json')
    return app


if __name__ == '__main__':
    print("Running Server")
    app = mainapp()
    app.run(host='0.0.0.0', debug=True)
