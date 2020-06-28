from app import create_app
from flask import jsonify


app = create_app()

@app.route('/')
def home():
    return jsonify({
        'status': 'ok'
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)