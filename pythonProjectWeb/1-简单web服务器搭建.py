# 1.导入模块
from fastapi import FastAPI
from fastapi import Response

import uvicorn

# 2.创建FastAPI对象
app = FastAPI()


# 3.使用装饰器处理html请求
@app.get('/')  # 首页
def main():
    with open(f'source/html/index.html', 'rb') as f:
        data = f.read()
    # 返回数据给客户端浏览器
    return Response(content=data, media_type='text/html')


# 5.返回图片信息
@app.get('/images/{path}')
def func0(path: str):
    with open(f'source/images/{path}', 'rb') as f:
        data = f.read()
    return Response(content=data, media_type='jpg')


@app.get('/{path}')
def get_html(path: str):
    with open(f'source/html/{path}', 'rb') as f:
        data = f.read()
    # 返回数据给客户端浏览器
    return Response(content=data, media_type='text/html')


# 添加一个小图标接收请求与处理返回
@app.get('/favicon.ico')
def get_ico():
    with open(f'source/html/favicon.ico', 'rb') as f:
        data = f.read()
    return Response(content=data, media_type='image/x-ico')


# 4.启动服务器开始监听
uvicorn.run(app, host='127.0.0.1', port=8000)
