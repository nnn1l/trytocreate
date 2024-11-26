class CustomOpen:
    counter = 0  #  for tracking the number of opened files

    def __init__(self, file, mode='r', encoding=None):
        self.file = file
        self.mode = mode
        self.encoding = encoding
        self.file_object = None

    def __enter__(self):
        self.file_object = open(self.file, self.mode, encoding=self.encoding)
        CustomOpen.counter += 1
        self.log(f"Opened file: {self.file} in mode: {self.mode}. Total open count: {CustomOpen.counter}")
        return self.file_object

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file_object:
            self.file_object.close()
            CustomOpen.counter -= 1
            self.log(f"Closed file: {self.file}. Total open count: {CustomOpen.counter}")

        if exc_type is not None:
            self.log(f"Exception occurred: {exc_type} - {exc_value}")
            return False
        return True

    @staticmethod
    def log(message):
        print(f"[CustomOpen LOG] {message}")


with CustomOpen("example.txt", "w") as f:
    f.write("Hello, World!")


print(f"Open files counter: {CustomOpen.counter}")
