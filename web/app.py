import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify
from domains import get_domain_module
from utils.augment import augment_and_label
from utils.exporter import export_data
import tempfile

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    config = request.json
    domain = config.get('domain')
    output_format = config.get('format', 'csv')
    domain_module = get_domain_module(domain)
    data = domain_module.generate(config)
    data = augment_and_label(data, config)
    with tempfile.NamedTemporaryFile(delete=False, suffix=f'.{output_format}') as tmp:
        export_data(data, tmp.name, config)
        tmp.seek(0)
        content = tmp.read()
    os.unlink(tmp.name)
    return content, 200, {'Content-Type': 'application/octet-stream'}

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
