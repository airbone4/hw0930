from flask import Flask, render_template

staticFolder='./static'
templateFolder='./templates'
app=Flask(__name__,
            static_url_path='', 
            static_folder=staticFolder,
            template_folder=templateFolder)

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
