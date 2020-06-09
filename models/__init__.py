import os
import importlib

# Imports all the modules from this package (models).
# We need this code to make migration framework working.
for module in os.listdir(os.path.dirname(__file__)):
    if module == '__init__.py' or module[-3:] != '.py':
        continue
    importlib.import_module(__package__ + '.' + module[:-3])
