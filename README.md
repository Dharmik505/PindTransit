# PindTransit - Rural Bus Tracking System

**Low-cost real-time bus tracking system for Tier-2 & Tier-3 Indian cities**

## Overview
PindTransit is an MVP (Minimum Viable Product) web-based bus tracking solution designed for small towns and rural areas in India. It provides real-time bus location tracking, route planning, and SMS fallback for users without smartphones.

## Features
- ✅ Real-time GPS bus tracking
- ✅ Route planning with OpenStreetMap
- ✅ SMS fallback for low connectivity areas
- ✅ Driver app for location broadcasting
- ✅ Passenger portal for bus discovery
- ✅ ETA (Estimated Time of Arrival) calculation
- ✅ Mobile-responsive UI
- ✅ Low-cost implementation (<$50/month)

## Tech Stack
- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Maps**: OpenStreetMap, Leaflet.js
- **Database**: SQLite (dev), PostgreSQL (production)
- **Hosting**: AWS EC2 / Heroku / Digital Ocean

## Project Structure
```
PindTransit/
├── app.py                          # Flask application
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment variables template
├── templates/
│   ├── index.html                 # Landing page
│   ├── driver_dashboard.html       # Driver interface
│   └── passenger_portal.html       # Passenger interface
├── static/
│   ├── css/
│   │   └── style.css             # Styling
│   └── js/
│       └── app.js                # Frontend logic
├── README.md                       # This file
└── .gitignore                      # Git ignore rules
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/Dharmik505/PindTransit.git
cd PindTransit
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Environment Variables
```bash
cp .env.example .env
# Edit .env with your configuration
```

### Step 5: Run the Application
```bash
python app.py
```
Access the app at `http://localhost:5000`

## API Endpoints

### Driver APIs
- `POST /api/register-driver` - Register new driver
- `POST /api/update-location` - Update bus location
- `GET /api/get-route/<bus_id>` - Get bus route

### Passenger APIs
- `GET /api/get-all-buses` - Get all active buses
- `GET /api/get-bus-location/<bus_id>` - Get specific bus location
- `POST /api/get-eta` - Get estimated arrival time
- `POST /api/send-sms` - SMS notification fallback

## Usage

### For Drivers
1. Visit `http://localhost:5000/driver`
2. Enter Driver ID and Bus Number
3. Click "Start Tracking" to begin broadcasting location
4. Location updates automatically every 30 seconds

### For Passengers
1. Visit `http://localhost:5000/passenger`
2. Select desired route
3. View real-time bus location on map
4. See ETA for bus arrival
5. Option to receive SMS updates

## Configuration

Edit `.env` file to configure:
```
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your-secret-key
SMS_API_KEY=your-sms-provider-key
MAP_API_KEY=your-openstreetmap-key
```

## Deployment

### Heroku Deployment
```bash
heroku login
heroku create pindtransit-app
git push heroku main
heroku config:set FLASK_ENV=production
```

### AWS EC2 Deployment
1. Launch EC2 instance (Ubuntu 20.04)
2. Install Python and dependencies
3. Clone repository and run with Gunicorn
4. Use Nginx as reverse proxy

## Cost Breakdown (Monthly)
- Server hosting: $5-15 (EC2 micro or Digital Ocean)
- SMS API: $10-20 (Twilio/AWS SNS)
- Domain: $1-3
- **Total: ~$20-40/month**

## Future Enhancements
- Mobile app (React Native)
- Advanced analytics dashboard
- Payment integration
- Driver rating system
- Historical tracking data
- Multiple city support
- AI-based delay prediction

## Contributing
Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License
MIT License - See LICENSE file

## Support
For issues or questions, create an issue on GitHub.

## Team
- Developed by: [Your Name]
- Last Updated: January 2026

---

**Made with ❤️ for India's Transportation**
