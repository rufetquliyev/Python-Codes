'''İçində olduğunuz dirin parentinin parentində olan faylların extensionlarını göstərən program hazırlayın.'''
# from pathlib import Path
# current_path = Path('.').absolute()
# parent = current_path.parent.parent
# data = list(parent.iterdir())
# extensions = []
# for i in data:
#     if i.is_file():
#         extensions.append(i.suffix)
# print(extensions)
import json
from uuid import uuid4
import secrets

with open('info.json', mode = 'r') as file:
    content = file.read()
    data = json.loads(content)
    
for datas in data:
    datas.update({'ID': str(uuid4())})
    datas.update({'Password': str(secrets.token_urlsafe(10))})

with open('info.json', mode = 'w') as new_file:
    new_file.write(json.dumps(data))
