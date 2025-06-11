from flask import Flask, send_from_directory
import os

# Compute absolute path to frontend folder
frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../frontend'))

app = Flask(__name__, static_folder=frontend_path, static_url_path='')

# Serve index.html on /
@app.route('/')
def root():
    return send_from_directory(app.static_folder, 'index.html')

# Serve static assets (CSS, JS)
@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(app.static_folder, path)

# Sample API
@app.route('/api/hello')
def hello():
    return {'message': 'Hello from backend'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
