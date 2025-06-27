import schedule
import time
from report_generator import generate_report
from email_sender import send_email

def daily_task():
    print("Running daily task...")
    report_file = generate_report() 
    send_email(report_file)          

schedule.every().day.at("08:00").do(daily_task)

while True:
    schedule.run_pending()
    time.sleep(60)