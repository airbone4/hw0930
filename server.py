from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # 由 static 資料夾提供 Iindex.html
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)