from flask import Flask, render_template
import server_tools

staticFolder='./static'
templateFolder='./templates'
server_tools.generate_index()
app=Flask(__name__,
            static_url_path='', 
            static_folder=staticFolder,
            template_folder=templateFolder)



@app.route('/')
def hello():
    #return render_template('index.html')
    # 由 static 資料夾提供 Iindex.html
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
