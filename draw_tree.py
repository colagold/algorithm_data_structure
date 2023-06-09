import matplotlib.pyplot as plt
import networkx as nx

# 构建二叉树
tree = nx.DiGraph()
tree.add_node(0, label='A')
tree.add_node(1, label='B')
tree.add_node(2, label='C')
tree.add_node(3, label='D')
tree.add_node(4, label='E')
tree.add_node(5, label='F')
tree.add_node(6, label='G')
tree.add_edges_from([(0,1), (0,2), (1,3), (1,4), (2,5), (2,6)])

# 绘制图形
pos = {0:(0,0), 1:(-1,-1), 2:(1,-1), 3:(-2,-2), 4:(0,-2), 5:(2,-2), 6:(3,-3)}
labels = nx.get_node_attributes(tree, 'label')
nx.draw(tree, with_labels=True, labels=labels, node_color='red', node_size=800)
plt.show()