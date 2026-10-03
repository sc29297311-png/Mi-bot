from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Mi-Bot is Live!"

@app.route('/api', methods=['GET', 'POST'])
def bot():
    data = request.json if request.method == 'POST' else {}
    msg = data.get('message', 'Hello')
    return jsonify({"reply": f"Bot ne bola: {msg} received!"})

# Vercel ke liye
if __name__ == '__main__':
    app.run()
