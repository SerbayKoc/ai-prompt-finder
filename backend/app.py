from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/optimize_prompt', methods=['POST'])
def optimize_prompt():
    data = request.get_json()
    prompt = data.get('prompt', '')
    # Optimize prompt logic goes here (placeholder)
    optimized_prompt = prompt + ' - optimized'
    return jsonify({'optimized_prompt': optimized_prompt})

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'running'}), 200

if __name__ == '__main__':
    app.run(debug=True)