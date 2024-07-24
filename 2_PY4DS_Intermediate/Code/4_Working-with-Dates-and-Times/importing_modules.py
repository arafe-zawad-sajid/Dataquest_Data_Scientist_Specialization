# 4.2 Importing Modules
# 1) import the whole module by name
import csv

# definitions are available using the format module_name.definition_name
csv.reader()


# 2) import the whole module with an alias
import csv as c

# definitions are available using the format alias.definition_name
c.reader()


# 3) import one or more definitions from the module by name
from csv import reader, writer

# the definitions you imported are available using the format definition_name
reader()
writer()


# 4) import all definitions with a wildcard
from csv import *

# all definitions from the module are available using the format definition_name
reader()
writer()
get_dialect()
