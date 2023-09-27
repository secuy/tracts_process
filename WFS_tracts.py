import numpy as np


def WFS_tracts(tract, para, k):
    """
    计算余弦级数表示的 3D 曲线。

    Parameters:
        tract (numpy.ndarray): 形状为 (3, n_vertex) 的 3D 曲线坐标。
        para (numpy.ndarray): 弧长参数化。
        k (int): 余弦级数的次数。

    Returns:
        wfs (numpy.ndarray): 余弦级数表示的曲线。
        beta (numpy.ndarray): 级数系数。

    """
    n_vertex = len(para)

    # 将 para 进行相反数操作拼接起来，长度变为原来的两倍减一，变成偶函数
    para_even = np.concatenate((-para[-2::-1], para))
    # 将 tract 进行相同的操作，区别是不加负号，长度变为原来的两倍减一，变偶
    tract_even = np.hstack((tract[:, -2::-1], tract))

    Y = np.zeros((2 * n_vertex - 1, k + 1))
    # 将 para 重复 k+1 遍
    para_even = np.tile(para_even, (k + 1, 1)).T
    # 0到k乘pi复制2倍的 vertex 的数量-1
    pi_factors = np.tile(np.arange(k + 1), (2 * n_vertex - 1, 1)) * np.pi
    Y = np.cos(para_even * pi_factors) * np.sqrt(2)


    # # 使用非负最小二乘法求解 beta
    # from scipy.optimize import nnls
    # beta, _ = nnls(Y.T, tract_even.T)

    # # 使用多元线性回归求解 beta
    # from sklearn.linear_model import LinearRegression
    # model = LinearRegression()
    # model.fit(Y, tract_even.T)
    # beta = model.coef_.T

    # 计算 beta
    YTY = np.dot(Y.T, Y)
    YTY_inv = np.linalg.pinv(YTY)
    YTY_inv_YT = np.dot(YTY_inv, Y.T)
    beta = np.dot(YTY_inv_YT, tract_even.T)

    # 计算 hat
    hat = np.dot(Y, beta)

    # 计算 wfs
    n_vertex = len(para)
    wfs = hat[n_vertex:(n_vertex * 2 - 1), :]
    return wfs, beta