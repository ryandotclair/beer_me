#!/usr/bin/env python3
from flask import Flask, jsonify, make_response
import os

# Initiate Flask
app = Flask(__name__)

port = int(os.getenv("PORT"))
instance = os.getenv("CF_INSTANCE_ADDR")

@app.route('/api/beer', methods=['GET'])
def get_some():

    print ("Getting someone some beer...")

    payload = {
        "Cost": "Free",
        "Temp": "Cold",
        "Brand": "Who Cares?",
        "Instance": instance
    }
    return jsonify(payload)

@app.errorhandler(404)
@app.errorhandler(405)
def not_found(error_code):
    return make_response(jsonify({'error': 'Not Found'}), str(error_code))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)
