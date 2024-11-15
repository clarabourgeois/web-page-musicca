# Variables
SASS_SCRIPT = ./compile_css.sh
SERVER_SCRIPT = ./run_server.py
SCSS_FILE = style.scss
CSS_FILE = assets/stylesheets/output.css
VERSION = 1.0.0

# Default target
all: dependencies clean version css server package help 

# Dependency management
dependencies:
	@echo "Installing system dependencies..."
	@sudo apt update
	@sudo apt install -y ruby-full python3 python3-pip
	@sudo gem install sass
	@echo "Installing Python dependencies..."
	@pip3 install -r requirements.txt

# Compile CSS target
css: $(CSS_FILE)

$(CSS_FILE): $(SCSS_FILE) $(SASS_SCRIPT)
	@echo "Compiling SCSS to CSS..."
	@bash $(SASS_SCRIPT)

# Server target
server:
	@echo "Starting server..."
	@python3 $(SERVER_SCRIPT)

# Clean target - Removes generated CSS files if necessary
clean:
	@echo "Cleaning generated CSS files..."
	@rm -f $(CSS_FILE)

# Show project version
version:
	@echo "Project Version: $(VERSION)"

# Package the project into a tar.gz archive
package:
	@echo "Packaging project into archive..."
	@tar -czf project-$(VERSION).tar.gz about.html $(SCSS_FILE) $(CSS_FILE) assets/ $(SASS_SCRIPT) $(SERVER_SCRIPT) makefile requirements.txt
	@echo "Package created: project-$(VERSION).tar.gz"

# Help target - displays usage information
help:
	@echo "Makefile for project"
	@echo "Available commands:"
	@echo "  make all        - Do all the following commands"
	@echo "  make dependencies - Install system and Python dependencies"
	@echo "  make css        - Compile SCSS to CSS"
	@echo "  make server     - Run the HTTP server"
	@echo "  make clean      - Clean generated CSS files"
	@echo "  make version    - Display the project version"
	@echo "  make package    - Package the project into an archive"
	@echo "  make help       - Display this help message"

.PHONY: all css server clean help

