# import numpy as np
#
# if __name__ == '__main__':
#     # base
#     arr =np.array( [1,2,3,4] )
#     arr =np.array( [ [1,2,3],[4,5,6]] )
#
#     # 1d array
#     arr = np.arange(15)
#     print(arr.shape)
#
#     # 2d array
#     arr = np.arange(15).reshape(3,5)
#     print(arr.shape)
#
#     # 3d array
#     arr = np.arange(24).reshape(2,3,4)
#     print(arr.shape)
#
#     # zeros -> 全是0的数组
#     arr = np.zeros( (2,3) )
#     print(arr)
#
#     # ones -> 全是1的数组
#     arr = np.ones( (2,3) )
#     print(arr)
#
#     # empty -> 一个随机的，根据内存状态生成的数组
#     arr = np.empty( (2,3) )
#     print(arr)
#
#     # 指定 dtype
#     arr = np.ones( (2,3), dtype= np.complex64)
#     print(arr)
#
#     # linspace  (from,to,size) (1,2,5) 从1->2 均分为5个元素
#     arr = np.linspace(1,2,5)
#     print(arr)
#
#
