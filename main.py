from flask import Flask, request, jsonify, render_template
import openai
import config

app = Flask(__name__, static_folder='static', template_folder='templates')

openai.api_key = config.api_key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate-story', methods=['POST'])
def generate_story():
    user_prompt = request.json.get('prompt') if request.json is not None else None
    if user_prompt is not None:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": "You are a creative storyteller."},
                          {"role": "user", "content": user_prompt}]
            )
            story = response.choices[0].message['content'].strip()
            return jsonify({'story': story})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'No prompt provided'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)



