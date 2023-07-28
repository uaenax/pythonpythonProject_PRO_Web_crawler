# 1.导入模块
from fastapi import FastAPI
from fastapi import Response
import logging
import uvicorn

# 2.创建FastAPI对象
app = FastAPI()

# 配置logging日志的输出信息(输出格式,输入到哪个文件)
f = open('fastapi.log', 'a', encoding='utf-8')
# 设置日志等级和输出日志格式
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s"- %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    stream=f)

# 3.使用装饰器处理html请求
@app.get('/')  # 首页
def main():
    with open(f'source/html/index.html', 'rb') as f:
        data = f.read()
    logging.info('访问/首页')
    # 返回数据给客户端浏览器
    return Response(content=data, media_type='text/html')


# 5.返回图片信息
@app.get('/images/{path}')
def func0(path: str):
    with open(f'source/images/{path}', 'rb') as f:
        data = f.read()
    logging.info(f'访问/images/{path}/图片')
    return Response(content=data, media_type='jpg')


@app.get('/{path}')
def get_html(path: str):
    with open(f'source/html/{path}', 'rb') as f:
        data = f.read()
    logging.info(f'访问/{path}/页面')
    # 返回数据给客户端浏览器
    return Response(content=data, media_type='text/html')


# 添加一个小图标接收请求与处理返回
@app.get('/favicon.ico')
def get_ico():
    with open(f'source/html/favicon.ico', 'rb') as f:
        data = f.read()
    logging.info(f'访问/favicon.ico/小图标')
    return Response(content=data, media_type='image/x-ico')


# 4.启动服务器开始监听
uvicorn.run(app, host='127.0.0.1', port=8000)
