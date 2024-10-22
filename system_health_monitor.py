import psutil
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='system_health.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Thresholds
CPU_THRESHOLD = 20  # CPU usage percentage
MEMORY_THRESHOLD = 50  # Memory usage percentage
DISK_THRESHOLD = 85 # Disk usage percentage

def check_cpu_usage():
    """Check the CPU usage and log if it exceeds the threshold."""
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        alert_message = f"High CPU Usage: {cpu_usage}%"
        print(alert_message)
        logging.warning(alert_message)

def check_memory_usage():
    """Check the memory usage and log if it exceeds the threshold."""
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        alert_message = f"High Memory Usage: {memory_usage}%"
        print(alert_message)
        logging.warning(alert_message)

def check_disk_usage():
    """Check the disk usage and log if it exceeds the threshold."""
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        alert_message = f"High Disk Usage: {disk_usage}%"
        print(alert_message)
        logging.warning(alert_message)

def check_running_processes():
    """Check for processes using more than 50% CPU and log them."""
    high_cpu_processes = []
    for proc in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent']):
        try:
            cpu_percent = proc.info['cpu_percent']
            if cpu_percent > 50:
                high_cpu_processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    if high_cpu_processes:
        alert_message = f"High CPU Usage by Processes: {high_cpu_processes}"
        print(alert_message)
        logging.warning(alert_message)

def main():
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()

if __name__ == "__main__":
    main()
