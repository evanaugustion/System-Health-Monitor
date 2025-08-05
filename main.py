import psutil
import time
import csv
import requests
import platform

SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/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'
def send_slack_alert (cpu):
    message = { 'text': f'High CPU usage detected: {cpu}%'}
    requests.post (SLACK_WEBHOOK_URL, json = message)


with open ('system_log.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Time", "CPU Usage (%)", "Memory Usage (%)", "Disk Usage (%)"])

    while True:
        current_time = time.strftime ("%d-%m-%y %H:%M:%S")

        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        if platform.system() == 'Windows':
            disk_path = 'C:\\'
        else:
            disk_path = '/'
        disk = psutil.disk_usage(disk_path).percent

        if cpu > 80:
            print (f"[{current_time}] WARNING: High CPU Usage: {cpu}%")
            send_slack_alert(cpu)
        else:
            print (f"[{current_time}] CPU: {cpu}, RAM: {memory}, Disk: {disk}")

        writer.writerow ([current_time, cpu, memory, disk])
        file.flush()

        time.sleep(1)