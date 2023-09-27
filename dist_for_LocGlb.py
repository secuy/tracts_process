import numpy as np

from calc_cosine_dist import calcCosDist

# all_streams是所有纤维的余弦系数长度为3*(k+1),stream_beta是计算的当前纤维,loc_num是求临近当前纤维的最近的个数
def calcLocalCosine(all_streams_beta, stream_beta, loc_num):
    all_cos_dist = np.array([])
    for lin in all_streams_beta:
        cos_dist = calcCosDist(stream_beta, lin)
        all_cos_dist = np.append(all_cos_dist, cos_dist)

    dis_idx_sort = np.argsort(-all_cos_dist)
    loc_beta = np.array(all_streams_beta[dis_idx_sort[0]])
    loc_dist = np.array([all_cos_dist[dis_idx_sort[0]]])
    for i in range(1, loc_num+1):
        loc_beta = np.vstack((loc_beta, all_streams_beta[dis_idx_sort[i]]))
        loc_dist = np.vstack((loc_dist, all_cos_dist[dis_idx_sort[i]]))
    return loc_beta, loc_dist


# all_streams是所有纤维的余弦系数长度为3*(k+1),glb_num是从所有纤维中抽出来的个数
def calcGlobalCosine(all_streams_beta, stream_beta, glb_num):
    rand_num = np.random.randint(0, all_streams_beta.shape[0], glb_num)
    glb_beta = np.array(all_streams_beta[rand_num[0]])
    cos_dist = calcCosDist(stream_beta, all_streams_beta[rand_num[0]])
    glb_dist = np.array([cos_dist])
    for i in range(1, len(rand_num)):
        cos_dist = calcCosDist(stream_beta, all_streams_beta[rand_num[i]])
        glb_dist = np.append(glb_dist, cos_dist)
        glb_beta = np.vstack((glb_beta, all_streams_beta[i]))
    return glb_beta, glb_dist