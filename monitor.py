import psutil
import time

def monitor_system():
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        
        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory.percent}%")
        print(f"Disk Usage: {disk.percent}%")
        
        if cpu_usage > 80:
            print("Warning: High CPU usage detected!")
        if memory.percent > 80:
            print("Warning: High Memory usage detected!")
        if disk.percent > 80:
            print("Warning: High Disk usage detected!")
        
        time.sleep(5)

if __name__ == "__main__":
    monitor_system()
