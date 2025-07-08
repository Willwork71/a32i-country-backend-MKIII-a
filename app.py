import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/report', methods=['GET'])
def serve_report():
    country = request.args.get('country', '')
    if not country:
        return "Please provide a country parameter in the URL, e.g., /report?country=Uganda", 400

    file_path = f"reports/{country}.md"
    print("== Debug: File path exists:", os.path.exists(file_path))
    print("== Debug: Absolute file path:", os.path.abspath(file_path))

    if not os.path.exists(file_path):
        return f"Report for {country} not found.", 404

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Return raw Markdown content
    return content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
