'''
请求使用fastapi代理爬虫题目中图片,实现一个简单的图片展示服务，要求如下：
A.要求首页显示，目前有哪些图片，不用展示具体图片，仅展示图片名字；
B.点击图片名字，跳转到具体的图片页面。
'''
from fastapi import FastAPI
from fastapi import Response
import uvicorn

app = FastAPI()


@app.get('/')
def main():
    with open(f'01/index.html', 'rb') as f:
        data = f.read()
        # 返回数据给客户端浏览器
    return Response(content=data, media_type='text/html')


@app.get('/{path}')
def func0(path: str):
    with open(f'01/{path}', 'rb') as f:
        data = f.read()
    return Response(content=data, media_type='jpg')


@app.get('/favicon.ico')
def get_ico():
    with open(f'01/favicon.ico', 'rb') as f:
        data = f.read()
    return Response(content=data, media_type='image/x-ico')


uvicorn.run(app, host='127.0.0.1', port=8000)
