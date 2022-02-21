import json
from collections import OrderedDict

data = OrderedDict()

#direction (up/down), height(cm),type(head/body/both)
#warm (on/off)

data['moter'] = {'direction':'up','height':'cm','type':'head'} 
data['warm'] = 'on'

print(json.dumps(data,ensure_ascii=False, indent ='\t'))