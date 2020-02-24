import os
import pathlib
import logging
from flask import Flask,request,jsonify
from flask_cors import CORS
from Host import Host

with open(str(pathlib.Path(__file__).parent.parent.parent.joinpath('Version'))) as f:
    Version = f.read().strip()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.getLogger('werkzeug').setLevel(logging.ERROR)
app = Flask(__name__)
CORS(app)
host = Host()

@app.route("/tpmj", methods=["POST"])
def tpmj():
    try:
        req = request.get_json(force=True,silent=True)
        if req == None: req = {}
        response = host.handle(req)
        return jsonify(response)
    except Exception as e:
        # Log exception raised while handling the request.
        logger.exception('Handling exception.')
        return jsonify({'Processed':0})

@app.route("/about", methods=["GET"])
def about():
    return jsonify({
        'Version':Version,
    })

if __name__ == "__main__":
    isDevelopment = 'TPMJ_BACKEND_PRODUCTION' not in os.environ
    if isDevelopment:
        Version+='*'
    app.run(host='0.0.0.0', debug=isDevelopment, port=8080)
