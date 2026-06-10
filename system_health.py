import psutil
def check_system_health():
    print(f"CPU: {psutil.cpu_percent(interval=1)}%, RAM: {psutil.virtual_memory().percent}%")
if __name__ == "__main__":
    check_system_health()
