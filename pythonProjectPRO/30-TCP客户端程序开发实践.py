'''
TCP客户端开发五步走：① 创建客户端套接字对象 ② 建立连接 ③ 发送数据 ④ 接收数据 ⑤ 关闭套接字对象
第一个知识点：
socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.AF_INET ：IP v4
socket.SOCK_STREAM ：TCP协议
第二个知识点：
tcp_client_socket.connect() => 连接服务器端（IP地址和端口号） => 参数是一个元组(IP地址，端口号)
第三个知识点：发送send()、接收数据recv()，注意事项：无论信息的发送还是接收都必须使用二进制流数据
encode() : 把字符串转二进制流数据
decode() : 把二进制流数据转换为字符串
'''
import socket

if __name__ == '__main__':
    # 1.创建客户端套接字对象
    tcp_cilent_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.和服务器端套接字建立链接(参数必须是一个元组)
    tcp_cilent_socket.connect(("127.0.0.1", 8080))
    # 3.发送数据
    tcp_cilent_socket.send('你不讨厌,但是毫无作用'.encode(encoding='gbk'))
    # 4.接收数据
    recv_data = tcp_cilent_socket.recv(1024).decode('gbk')
    print(recv_data)
    # 5.关闭客户端套接字
    tcp_cilent_socket.close()