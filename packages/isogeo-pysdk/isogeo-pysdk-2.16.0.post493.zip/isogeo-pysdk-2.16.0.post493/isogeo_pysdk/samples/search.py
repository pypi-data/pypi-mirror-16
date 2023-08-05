# -*- coding: UTF-8 -*-
#!/usr/bin/env python
from __future__ import (absolute_import, print_function, unicode_literals)
# -----------------------------------------------------------------------------
# Name:         Isogeo
# Purpose:      Python minimalist SDK to use Isogeo API
#
# Author:       Julien Moura (@geojulien)
#
# Python:       2.7.x
# Created:      22/12/2015
# Updated:      10/01/2016
# -----------------------------------------------------------------------------

# #############################################################################
# ########## Libraries #############
# ##################################

# Standard library
import ConfigParser     # to manage options.ini
from os import path

# Isogeo
from isogeo_pysdk import Isogeo

# #############################################################################
# ######## Main program ############
# ##################################

# storing application parameters into an ini file
settings_file = r"../isogeo_params.ini"

# testing ini file
if not path.isfile(path.realpath(settings_file)):
    print("ERROR: to execute this script as standalone, you need to store your Isogeo application settings in a isogeo_params.ini file. You can use the template to set your own.")
    import sys
    sys.exit()
else:
    pass

# reading ini file
config = ConfigParser.SafeConfigParser()
config.read(settings_file)

share_id = config.get('auth', 'app_id')
share_token = config.get('auth', 'app_secret')

# ------------ Real start ----------------
# instanciating the class
isogeo = Isogeo(client_id=share_id,
                client_secret=share_token)

# check which sub resources are available
print(isogeo.sub_resources_available)
print(isogeo.tr_types_label_fr)

# getting a token
jeton = isogeo.connect()

# let's search for metadatas!
print(dir(isogeo))
search = isogeo.search(jeton)

print(search.keys())
print(search.get('query'))
print("Total count of metadatas shared: ", search.get("total"))
print("Count of resources got by request: {}\n".format(len(search.get("results"))))
