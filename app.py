from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

API_KEY = 'your_api_key'
BASE_URL = 'https://catalogopmb.catastrobogota.gov.co/PMBWeb/web/api'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/geocode', methods=['GET'])
def geocode():
    address = request.args.get('address')
    if not address:
        return jsonify({'error': 'Address is required'}), 400

    params = {
        'cmd': 'geocodificar',
        'apikey': API_KEY,
        'query': address
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200 and data['status']:
        return jsonify(data['response']['data'])
    else:
        return jsonify({'error': data['response']['message']}), response.status_code

@app.route('/reverse_geocode', methods=['GET'])
def reverse_geocode():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    
    if not latitude or not longitude:
        return jsonify({'error': 'Latitude and Longitude are required'}), 400

    params = {
        'cmd': 'geocodificar_inverso',
        'apikey': API_KEY,
        'LATITUD': latitude,
        'LONGITUD': longitude
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200 and data['status']:
        return jsonify(data['response']['data'])
    else:
        return jsonify({'error': data['response']['message']}), response.status_code

@app.route('/route', methods=['GET'])
def route():
    start = request.args.get('start')
    end = request.args.get('end')
    vehicle = request.args.get('vehicle', 'car')

    if not start or not end:
        return jsonify({'error': 'Start and end points are required'}), 400

    params = {
        'type': 'json',
        'locale': 'es',
        'points_encoded': 'false',
        'elevation': 'true',
        'ch.disable': 'true',
        'algorithm': 'alternative_route',
        'alternative_route.max_paths': 3,
        'vehicle': vehicle,
        'point': [start, end]
    }

    response = requests.get(f'{BASE_URL}/route', params=params)
    data = response.json()

    if response.status_code == 200:
        return jsonify(data)
    else:
        return jsonify({'error': 'Failed to calculate route'}), response.status_code

@app.route('/search_chip', methods=['GET'])
def search_chip():
    chip = request.args.get('chip')
    if not chip:
        return jsonify({'error': 'CHIP code is required'}), 400

    params = {
        'cmd': 'direccion_chip',
        'spatialReference': 102100,
        'query': chip
    }

    response = requests.get(f'{BASE_URL}/buscar', params=params)
    data = response.json()

    if response.status_code == 200:
        return jsonify(data)
    else:
        return jsonify({'error': 'Failed to search CHIP'}), response.status_code

@app.route('/search_place', methods=['GET'])
def search_place():
    query = request.args.get('q')
    if not query:
        return jsonify({'error': 'Search query is required'}), 400

    params = {
        'q': query,
        'boundingBox': request.args.get('boundingBox'),
        'distance': request.args.get('distance'),
        'lat': request.args.get('lat'),
        'lng': request.args.get('lng'),
        'page': request.args.get('page', 1),
        'size': request.args.get('size', 10)
    }

    response = requests.get(f'{BASE_URL}/buscar2', params=params)
    data = response.json()

    if response.status_code == 200:
        return jsonify(data)
    else:
        return jsonify({'error': 'Failed to search place'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)