import json
import requests
import pymysql
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def send_slack_message(webhook_url, message):
    client = WebClient()
    try:
        response = client.chat_postMessage(
            channel="#your-channel",  # Replace with your desired channel name or ID
            text=message
        )
        return response
    except SlackApiError as e:
        print(f"Error sending message to Slack: {e.response['error']}")
        return None

def lambda_handler(event, context):
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        latitude = data["iss_position"]["latitude"]
        longitude = data["iss_position"]["longitude"]
        timestamp = data["timestamp"]
        message = data["message"]

        # Connect to the MySQL database
        conn = pymysql.connect(
            host='mydb.cactwvvrj8cu.ap-south-1.rds.amazonaws.com',
            user='admin',
            password="Appasatti2.0",
            database="mydb"
        )

        try:
            with conn.cursor() as cursor:
                # Insert the data into the MySQL table
                sql = "INSERT INTO mydata (latitude, longitude, timestamp, message) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (latitude, longitude, timestamp, message))
            conn.commit()

            return {
                "statusCode": 200,
                "body": "Data inserted successfully into the MySQL database"
            }
        except Exception as e:
            webhook_url = "https://hooks.slack.com/services/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"
            message = "Error occurred while inserting data into the MySQL database: " + str(e)
            send_slack_message(webhook_url, message)
            
            return {
                "statusCode": 500,
                "body": "Error occurred while inserting data into the MySQL database: " + str(e)
            }
        finally:
            conn.close()
    else:
        webhook_url = "https://hooks.slack.com/services/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"
        message = "Error occurred: " + str(response.status_code)
        send_slack_message(webhook_url, message)
        
        return {
            "statusCode": response.status_code,
            "body": "Error occurred: " + str(response.status_code)
        }
