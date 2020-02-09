import logging
from flask import Flask,request,jsonify
from flask_cors import CORS
from Host import Host

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

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

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=8080)
