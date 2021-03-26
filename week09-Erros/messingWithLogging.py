# messing with logging
# attributes you can put in the basicConfig
#   level
#   filename
#   filemode
#   format
#       %(name)s - %(levelname)s - %(message)s -  %(asctime)s - %(lineno)d

import logging
# logging.basicConfig(level=logging.INFO)
# sets the level to whatever you want

# logging.basicConfig(level=logging.ERROR) 
logging.basicConfig(filename = "./debugging.log", 
    filemode = "a", 
    level=logging.DEBUG, 
    format="%(asctime)s - %(levelname)s - %(message)s - line: %(lineno)d") 

# didn't work the first time as we had basicConfig listed twice

name = "joe"

logging.error  ("this is an error")
logging.critical ("hiya")
logging.warning("Don't know %s", name) # %s string
logging.info ("still going")
logging.debug("and so is this")

# default is to warning level
