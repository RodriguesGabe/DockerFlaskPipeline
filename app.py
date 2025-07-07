from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Minha Pipeline DevOps Funcionou!"

@app.route('/health')
def health():
    return "Ta funcionando", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
