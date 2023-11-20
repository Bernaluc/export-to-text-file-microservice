from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'Hello World!'


@app.route('/extract_ids', methods=['POST'])
def extract_ids():
    try:
        data = request.get_json()
        if 'store' in data:
            store_data = data['store']

            page_ids = []
            shape_ids = []d

            # Iterate through the keys in store_data
            for key, value in store_data.items():
                if key == 'page:page':
                    page_ids.append(value['id'])
                elif 'shape:' in key:
                    shape_ids.append(key)

            result = {
                'page_ids': page_ids,
                'shape_ids': shape_ids
            }

            return jsonify(result), 200
        else:
            return jsonify({'error': 'Invalid JSON format'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
