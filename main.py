import json

object = json.loads('[{"id":1,"data":"Item 1"} , {"id":2,"data":"Item 2"} , {"id":3,"data":"Item 3"} ]')

for item in object:
    print(item['data'])
