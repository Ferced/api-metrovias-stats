from server.instance import server
import sys, os

# Se necesitan importar todas las rutas/resources/controllers
# asi se registran con el servidor
from controllers.metrovias_stats import *
from controllers.actualizar_bd import *

if __name__ == '__main__':
    server.run()