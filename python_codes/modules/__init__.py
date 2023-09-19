# Ref. https://www.tutorialsteacher.com/python/python-package

# -------------------------------------------------------
# Package
# -------------------------------------------------------
# 1. if this is a package folder, __init__.py must exist, even it's an empty file
# 2. PYTHONPATH:
#                Ensure that the directory containing your mypackage is included in the Python path (sys.path).
#                If it's not, you may need to add it manually or modify the PYTHONPATH environment variable.

# ------------- import folder/module --------------
# https://csatlas.com/python-import-file-module/

# ------------- reference pandas --------------
# Ref. https://github.com/pandas-dev/pandas/tree/main/pandas
# import modules.built_in


# If this package folder is not under os.sys PATH, manually import files explicitly
# from modules import built_in

from .built_in import print_name
