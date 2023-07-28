# # 请同学自行查看int的用法 以及进制转化
# class Partiment(object):
#     def __init__(self,fn,*pargs,**pkwargs):
#         self.fn = fn
#         self.args = pargs
#         self.kwargs = pkwargs
#     def __call__(self,*args,**kwargs):
#         final_args = self.args+args
#         final_kwargs = self.kwargs.copy()
#         final_kwargs.update(kwargs)
#         return self.fn(*final_args,**final_kwargs)
# int_two = Partiment(int,base=2)
# print(int_two('100'))
#
#
#
# int_x = Partiment(int,base=16)
# print(int_x('A'))
import copy
d = {'a':[1,2,3]}
d1 = copy.copy(d)
d1.get('a').append(4)
print(d.get('a'))
d2 = copy.deepcopy(d1)
d2['a'] = 100
print(d1.get('a'))
d.update(b = 10)
print(d2.get('b'))
