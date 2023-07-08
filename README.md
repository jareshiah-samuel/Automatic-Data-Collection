# Automatic-Data-Collection
Designing an Automatic Data Collection and Storage System with AWS Lambda and Slack Integration for Server Availability Monitoring and Slack Notification
Create an AWS Lambda function and configure it to be triggered by an Amazon CloudWatch Event that occurs every 15 seconds.

In the function's code, use the requests library to make a GET request to the API to fetch the data.

Use a library such as pymysql to connect to the Amazon RDS instance and store the data in the database.
for these process you have to pip insatll requests and pymysql and zip the file add them to the layers 


Use Amazon CloudWatch to set up a monitoring alarm that will trigger when the server is unavailable.
for that Use the Slack API to send a message to your Slack community when the alarm is triggered.
for using slack api uhave to create a channel and webhook_url so that you can access slack
for using slack in the oode you have to pip install slack-sdk then import slack 
this how you slack channel looks like 
![Screenshot (16)](https://github.com/jareshiah-samuel/Automatic-Data-Collection/assets/108394157/28a51049-933e-4f0d-95a9-49c196744f6d)

Test the function to ensure that it is able to fetch and store the data correctly the data which is stored in rds using mysql
![Screenshot (15)](https://github.com/jareshiah-samuel/Automatic-Data-Collection/assets/108394157/b079e08e-2669-4acd-bd01-bf28212f0093)

