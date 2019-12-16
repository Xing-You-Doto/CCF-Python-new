import requests
import re
import os

def add(payloads):
    url = 'http://codepedia.trustie.net/operations/add_annotation/'
    add_log = open('add_result.txt','w')
    for payload in payloads:
        i = payload[0]
        content = payload[1]
        data = {
            'file_id': 180354,
            'linenum': i,
            'content': content
        }
        text = requests.post(url, data=data, headers=header)
        if text.status_code==200:
            if re.search('fail',text.text):
                print(i , ': fail to add, maybe already add')
                add_log.write('{} , : fial to add, maybe already add\n'.format(str(i)))
            else:
                print(i , ': add succeed')
                add_log.write('{} , : add succeed\n'.format(str(i)))
        else:
            print(i, 'error')
            add_log.write('{} , : error\n'.format(str(i)))

# def delete(lines):
#

# def modify(content,lines):
#     for i in lines:
#         data = {
#             'file_id': 180163,
#             'linenum': i,
#             'anno_id': 448749+i-5935,
#             'content': content
#         }
#         print(requests.post(url, data=data, headers=header))
#



header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
'Accept': 'application/json, text/javascript, */*; q=0.01',
'X-Requested-With': 'XMLHttpRequest',
'Referer': 'http://codepedia.trustie.net/projects/keras/keras/layers/recurrent.py',
'Cookie': 'sessionid=odhcw903mf8bqx7xltsepzay47nxh6jc'
}


# lines = [x for x in range(5935,5944)]
# add(content='哈哈哈',lines=lines)

f = open('payload',encoding='UTF-8')
a = f.readlines()
payloads = []
for i in a:
    n=i.split(':',1)
    line = int(n[0])
    content = n[1]
    payloads.append([line,content])
    print(payloads)

add(payloads)



