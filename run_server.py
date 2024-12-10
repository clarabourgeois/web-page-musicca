#!/usr/bin/env python3
"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
from http.server import HTTPServer, SimpleHTTPRequestHandler
import logging
from urllib.parse import parse_qs
import re

# Configurer le logging pour inclure tous les niveaux (DEBUG, INFO, WARNING, ERROR, CRITICAL)
logging.basicConfig(
    level=logging.DEBUG,  # Niveau de log par défaut
    format='%(asctime)s - %(levelname)s - %(message)s',  # Format des logs
    handlers=[
        logging.FileHandler('app.log'),  # Écrire les logs dans un fichier 'app.log'
        logging.StreamHandler()  # Afficher les logs dans la console
    ]
)

def safeget(dct, *keys):
    """Retourne la valeur d'une clé dans un dictionnaire si elle existe, sinon None."""
    for key in keys:
        try:
            dct = dct[key]
        except KeyError:
            return None
    return dct


class S(SimpleHTTPRequestHandler):
    """Configure la réponse HTTP de base"""
    def _set_response(self):
        """Définir la réponse HTTP de base (code 200, type HTML)."""
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        logging.debug("Response set with 200 status code")

    def do_GET(self):
        """Traite une requête GET"""
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        super().do_GET()

    def do_post(self):
        """Traite une requête post"""
        logging.debug("Processing post request for path: %s", self.path)

        # Lecture du contenu de la requête post
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.debug("Received post data: %s", post_data.decode('utf-8'))

        # Log des informations de la requête POST
        logging.info("post request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                     str(self.path), str(self.headers), post_data.decode('utf-8'))

        post_data_fields = parse_qs(post_data.decode('utf-8'))


        self._set_response()
	# Logique de traitement des données
        if (re.match(r"^/register", self.path) and
            safeget(post_data_fields, "username", 0) == "admin@domain.com" and
            safeget(post_data_fields, "password", 0) == "rainbow"):
            logging.info("Registration successful for admin user")
            self.wfile.write("""
                <h1>Congrats, you succeeded to submit the correct data</h1>
                """.encode('utf-8'))
        else:
            # CRITICAL si une tentative incorrecte est détectée
            logging.critical("""
                             CRITICAL ERROR: Unauthorized access attempt for path %s. Post data: %s
                             """, self.path, post_data.decode('utf-8'))
            logging.warning("Bad request received for path %s", self.path)
            self.wfile.write("""
                <h1>Error : Bad Request</h1> POST request for {self.path}<br> Body : <br> {post_data.decode('utf-8')}
                """.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8000):
    """Démarre le serveur HTTP"""
    logging.info("Initializing server...")
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info("Starting http server on port %d...\n", port)
    try:
        httpd.serve_forever()
        logging.info("Server is running...")
    except KeyboardInterrupt:
        logging.warning("Server interrupted by user")
    except (ConnectionError, TimeoutError) as e:
        logging.error("Network error: %s", e)
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv
    # Exécution du serveur avec le port passé en argument, ou avec le port par défaut (8080)
    if len(argv) == 2:
        logging.info("Starting server with custom port: %s", argv[1])
        run(port=int(argv[1]))
    else:
        logging.info("Starting server on default port: 8000")
        run()
