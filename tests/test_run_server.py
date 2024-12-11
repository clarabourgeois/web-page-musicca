# Module docstring
"""
Test the functionality of the server and the safeget function in the 'run_server.py' script.
The tests include checking the server's response to GET requests and verifying the behavior
of the safeget function when handling nested dictionaries.
"""

import unittest
import threading
import requests
import run_server


class TestServer(unittest.TestCase):
    """
    Test class for the server and the safeget function.
    It tests the server's GET requests and the functionality of the safeget function
    used to access nested dictionary values safely.
    """

    def setUp(self):
        """Set up a test server in a separate thread."""
        self.port = 8081
        self.server_thread = threading.Thread(
            target=run_server.run,
            kwargs={"port": self.port},
            daemon=True
        )
        self.server_thread.start()

    def tearDown(self):
        """Shut down the test server after each test."""
        # Send a request to shut down the server cleanly
        try:
            requests.post(f"http://localhost:{self.port}", data={}, timeout=5)
        except requests.Timeout:
            self.fail(f"Timeout occurred when shutting down the server on port {self.port}")
        self.server_thread.join(timeout=5)

    def test_get_request(self):
        """Test GET request for a valid path."""
        try:
            response = requests.get(f"http://localhost:{self.port}/", timeout=5)
            self.assertEqual(response.status_code, 200)
            self.assertIn("html", response.headers["Content-Type"])
        except requests.Timeout:
            self.fail("GET request timed out")

    def test_safeget_function(self):
        """Test the safeget function."""
        test_dict = {"key1": {"key2": {"key3": "value"}}}
        result = run_server.safeget(test_dict, "key1", "key2", "key3")
        self.assertEqual(result, "value")
        result = run_server.safeget(test_dict, "key1", "nonexistent")
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
