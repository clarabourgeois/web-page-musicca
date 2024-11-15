# Web Page Musicca Project #
This project is a web application that utilizes SCSS for styling and Python for server-side logic. The build process is automated using a Makefile.

## Prerequisites #
Before building and running the project, ensure that the following tools are installed:

Ruby (to enable SCSS compilation with sass), Python 3 and pip3 (for server-side development), GNU Make (to execute build commands)
## Project Structure #

```bash
web-page-musicca/
├── about.html                 # HTML file for the web page
├── assets/
│   └── stylesheets/
│       └── output.css         # Compiled CSS (generated)
├── requirements.txt           # Python dependencies
├── style.scss                 # SCSS file to compile
├── compile_css.sh             # Bash script for SCSS compilation
├── run_server.py              # Python script to run the server
├── makefile                   # Build tool configuration
└── project-1.0.0.tar.gz       # Packaged archive (created after build)
```

## How to Build, Test, and Run #
### 1. Installing Dependencies #
Run the following command to install all system and Python dependencies.  
This command performs the following steps:  
  Updates system packages  
  Installs Ruby, Python, and pip3  
  Installs the sass gem for SCSS compilation   
  Installs Python packages specified in requirements.txt  

### 2. Compiling SCSS to CSS 
To compile the SCSS file into a CSS file: make css  
This command will generate the CSS file assets/stylesheets/output.css.  

### 3. Running the Server  
To start the HTTP server: make server  
This runs the run_server.py script and launches the server which will run on http://localhost:8000. Open this URL to view the webpage once the command is used.  

### 4. Cleaning Generated Files
To remove the generated CSS file: make clean  
This cleans the project directory by removing output.css.  

### 5. Full Build Process
To execute all necessary steps in one go: make all  

### 6. Displaying the Project Version
To check the current project version: make version  
The current version is defined as 1.0.0 in the Makefile.  

### 7. Packaging the Project
To package the project into a tarball (.tar.gz): make package  
This creates a file named project-1.0.0.tar.gz containing all essential project files.  

### 8. Help
For a summary of available commands, use: make help  
This will display detailed usage information.  

## Metadata
Version: 1.0.0  
Build Tool: GNU Make  

## Build Automation Details
The project uses a Makefile to automate various tasks, including:    
Dependency Management: Installs system dependencies (Ruby, Python) and Python libraries from requirements.txt.   
SCSS Compilation: Compiles the style.scss file into CSS using a Bash script (compile_css.sh).  
Server Management: Runs the server script (run_server.py).  
Project Versioning: Uses a VERSION variable to display and manage project versioning.  
Packaging: Creates a compressed .tar.gz archive containing all project files.  

