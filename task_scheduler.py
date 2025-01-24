import time
import threading
from utils.logger import Logger

class TaskScheduler:
    def __init__(self):
        self.tasks = []
        self.logger = Logger()

    def schedule_task(self, task_name, interval):
        task = threading.Thread(target=self.run_task, args=(task_name, interval), daemon=True)
        self.tasks.append(task)
        task.start()

    def run_task(self, task_name, interval):
        while True:
            self.logger.log(f"Executing task: {task_name}")
            time.sleep(interval)

    def get_logs(self):
        return self.logger.get_logs()
