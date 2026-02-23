from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        API_KEY = "62ce744befbe8b7bb6ef9a5bf3d6b099"
        
        # We use http (no 's') to avoid handshake blocks in some regions
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        
        # We pretend to be a real web browser (Chrome)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        try:
            # Increased timeout to 15 seconds
            response = requests.get(url, headers=headers, timeout=15)
            
            print(f"DEBUG: Status {response.status_code}") # Watch your terminal for this!
            
            if response.status_code == 200:
                weather_data = response.json()
            elif response.status_code == 401:
                weather_data = {"error": "API Key not active yet. Wait 1-2 hours."}
            else:
                weather_data = {"error": f"City not found (Error {response.status_code})"}
                
        except Exception as e:
            print(f"Error details: {e}")
            weather_data = {"error": "Connection refused. Try turning on a VPN if available."}

    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
    
