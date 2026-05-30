import psutil
import csv
import os
from datetime import datetime
import time

def get_status():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return ram, cpu, disk

def check_warnings(ram,cpu,disk):
    print (f"RAM Usage: {ram}%")
    print (f"CPU Usage: {cpu}%")
    print (f"Disk Usage: {disk}%")
    
    if ram > 80:
        print (f"WARNING!! RAM is running high: {ram}%")
    if cpu > 80:
        print (f"WARNING!! CPU is running high: {cpu}%")
    if disk > 80:
        print (f"WARNING!! Disk space is running low : {disk}%")

def save_log(ram,cpu,disk):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file = "system_logs.csv"
    file_exists = os.path.exists(log_file)
    with open(log_file, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "ram", "cpu", "disk"])  
        writer.writerow([now, ram, cpu, disk])

print("Monitor started. Press Ctrl+C to stop")

while True:
    ram, cpu, disk = get_status()
    check_warnings(ram, cpu, disk)
    save_log(ram, cpu, disk)
    time.sleep(60)
     
    
