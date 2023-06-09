from matplotlib import pyplot as plt
import networkx as nx
from Node import TreeNode, Node





#[1,null,0,0,1]
def to_list(string):
    string=string[1:-1].replace('null', 'None').split(',')
    res=[]
    for i in string:
        if i!="None":
            res.append(int(i))
        else:
            res.append(eval(i))
    return res

def create_binary_tree_from_list(value_list:list)->TreeNode:
    root=TreeNode(value_list.pop(0))
    q=[root]

    while len(q)>0:
        node=q.pop(0)
        if len(value_list) == 0: break
        if value_list[0] is None: #左节点
            node.left=None
            value_list.pop(0)
        else:
            node.left=TreeNode(value_list.pop(0))
            q.append(node.left)
        if len(value_list)==0:break
        if value_list[0] is None: # 右子树
            node.right=None
            value_list.pop(0)
        else:
            node.right=TreeNode(value_list.pop(0))
            q.append(node.right)
    return root

def create_linklist_from_list(value_list:list)->Node:
    head=Node(value_list[0])
    temp=head
    for value in value_list[1:]:
        t=Node(value)
        temp.next=t
        temp=temp.next
    return head

def print_tree(root:TreeNode):
    if root is None:
        return
    print(root.value)
    print_tree(root.left)
    print_tree(root.right)

def plot_tree(node, x, y, parent_x=None, parent_y=None):
    if node is not None:
        plt.plot([parent_x, x], [parent_y, y], 'k-') # 绘制边，两个坐标，即起始坐标和终点坐标
        plt.text(x, y, str(node.value), color='r', ha='center', va='center', fontsize=15, bbox=dict(facecolor='w', edgecolor='w', boxstyle='circle'))
        plot_tree(node.left, x-1, y-1, x, y)
        plot_tree(node.right, x+1, y-1, x, y)

def draw_tree(graph,root,index,pos, x, y):
    if root is None:
        return
    graph.add_node(index,label=root.value)
    pos.update({index:(x,y)})
    draw_tree(graph,root.left,index+1,pos,x-1,y-1)
    draw_tree(graph,root.right,index+1,pos,x+1,y-1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    node_list=to_list("[1,null,0,0,1]")
    root=create_binary_tree_from_list(node_list)
    print_tree(root)
    tree=nx.DiGraph()
    pos=dict()
    draw_tree(tree,root,0,pos,0,0)
    labels = nx.get_node_attributes(tree, 'label')
    nx.draw(tree, with_labels=True, labels=labels, node_color='white', node_size=800)
    plt.show()
