import datetime

class Logger:
    def __init__(self):
        self.logs = []

    def log(self, message):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] {message}"
        self.logs.append(log_entry)

    def get_logs(self):
        return self.logs
