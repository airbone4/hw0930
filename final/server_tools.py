import os
import md_to_html


def generate_index():

    mdfiles=[f for f in os.listdir('.') if f.endswith('.md') and f != 'index.md' ]
    for md in mdfiles:
        htmlfile=os.path.splitext(md)[0]+'.html'
        md_to_html.convert(md, os.path.join('static', htmlfile))

    # List all files in current directory and filter for .html files
    # Exclude 'index.html' itself from the list
    files = [f for f in os.listdir('./static') if f.endswith('.html') and f != 'index.html']
    
    # Sort files alphabetically
    files.sort()

    # Define HTML template
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>File Index</title>
    </head>
    <body>
        <h1>Directory Index</h1>
        <ul>
            {''.join(f'<li><a href="{f}">{f}</a></li>' for f in files)}
        </ul>
    </body>
    </html>
    """

    # Write the content to index.html
    with open(os.path.join('static','index.html'), 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Successfully indexed {len(files)} HTML files.")
