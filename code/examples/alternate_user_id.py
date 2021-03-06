# See discussion and more examples at http://packages.python.org/pymqi/examples.html
# or in doc/sphinx/examples.rst in the source distribution.

import pymqi
import CMQC

queue_manager = "QM01"
channel = "SVRCONN.1"
host = "192.168.1.135"
port = "1434"
queue_name = "TEST.1"
message = "Hello from Python!"
alternate_user_id = "myuser"
conn_info = "%s(%s)" % (host, port)

qmgr = pymqi.connect(queue_manager, channel, conn_info)

od = pymqi.OD()
od.ObjectName = queue_name
od.AlternateUserId = alternate_user_id

queue = pymqi.Queue(qmgr)
queue.open(od, CMQC.MQOO_OUTPUT | CMQC.MQOO_ALTERNATE_USER_AUTHORITY)
queue.put(message)

queue.close()
qmgr.disconnect()
