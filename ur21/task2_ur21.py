import unittest
from task1_ur21 import CustomOpen

class TestCustomOpen(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_file.txt"
        self.nonexistent_file = "nonexistent_file.txt"
        self.sample_content = "Hello, World!"

    def test_file_creation_and_write(self): # Verify the file exists and contains the correct content
        with CustomOpen(self.test_file, "w") as f:
            f.write(self.sample_content)
        with open(self.test_file, "r") as f:
            self.assertEqual(f.read(), self.sample_content)

    def test_file_reading(self): # Test that the context manager reads a file successfully
        with open(self.test_file, "w") as f:
            f.write(self.sample_content)
        with CustomOpen(self.test_file, "r") as f:
            self.assertEqual(f.read(), self.sample_content)

    def test_open_files_counter(self): # Test that the open files counter behaves as expected
        self.assertEqual(CustomOpen.counter, 0)
        with CustomOpen(self.test_file, "w"):
            self.assertEqual(CustomOpen.counter, 1)
        self.assertEqual(CustomOpen.counter, 0)

    def test_logging_behavior(self):
        with CustomOpen(self.test_file, "w") as f:
            f.write(self.sample_content)
        with open(self.test_file, "r") as f:
            self.assertEqual(f.read(), self.sample_content)

    def test_printing_context_managers(self):
        with CustomOpen(self.test_file, "w") as f1, CustomOpen("another_test_file.txt", "w") as f2:
            f1.write("File 1 content")
            f2.write("File 2 content")

        # Verify both files were written correctly
        with open(self.test_file, "r") as f1:
            self.assertEqual(f1.read(), "File 1 content")
        with open("another_test_file.txt", "r") as f2:
            self.assertEqual(f2.read(), "File 2 content")


if __name__ == "__main__":
    unittest.main()
