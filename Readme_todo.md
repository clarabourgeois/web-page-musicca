\# Musicca Web Page Project

\## Project Overview

The \*\*Musicca Web Page Project\*\* is a static website designed to demonstrate the automation of development tasks using a \*\*Makefile\*\*. The project includes tools for:

- \*\*Dependency management\*\*
- \*\*Compilation of SCSS files to CSS\*\*
- \*\*Project versioning\*\*
- \*\*Packaging the project into a .tar.gz archive\*\*
- \*\*Running a Python HTTP server\*\*

This project highlights how a modern build tool can streamline the development process while meeting specific project requirements.

\---

\## Features

\### Automated Tasks

The project automates the following tasks through a Makefile:

- Installation of \*\*system and Python dependencies\*\*
- Compilation of \*\*SCSS to CSS\*\*
- Displaying the \*\*project version\*\*
- Packaging the project for distribution
- Running a local \*\*HTTP server\*\* to serve the webpage

\### Technology Stack

- \*\*HTML & SCSS\*\*: Core technologies for content and styling
- \*\*Python\*\*: Running a simple HTTP server
- \*\*SASS\*\*: Compiling SCSS files into CSS
- \*\*Makefile\*\*: Coordinating and automating tasks

\---

\## Prerequisites

Ensure you have the following installed on your system:

- \*\*Linux-based OS\*\* (or WSL for Windows users)
- \*\*Python 3\*\*
- \*\*Ruby\*\* (for SASS)
- \*\*GNU Make\*\*

\---

\## How to Build, Test, and Run

\### 1. Clone the Repository

bash

git clone https://github.com/clarabourgeois/web-page-musicca.git

cd web-page-musicca

2\. Install Dependencies

Install system dependencies, Python libraries, and SASS by running:

bash

Copier le code

make dependencies

3\. Compile SCSS to CSS

Generate the output.css file from the style.scss file:

bash

Copier le code

make css

4\. Run the HTTP Server

Start the server to serve the webpage locally:

bash

Copier le code

make server

The server will run on http://localhost:8000. Open this URL in your browser to view the webpage.

5\. Package the Project

Package the project into a compressed .tar.gz archive:

bash

Copier le code

make package

The archive will be created as project-1.0.0.tar.gz in the project directory.

Available Makefile Commands

Command	Description

make all	Install dependencies, compile SCSS, and run the server.

make dependencies	Install required system and Python dependencies.

make css	Compile SCSS files to CSS.

make server	Run the local HTTP server.

make clean	Remove the generated CSS file.

make version	Display the current project version.

make package	Package the project into a .tar.gz archive.

make help	Display a list of available Makefile commands.

Project Structure

plaintext

Copier le code

web-page-musicca/

├── assets/

│   ├── img/                 # Images used in the webpage

│   └── stylesheets/         # Directory for compiled CSS files

├── about.html               # HTML file for the webpage

├── style.scss               # SCSS file for custom styles

├── compile\_css.sh           # Bash script to compile SCSS to CSS

├── run\_server.py            # Python script for running the HTTP server

├── requirements.txt         # Python dependencies

├── makefile                 # Makefile for build automation

└── project-1.0.0.tar.gz     # Packaged project (generated after `make package`)

Replicability

The project can be fully replicated using simple commands:

make dependencies

make css

make server

Metadata

Version: 1.0.0

Build Tool: GNU Make

Additional Notes

Dependency Details

System Dependencies: Ruby (for SASS) and Python 3.

Python Dependencies: Listed in requirements.txt.

Future Improvements

Add tests to validate SCSS compilation and server functionality.

Include CI/CD pipelines for automated testing and deployment.

Enhance cross-platform compatibility (e.g., support for macOS).

License

This project is open source and available under the MIT licence

