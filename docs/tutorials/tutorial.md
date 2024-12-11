Web Page Musicca - Tutorial
Introduction
Welcome to the Web Page Musicca tutorial! This guide will help you get started with building, testing, and running the web application. The application utilizes SCSS for styling, Python for server-side logic, and uses a Makefile to automate common tasks.

Prerequisites
Before starting, ensure the following tools are installed:

Ruby: Required to enable SCSS compilation using sass.
Python 3 and pip3: Needed for running the server and testing the application.
GNU Make: Automates the build and deployment processes.
To install these dependencies on your system:

Installing Dependencies
System Dependencies: Run the following commands to update your system and install the necessary tools:

bash
Copier le code
sudo apt update
sudo apt install -y ruby-full python3 python3-pip
sudo gem install sass
Python Dependencies: Install Python dependencies from requirements.txt:

bash
Copier le code
pip3 install -r requirements.txt

Steps to Build, Test, and Run the Project
1. Compiling SCSS to CSS
Run the following command to compile the SCSS into CSS:

bash
Copier le code
make css
This will generate the assets/stylesheets/output.css file.

2. Running the Server
To start the HTTP server, use the following command:

bash
Copier le code
make server
This will launch the server, which can be accessed at http://localhost:8000.

3. Cleaning Generated Files
To clean up generated files, like output.css, use:

bash
Copier le code
make clean
4. Full Build Process
You can execute all the steps in one go using the make all command:

bash
Copier le code
make all
5. Displaying the Project Version
To display the current version of the project, use:

bash
Copier le code
make version
6. Packaging the Project
To package the project into a .tar.gz archive, use:

bash
Copier le code
make package
This will create a project-1.0.0.tar.gz archive with all the necessary files.

7. Static Analysis
This project uses pylint and htmlhint for static code analysis. To install them, use:

bash
Copier le code
pip install pylint
npm install -g htmlhint
pip install pre-commit
pre-commit install
Once set up, every commit will automatically trigger static analysis for Python and HTML files.

8. Unit Testing
You can run unit tests for the server and SCSS compilation scripts:

bash
Copier le code
python3 -m unittest tests/test_run_server.py
python3 -m unittest tests/test_compile_css.py

Conclusion
You’ve successfully set up and learned how to run the Web Page Musicca project. For more information, check the project documentation or ask for help via GitHub issues.
