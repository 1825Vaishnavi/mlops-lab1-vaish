from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to My Cloud Run App! 🚀"

@app.route('/about')
def about():
    return "This app is built by [VAISHNAVI GAJARLA] and deployed on Google Cloud Run!"

@app.route('/health')
def health():
    return "App is running healthy "

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)