import numpy as np


from dipy.viz import actor, window

from get_streamlines import get_tck_streamlines, get_trk_streamlines
from tracts import trans_cosine
from dist_for_LocGlb import calcLocalCosine, calcGlobalCosine

# "D:/njust/wuye/primate/aotus/fibers_dti.trk"
# D:/njust/wuye/some_tracts/599469/tracts/AF_left.trk
# streamlines = get_tck_streamlines("D:/njust/wuye/human_tck/postop_sub-CON05/track.tck")


streamlines = get_trk_streamlines("D:/njust/wuye/some_tracts/620434/tracts/CA.trk")


totalLines = len(streamlines)

print(totalLines)
# print(streamlines)


k = 19
all_cos_dist = np.array([])
all_streams_beta = np.array([])

# 求出所有纤维的余弦级数的系数表示
for i in range(totalLines):
    wfs, beta = trans_cosine(streamlines[i].T, k)
    beta = beta.flatten()
    # 如果 all_streams_beta 为空，直接赋值，否则垂直堆叠
    if all_streams_beta.size == 0:
        all_streams_beta = beta
    else:
        all_streams_beta = np.vstack((all_streams_beta, beta))

print(all_streams_beta.shape)
loc_num = 20
glb_num = 500
x = 0
loc_beta, loc_dist = calcLocalCosine(all_streams_beta, all_streams_beta[x], loc_num)
glb_beta, glb_dist = calcGlobalCosine(all_streams_beta, all_streams_beta[x], glb_num)
print(loc_beta.shape, loc_dist.shape, loc_beta, loc_dist)
print(glb_beta.shape, glb_dist.shape, glb_beta, glb_dist)


lines2 = []

flag = 0
while flag < 30:
    lines2.append(streamlines[flag])
    flag += 1

interactive = True

scene = window.Scene()
scene.SetBackground(1, 1, 1)
scene.add(actor.line(streamlines))
if interactive:
    window.show(scene)
else:
    window.record(scene, out_path='tractograms_initial.png', size=(600, 600))

# line = streamlines[0]
# fig = plt.figure()
# # 在图形中创建一个 3D 子图
# ax = fig.add_subplot(111, projection='3d')
#
# print(line)
#
# # 绘制散点图
# ax.scatter(line[:,0], line[:,1], line[:,2], c='b', marker='.')
#
# # 设置坐标轴标签（可选）
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')
#
# # 显示图形
# plt.show()