from urllib.parse import urlencode
from urllib.request import urlopen
def send_to_server(url, post_data = None):
    if post_data:
        para = urlencode(post_data)
        page = urlopen(url, para.encode('utf-8'))   #注意这里不encode会报错
    else:
        page = urlopen(url)
    return(page.read().decode('utf-8'))
url = "http://publish.domestore.cn/pic/upload"