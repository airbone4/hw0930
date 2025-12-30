import markdown
import os




def convert_md_to_html1(input_file_path, output_file_path):
    """
    Converts a Markdown file to an HTML file using the Python-Markdown library.
    """
    try:
        # Read the Markdown file
        with open(input_file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # Convert Markdown to HTML
        # Using 'extra' extension for tables, footnotes, etc.
        html_content = markdown.markdown(text, extensions=['extra'])
        
        # Write the HTML content to a file
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
            
        print(f"Successfully converted {input_file_path} to {output_file_path}")
        
    except FileNotFoundError:
        print(f"Error: The file {input_file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")





def convert_md_to_html():
    # 設定目標資料夾
    output_dir = 'static'
    
    # 如果資料夾不存在則建立
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"已建立資料夾: {output_dir}")

    # 遍歷目前目錄下的檔案
    for filename in os.listdir('.'):
        if filename.endswith('.md'):
            # 讀取 Markdown 檔案內容
            with open(filename, 'r', encoding='utf-8') as f:
                text = f.read()
            
            # 轉換為 HTML
            # 這裡加入了 'extra' 擴展以支援表格、註腳等語法
            html_content = markdown.markdown(text, extensions=['extra'])
            
            # 設定輸出的 HTML 檔名
            base_name = os.path.splitext(filename)[0]
            
            output_file = os.path.join(output_dir, f"{base_name}.html")
            
            # 寫入 HTML 檔案
            with open(output_file, 'w', encoding='utf-8') as f:
                # 加入基礎的 HTML 結構與 UTF-8 編碼設定，避免亂碼
                f.write(f"<!DOCTYPE html>\n<html>\n<head>\n<meta charset='utf-8'>\n<title>{base_name}</title>\n</head>\n<body>\n")
                f.write(html_content)
                f.write("\n</body>\n</html>")
            
            print(f"已轉換: {filename} -> {output_file}")

     


def generate_index():
    # 設定輸出的檔名
    index_filename = "static/index.html"
    
    # 取得當前目錄下所有的 .html 檔案，並排除 index.html 自己
    html_files = [f for f in os.listdir('./static') if f.endswith('.html') and f != index_filename]
    
    # 排序檔案名稱
    html_files.sort()

    # 定義 HTML 的內容結構
    html_content = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>檔案索引</title>
    <style>
        body {{ font-family: sans-serif; line-height: 1.6; padding: 20px; }}
        ul {{ list-style-type: none; }}
        li {{ margin-bottom: 8px; }}
        a {{ text-decoration: none; color: #0066cc; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <h1>子目錄 HTML 檔案索引</h1>
    <ul>
"""

    # 為每個檔案添加 <li> 連結
    for file in html_files:
        html_content += f'        <li><a href="{file}">{file}</a></li>\n'

    # 封閉 HTML 標籤
    html_content += """    </ul>
</body>
</html>
"""

    # 寫入檔案
    with open(index_filename, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"成功！已生成 {index_filename}，共包含 {len(html_files)} 個連結。")

   