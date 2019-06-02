import matplotlib.pyplot as plt
import networkx as nx


def calculate_degree(G):
    # 计算图中每个节点的度，描述中心度
    Gd = G.degree();
    print('图中各个点的度为：')
    print(Gd)

    print('图中各个点的正则化度为：')
    # 正则法一：每个度除于最大度（1045）
    # for i in range(len(Gd)):
    #     # 最大的度为1045
    #     print("(%d, %f)" % (i, Gd[i] / 1045))

    # 正则法二：每个度除以节点数
    print(nx.degree_centrality(G))


def calculate_transitivity(G):
    # 计算传递性
    print('图的传递性：')
    print(nx.transitivity(G))


def calculate_clustering(G):
    # 计算聚集系数
    print('图中各个点的聚集系数：')
    print(nx.clustering(G))


def calculate_betweenness(G):
    # 计算betweenness
    print('图中各个点的节点介数中心系数：')
    print(nx.betweenness_centrality(G))


def draw(G):
    # 设置中心放射布局
    pos = nx.spring_layout(G)
    # 计算每个结单距离聚簇中心的距离
    dmin = 1
    ncenter = 0

    for n in pos:
        x, y = pos[n]
        d = (x - 0.5) ** 2 + (y - 0.5) ** 2
        if d < dmin:
            ncenter = n
            dmin = d

    # 生成最短路径保存在map中
    p = dict(nx.single_source_shortest_path_length(G, ncenter))

    nx.draw_networkx_edges(G, pos, nodelist=[ncenter], line_color='grey', alpha=0.2)
    nx.draw_networkx_nodes(G, pos, nodelist=list(p.keys()), node_size=10, node_color=list(p.values()),
                           cmap=plt.cm.Reds_r)
    plt.show()


# 读取facebook数据集
facebook = open('facebook.txt')
# 生成空白无向图
G = nx.Graph()

for line in facebook.readlines():
    edge = line.strip('\n').split(' ')
    G.add_edge(int(edge[0]), int(edge[1]))

# ----------------中心度描述
print('-----图的中心度描述方法------')
calculate_degree(G)
# 计算量较大，所花时间在两分钟左右
# calculate_betweenness(G)

# ----------------传递性描述
print('-----图的传递性描述------')
calculate_transitivity(G)

# ----------------全局聚类系数描述
print('-----图的全局聚类系数描述------')
calculate_clustering(G)

# ----------------图像绘制
# 由于渲染速度较慢，可能所花时间在一分钟左右
# draw(G)
