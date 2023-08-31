from flask import Flask, request, jsonify
import requests
import json
import schedule
import time
import threading
import os

app = Flask(__name__)

# USASpending.gov API base URL
USASPENDING_API_BASE_URL = "https://api.usaspending.gov/api/v2/"

# Your Microsoft Teams webhook URL
TEAMS_WEBHOOK_URL = "https://suncoastuw.webhook.office.com/webhookb2/5b270317-0e4b-4d48-9aff-a00882f78ea1@134ff625-eed0-4678-97ff-9324cee9c346/IncomingWebhook/66f9a182bdb54f38875f7fa66ee01ac8/4076aaa8-063b-4b45-aea9-3e923ebab60c"

# Configuration variable for the USASpending.gov API key
app.config["USASPENDING_API_KEY"] = "1wHjFnDiaU2bdwfIQ2eUC8sbFXHTbi6XdF4Ez4Qc"



@app.route("/")
def index():
    return "USASpending.gov API application"

@app.route("/contracts")
def get_contracts():
    # Get the NAICS code from the request query parameters
    naics_code = request.args.get("naics_code")

    if not naics_code:
        return jsonify({"error": "Missing 'naics_code' parameter"}), 400

    # Retrieve the USASpending.gov API endpoint
    api_endpoint = f"https://api.usaspending.gov/api/v2/awards/"

    contract_names = []
    page = 1
    max_pages = 100  # max number of pages to fetch

    while page <= max_pages:
        try:
            response = requests.get(api_endpoint, params={"limit": 100, "page": page, "api_key": app.config["USASPENDING_API_KEY"], "naics": naics_code})
            response.raise_for_status()
            contracts_data = response.json()
        except requests.exceptions.RequestException as e:
            return jsonify({"error": "Failed to retrieve contract data"}), 500

        # If the results list is empty, stop fetching more pages
        if not contracts_data["results"]:
            break

        # Process the contracts_data to extract relevant contract information
        contract_names.extend([contract["awarding_agency"]["agency_name"] for contract in contracts_data["results"] if contract["naics"]["naics_code"] == naics_code])

        page += 1  # Go to the next page for the next iteration

    return jsonify({"contract_names": contract_names}), 200


@app.route("/notifications", methods=["POST"])
def send_notification():
    # Get the notification data from the request (you can customize this as needed)
    data = request.get_json()

    if not data or "contract_number" not in data:
        return jsonify({"error": "Missing 'contract_number' in request data"}), 400

    try:
        # Customize the notification payload as needed
        notification_payload = {
            "title": "Contract Renewal Notification",
            "message": "A contract attributed to the specified NAICS code is coming up for renewal.",
            "contract_number": data["contract_number"],  # You can include other relevant data
        }

        # Convert the notification payload to JSON format
        notification_payload = json.dumps(notification_payload)

        # Send the notification to Microsoft Teams using the webhook
        response = requests.post(TEAMS_WEBHOOK_URL, data=notification_payload, headers={"Content-Type": "application/json"})
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to send notification"}), 500

    return jsonify({"message": "Notification sent successfully"}), 200

def check_contracts_and_notify():
    naics_code = '541211'
    url_contracts = "https://api.usaspending.gov/api/v2/agency/012/awards/" 
    url_notifications = "https://suncoastuw.webhook.office.com/webhookb2/5b270317-0e4b-4d48-9aff-a00882f78ea1@134ff625-eed0-4678-97ff-9324cee9c346/IncomingWebhook/66f9a182bdb54f38875f7fa66ee01ac8/4076aaa8-063b-4b45-aea9-3e923ebab60c"

    response = requests.get(url_contracts, params={"naics_code": naics_code})
    
    if response.status_code == 200:
        try:
            contract_data = response.json()
        except json.JSONDecodeError:
            print("Failed to parse contracts data")
            return
    else:
        print("Failed to get contracts")
        return

    identified_contracts = []
    for contract in contract_data:
        if 'is_coming_for_renewal' in contract and 'is_new' in contract:
            if contract['is_coming_for_renewal'] or contract['is_new']:
                if 'id' in contract:
                    identified_contracts.append(contract)
                else:
                    print(f"Contract {contract} is missing 'id' field")
        else:
            print(f"Contract {contract} is missing 'is_coming_for_renewal' or 'is_new' field")

    for contract in identified_contracts:
        notification_data = {
            "text": f"Contract {contract['id']} is coming up for renewal or is new.",
        }
        response = requests.post(url_notifications, data=json.dumps(notification_data), headers={"Content-Type": "application/json"})

        if response.status_code != 200:
            print(f"Failed to send notification for contract {contract['id']}")


def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(60)  # Wait for 60 seconds between each check



if __name__ == "__main__":
     # Test API connection
    test_response = requests.get(f"{USASPENDING_API_BASE_URL}/agency/012/awards/")
    if test_response.status_code == 200:
        print("Successfully connected to the USASpending.gov API")
    else:
        print(f"Failed to connect to the USASpending.gov API. Status code: {test_response.status_code}")
    # Send a test message to Microsoft Teams on start-up
    try:
        test_message_payload = json.dumps({"title": "App Start-up", "text": "App has started successfully."})
        response = requests.post(TEAMS_WEBHOOK_URL, data=test_message_payload, headers={"Content-Type": "application/json"})
        response.raise_for_status()
        print("Test message sent to Microsoft Teams successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send test message to Microsoft Teams: {e}")

    # Start the scheduled tasks in a separate thread
    schedule.every().day.at("09:00").do(check_contracts_and_notify)
    schedule_thread = threading.Thread(target=run_schedule)
    schedule_thread.start()

    # Run the Flask app
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Failed to start Flask app: {e}")
        schedule_thread.do_run = False
        schedule_thread.join()

def test_api_connection():
    response = requests.get(f"{USASPENDING_API_BASE_URL}awards/")
    if response.status_code == 200:
        print("Successfully connected to the USASpending.gov API")
    else:
        print(f"Failed to connect to the USASpending.gov API. Status code: {response.status_code}")

# Call the function
test_api_connection()

