def is_connected(node1,node2,G):
    """returns True if node1 and node2 are connected in G. Otherwise returns False
    Prec:G is a dictionary. node1 and node2 are keys in G"""
    to_visit=G[node1]
    visit=[node1]
    while(to_visit!=[]):
        cur_node=to_visit[0]
        visit.append(cur_node)
        to_visit=to_visit[1:]
        if cur_node==node2:
            return True
        for d in G[cur_node]:
            if d not in visit and d not in to_visit:
                to_visit.append(d)
    return False
G1={"A":["B"],"B":["A","C"],"C":["B"],"D":[]}
print(is_connected("A","B",G1))

"""def is_connected(node1,node2,G):
    to_visit=G[node1]
    visit=[node1]
    while(to_visit!=[]):
        index=len(to_visit)-1
        visit.append(to_visit[index])
        to_visit.pop()
        index=index-1
        for d in G[to_visit[index]]:
            if d not in visit:
                to_visit.append(d)
        if node2 in to_visit:
            return True
G1={"A":["B"],"B":["A","C"],"C":["B"],"D":[]}
print(is_connected("A","B",G1))"""          
        
    
