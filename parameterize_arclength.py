import numpy as np


def parameterize_arclength(tract):
    """
    计算弧长并执行单位长度参数化。

    Parameters:
        tract (numpy.ndarray): 形状为(3, n_vertex)或(2, n_vertex)的输入曲线数组。

    Returns:
        arc_length (float): 总弧长
        para (numpy.ndarray): 映射曲线到单位区间[0, 1]的参数数组
    """
    n_vertex = tract.shape[1]
    # n_vertex 必须大于等于2才能正常运行此函数。

    p0 = tract[:, :-1]
    p1 = tract[:, 1:]
    disp = p1 - p0

    # 计算每一段的欧氏距离
    L2 = np.sqrt(np.sum(disp ** 2, axis=0))

    arc_length = np.sum(L2)

    # 计算参数化值
    cum_len = np.cumsum(L2) / arc_length
    para = np.zeros(n_vertex)
    para[1:] = cum_len

    return arc_length, para


