import numpy as np
import matplotlib.pyplot as plt

from parameterize_arclength import parameterize_arclength
from WFS_tracts import WFS_tracts
def trans_cosine(tract, k):
    # 模拟
    # t = np.arange(0, 10.1, 0.1)
    # print(t.shape)
    # tract = np.array([t * np.sin(t), t * np.cos(t), t])

    # 将 x、y、z 坐标映射到单位区间 [0,1]
    arc_length, para = parameterize_arclength(tract)
    # plt.figure()
    # plt.subplot(3, 1, 1)
    # plt.plot(para, tract[0, :])
    # plt.subplot(3, 1, 2)
    # plt.plot(para, tract[1, :])
    # plt.subplot(3, 1, 3)
    # plt.plot(para, tract[2, :])

    # 在 [0,1] 区间中进行余弦级数表示
    wfs, beta = WFS_tracts(tract, para, k)

    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    # ax.plot(tract[0, :], tract[1, :], tract[2, :], '.b')
    # ax.plot(wfs[:, 0], wfs[:, 1], wfs[:, 2], 'k')

    # 显示图形
    plt.show()
    return wfs, beta
