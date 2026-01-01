from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
from datetime import datetime
import random
import math

app = Flask(__name__)
CORS(app)

# In-memory storage (replace with database in production)
bus_data = {}
driver_locations = {}
routes = {}
user_data = {}

# Initialize routes
ROUTES_CONFIG = {
    "BUS_001": {"name": "Route 1: Central to Station", "stops": [{"id": "s1", "name": "Central Bus Stand", "lat": 23.1815, "lng": 79.9864}, {"id": "s2", "name": "Railway Station", "lat": 23.1819, "lng": 79.9914}, {"id": "s3", "name": "Market Area", "lat": 23.1825, "lng": 79.9950}]},
    "BUS_002": {"name": "Route 2: Hospital to Market", "stops": [{"id": "h1", "name": "District Hospital", "lat": 23.1855, "lng": 79.9850}, {"id": "h2", "name": "Health Center", "lat": 23.1860, "lng": 79.9880}, {"id": "h3", "name": "Market Plaza", "lat": 23.1870, "lng": 79.9920}]}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/driver')
def driver_dashboard():
    return render_template('driver_dashboard.html')

@app.route('/passenger')
def passenger_portal():
    return render_template('passenger_portal.html')

# API Endpoints
@app.route('/api/register-driver', methods=['POST'])
def register_driver():
    data = request.json
    driver_id = data.get('driver_id')
    user_data[driver_id] = {'name': data.get('name'), 'phone': data.get('phone'), 'role': 'driver'}
    return jsonify({'status': 'success', 'driver_id': driver_id})

@app.route('/api/update-location', methods=['POST'])
def update_location():
    data = request.json
    bus_id = data.get('bus_id')
    driver_locations[bus_id] = {'lat': data.get('lat'), 'lng': data.get('lng'), 'timestamp': datetime.now().isoformat()}
    return jsonify({'status': 'success', 'message': 'Location updated'})

@app.route('/api/get-bus-location/<bus_id>')
def get_bus_location(bus_id):
    if bus_id in driver_locations:
        return jsonify(driver_locations[bus_id])
    return jsonify({'lat': ROUTES_CONFIG[bus_id]['stops'][0]['lat'], 'lng': ROUTES_CONFIG[bus_id]['stops'][0]['lng']})

@app.route('/api/get-route/<bus_id>')
def get_route(bus_id):
    if bus_id in ROUTES_CONFIG:
        return jsonify(ROUTES_CONFIG[bus_id])
    return jsonify({'error': 'Route not found'}), 404

@app.route('/api/get-all-buses')
def get_all_buses():
    buses = []
    for bus_id, route in ROUTES_CONFIG.items():
        location = driver_locations.get(bus_id, {'lat': route['stops'][0]['lat'], 'lng': route['stops'][0]['lng']})
        buses.append({
            'bus_id': bus_id,
            'route_name': route['name'],
            'lat': location['lat'],
            'lng': location['lng'],
            'stops_count': len(route['stops'])
        })
    return jsonify(buses)

@app.route('/api/send-sms', methods=['POST'])
def send_sms():
    data = request.json
    phone = data.get('phone')
    message = data.get('message')
    # SMS fallback simulation
    return jsonify({'status': 'success', 'message': f'SMS sent to {phone}'})

@app.route('/api/get-eta', methods=['POST'])
def get_eta():
    data = request.json
    bus_id = data.get('bus_id')
    stop_id = data.get('stop_id')
    # Simulate ETA calculation (in minutes)
    eta = random.randint(5, 25)
    return jsonify({'eta': eta, 'unit': 'minutes', 'bus_id': bus_id})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
