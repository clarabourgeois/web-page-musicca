# Module docstring
"""
Test the functionality of the SCSS compilation process using the script 'compile_css.sh'.
The test verifies if the output CSS file is generated after the compilation process.
"""

import unittest
import subprocess
import os
import time
import threading

class TestSCSSCompile(unittest.TestCase):
    """
    Test class for SCSS compilation using the 'compile_css.sh' script.
    It checks if the SCSS file is correctly compiled into CSS and if the output file is generated.
    """

    def setUp(self):
        """Set up the SCSS compile process in a separate thread."""
        self.port = 8081  # Port number for your server (if needed)
        self.sass_process = None
        self.output_css_path = 'assets/stylesheets/output.css'

    def start_scss_compile(self):
        """Start the SCSS compilation process in a separate thread."""
        # Start the SCSS compilation script
        self.sass_process = subprocess.Popen(
            ['bash', 'compile_css.sh'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

    def stop_scss_compile(self):
        """Stop the SCSS compile process after test."""
        if self.sass_process:
            self.sass_process.terminate()  # Terminate the process after the test
            self.sass_process.wait(timeout=5)  # Wait for process termination
            # Close the stdout and stderr streams
            self.sass_process.stdout.close()
            self.sass_process.stderr.close()

    def test_scss_compile(self):
        """Test if SCSS compiles into CSS and the output file is generated."""
        # Start the SCSS compile in a separate thread
        compile_thread = threading.Thread(target=self.start_scss_compile)
        compile_thread.start()

        # Give the process a moment to start
        time.sleep(2)

        try:
            # Check if the output CSS file is created after compilation starts
            self.assertTrue(os.path.exists(self.output_css_path), "Output CSS file not generated.")
        finally:
            # Stop the SCSS compile process
            self.stop_scss_compile()

            # Wait for the compile thread to complete
            compile_thread.join()

if __name__ == '__main__':
    unittest.main()
