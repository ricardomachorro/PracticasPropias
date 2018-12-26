#En python se puede usar fechas con el uso de fehcas exactas
#por medio de imprtar el modulo datetime

import datetime #importacion modulo datetime

dt = datetime.datetime.strptime("2016-04-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")

print("date:",dt)

from datetime import datetime, timedelta, timezone 
JST = timezone(timedelta(hours= +9))

dt = datetime(2015,1,1,12,0,0,tzinfo=JST)
print(dt)

print(dt.tzname())

