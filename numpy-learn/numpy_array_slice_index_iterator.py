import numpy as np

if __name__ == '__main__':
    arr_1_d = np.array([1, 2, 3, 4, 5, 6,7,8,9])
    arr_2_d = np.array([[1, 2],
                        [3, 4],
                        [5, 6]])
    arr_3_d = np.arange(27).reshape((3,3,3))

    # index
    print(arr_1_d[3])
    print(arr_2_d[1])
    print(arr_2_d[1,1])
    print(arr_3_d[2,2,2])

    # slice
    print(arr_1_d[:4])
    print(arr_2_d[:2])
    # [0,2) 行的， 每一行的下标1的元素
    print(arr_2_d[:2,1])
    print(arr_3_d[:,1,1])

    # from [0,7) 每2个元素赋值为 99
    arr_1_d[:7:2] = 99
    print(arr_1_d)

    # reverse
    print(arr_1_d[::-1])

    # iterator
    for row in arr_3_d:
        print(row)
    # iterator 每一个元素
    for item in arr_3_d.flat:
        print(item)
