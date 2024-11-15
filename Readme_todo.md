# Musicca Web Page Project  

## Project Overview  
The Musicca Web Page Project is a simple static website designed to demonstrate the automation of common development tasks using a **Makefile**. This project uses tools like **SASS** for CSS compilation, **Python** for running a local HTTP server, and includes dependency management, version control, and packaging.  

This project serves as a demonstration of modern build tool capabilities and aims to meet the requirements for managing dependencies, automating tasks, and packaging the project.  

---

## Features  

### Automated Tasks  
This project uses a `Makefile` to automate the following tasks:  
- **Dependency Management:** Installing system and Python dependencies.  
- **Compilation:** Converting SCSS files to CSS using SASS.  
- **Version Management:** Displaying the current project version.  
- **Packaging:** Creating a `.tar.gz` archive of the project for distribution.  
- **Server:** Running a Python-based HTTP server to serve the webpage locally.  

### Technology Stack  
- **HTML & SCSS**: For the website content and styling.  
- **Python**: For running the HTTP server (`http.server`).  
- **SASS**: For compiling SCSS into CSS.  
- **Makefile**: Build tool to orchestrate all tasks.  

---

## Prerequisites  

Before you can build and run this project, ensure you have the following installed on your system:  
- **Linux-based OS** (or WSL for Windows users)  
- **Python 3**  
- **Ruby**  
- **SASS (Ruby Gem)**  
- **GNU Make**  

---

## How to Build, Test, and Run  

### 1. Clone the Repository  
```bash  
git clone https://github.com/clarabourgeois/web-page-musicca.git  
cd web-page-musicca

### 2. Install Dependencies
Install system dependencies, Python libraries, and SASS by running:  

```bash
make dependencies  
  
