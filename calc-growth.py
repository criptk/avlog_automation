#!/usr/bin/python3

from pyexcel_xls import get_data
import json

data = get_data("ips_growth_compared.xls")
print (json.dump(data))
