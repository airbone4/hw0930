- [存取某個子目錄裡面的html](https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask)
[]()
- [簡單講一下html協定](https://sdwh.dev/posts/2023/03/HTTP-Protocol-Guide/)

## 如何建立自己的web server

利用的語言是python

為甚麼是python而不是javascript 因為javascript 受限於security無法存取本地端的硬碟檔案。


- 使用AI寫的程式碼,一樣的敘述,出現不一樣的server.py 裡面用的套件(程式碼 英文module or library)不一樣
  最後必須再指定使用甚麼套件。才產生一樣的程式碼。 
  
1. 我給AI的命令是💖`利用python 和flask 寫一個server`
1. python server.py

  出現錯誤訊息 ModuleNotFoundError: No module named 'flask'
  解決方法: pip install flask

安裝的時候,vscode 建議我不要安裝全局的套件
所以我現在要來建立一個虛擬環境
終端機裡面敲入
```
python -m venv .venv # 其中.venv 是使用者指定的本地端套件安裝根目錄
```
問AI怎樣建立虛擬環境 💖`幫我建立一個python的虛擬環境`按照AI回答的說明
1. 執行 Python: Create Environment 指令，依照畫面指示選擇 venv。
1. 選擇要作為虛擬環境基礎的 Python 直譯器。
1. 建立完成後，建議再執行 Python: Select Interpreter 指令，

但是他沒有提示關掉目前的終端機,再重新開一個終端機.
這時候提示符號變成
```
(.venv) @airbone4  #注意前面的括號,表示目前我們在虛擬環境
```

詢問AI說怎麼安裝flask 💖`幫我安裝flask套件` 出現指令
```
pip install flask
```

解釋`http://127.0.0.1:5000`
- http 指的是 我要在本地端(127.0.0.1)的port 5000使用http 協定

在終端機上敲入指令
```python
python server.py
```

作業
1. 利用python幫我寫一個網頁可以讓使用者選取主機端mp3 並且播放
```
from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)

# MP3 檔案所在資料夾
MP3_FOLDER = 'mp3_files'

@app.route('/')
def index():
    # 取得 mp3 檔案清單
    files = [f for f in os.listdir(MP3_FOLDER) if f.endswith('.mp3')]
    # HTML 模板
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>MP3 播放器</title>
    </head>
    <body>
        <h1>選擇 MP3 播放</h1>
        <ul>
        {% for file in files %}
            <li>
                {{ file }}
                <audio controls>
                    <source src="/mp3/{{ file }}" type="audio/mpeg">
                    您的瀏覽器不支援 audio 標籤。
                </audio>
            </li>
        {% endfor %}
        </ul>
    </body>
    </html>
    '''
    return render_template_string(html, files=files)

@app.route('/mp3/<filename>')
def mp3(filename):
    # 傳送 mp3 檔案
    return send_from_directory(MP3_FOLDER, filename)

if __name__ == '__main__':
    # 確保 mp3 資料夾存在
    os.makedirs(MP3_FOLDER, exist_ok=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
```    