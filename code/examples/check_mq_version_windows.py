# See discussion and more examples at http://packages.python.org/pymqi/examples.html
# or in doc/sphinx/examples.rst in the source distribution.

import logging
import winreg

logging.basicConfig(level=logging.INFO)

key_name = "Software\\IBM\\MQSeries\\CurrentVersion"

try:
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_name)
except WindowsError:
    logging.info("Could not find WebSphere MQ-related information in Windows registry.")
else:
    version = winreg.QueryValueEx(key, "VRMF")[0]
    logging.info("WebSphere MQ version is [%s]." % version)
