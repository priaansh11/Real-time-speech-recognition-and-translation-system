from flask import Flask, render_template, jsonify
from main import recognize_and_translate  # Replace with your module name

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recognize-and-translate')
def recognize_and_translate_endpoint():
    speech_text, translated_text = recognize_and_translate()
    return jsonify({
        'speech_text': speech_text,
        'translated_text': translated_text
    })

if __name__ == '__main__':
    app.run(debug=True)
