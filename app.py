from flask import Flask, render_template, request, jsonify
import morsecode_core

app = Flask(__name__)

# Root page.
@app.route('/')
def index():
    return render_template('index.html')

# Handle the post request to convert the provided message to cipher.
@app.route('/encrypt/', methods=['POST'])
def encrypt():
    # Return the error if the message is not provided in the request.
    if 'message' not in request.form:
        return (jsonify({
            'status' : 'error',
            'message': 'Message is not provided.'
        }), 400)
    
    try:
        # Covert the message and return the cipher with success status code.
        message = request.form['message']
        return (jsonify({
            'status' : 'success',
            'cipher': morsecode_core.encrypt(message.strip())
        }), 200)
    except: 
        # In case of exception, throw the internal error status code.
        return (jsonify({
            'status' : 'error',
            'message': 'Unknown exception occured.'
        }), 500)

# Handle the post request to convert the provided cipher to message.
@app.route('/decrypt/', methods=['POST'])
def decrypt():
    # Return the error if the cipher is not provided in the request.
    if 'cipher' not in request.form:
        return (jsonify({
            'status' : 'error',
            'message': 'Cipher is not provided.'
        }), 400)
    
    try:
        # Covert the cipher and return the text with success status code.
        cipher = request.form['cipher']
        return (jsonify({
            'status' : 'success',
            'message': morsecode_core.decrypt(cipher.strip())
        }), 200)
    except: 
        # In case of exception, throw the internal error status code.
        return (jsonify({
            'status' : 'error',
            'message': 'Unknown exception occured.'
        }), 500)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
