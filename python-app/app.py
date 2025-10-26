#!/usr/bin/env python3
from flask import Flask
import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    env = os.environ.get('ENVIRONMENT', 'development')
    return f'''
    <h1>🐍 Python Flask App in Docker</h1>
    <p>Environment: {env}</p>
    <p>Current time: {datetime.datetime.now()}</p>
    <p>This app is running in a Docker container!</p>
    '''

@app.route('/health')
def health():
    return {
        'status': 'healthy', 
        'timestamp': datetime.datetime.now().isoformat(),
        'environment': os.environ.get('ENVIRONMENT', 'development')
    }

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)