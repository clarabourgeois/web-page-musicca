# Web Page Musicca Project

This project is a web application for showcasing music-related content. It uses SCSS for styling and Python for the server-side logic. The build process is automated using a `Makefile`.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [How to Build, Test, and Run](#how-to-build-test-and-run)
  - [Installing Dependencies](#installing-dependencies)
  - [Compiling SCSS to CSS](#compiling-scss-to-css)
  - [Running the Server](#running-the-server)
  - [Cleaning Generated Files](#cleaning-generated-files)
- [Project Version](#project-version)
- [Packaging](#packaging)
- [Help](#help)
- [Build Tool Configuration](#build-tool-configuration)

## Prerequisites

Before you begin, ensure you have the following installed on your system:

1. **Ruby** (to compile SCSS using `sass`)
2. **Python 3** and `pip3` (for the server-side logic)
3. **GNU Make** (to execute the build commands)

## Project Structure

web-page-musicca/ ├── about.html ├── assets/ │ └── stylesheets/ │ └── output.css # Generated CSS file ├── requirements.txt # Python dependencies ├── style.scss # SCSS file to be compiled ├── compile_css.sh # Script to compile SCSS to CSS ├── run_server.py # Python script for running the server ├── makefile # Build tool configuration └── project-version.tar.gz # Packaged project (created via make package)

## How to Build, Test, and Run

### Installing Dependencies

Run the following command to install all necessary system and Python dependencies:

```bash
make dependencies
This will:

Update the system package index
Install Ruby and Python
Install the sass gem for SCSS compilation
Install Python packages specified in requirements.txt
Compiling SCSS to CSS
To compile the SCSS file into CSS, use:
