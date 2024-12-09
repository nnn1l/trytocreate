import datetime

class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.log_error(msg)

    def log_error(self, msg):
        with open('logs.txt', 'a') as file:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write(f"[{timestamp}] ERROR: {msg}\n")

try:
    raise CustomException("Something went wrong!")
except CustomException as e:
    print(f"Caught exception: {e}")