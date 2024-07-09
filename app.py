from flask import Flask, render_template, jsonify, request
from main import recognize_and_translate  # import the function from main.py

app = Flask(__name__)

# Global variable to control recording state and selected language
is_recording = False
selected_language = 'hi'  # default language code

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recognize-and-translate', methods=['GET'])
def recognize_and_translate_route():
    global is_recording, selected_language
    if not is_recording:
        return jsonify({'error': 'Recording not started'})
    
    print(f"Selected language code in recognize-and-translate route: {selected_language}")
    result = recognize_and_translate(selected_language)  # Pass the selected language to the function
    return jsonify(result)

@app.route('/start-recording', methods=['POST'])
def start_recording():
    global is_recording
    is_recording = True
    return jsonify({'status': 'Recording started'})

@app.route('/stop-recording', methods=['POST'])
def stop_recording():
    global is_recording
    is_recording = False
    return jsonify({'status': 'Recording stopped'})

@app.route('/select-language', methods=['POST'])
def select_language():
    global selected_language
    data = request.json  # Access JSON data sent from frontend
    selected_language = data['language']  # Access 'language' key from JSON data
    print(f"Selected language code from frontend: {selected_language}")
    return jsonify({'status': 'Language selected'})

if __name__ == '__main__':
    app.run(debug=True)
