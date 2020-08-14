# Python
##描述：该脚本目前适合下载爱奇艺，腾迅视频VIP视频
##注意：只适全python爬虫的学习者，不适合专门去看电影的爱好者
##导入的两个模块，其中requests模块需要自行下载
from multiprocessing import Pool
import requests
##定义一个涵数
def demo(i):
    url = "https://vip.okokbo.com/20180114/ArVcZXQd/1000kb/hls/phJ51837151%03d.ts" % i
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36"}
    req = requests.get(url, headers=headers)
    with open('./mp4/ {}'.format(url[-10:]), 'wb') as f:
        f.write(req.content)

if __name__ == '__main__':
    pool = Pool(20)
    for i in range(100):
        pool.apply_async(demo, (i,))
   
    pool.close()
    pool.join()
