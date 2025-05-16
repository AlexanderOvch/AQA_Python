import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "randominfo-master", "randominfo"))

import __init__ as randominfo

person = randominfo.Person()
addr = person.address
addr_str = f"{addr.get('street', '')}, {addr.get('landmark', '')}, {addr.get('area', '')}, {addr.get('city', '')}, {addr.get('state', '')}"
print(f"{person.full_name}, {person.gender}, {person.country}, {addr_str}")
