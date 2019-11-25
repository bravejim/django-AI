"""
Uniform Cost Search Implementation using PriorityQueue

Map and input taken from
http://www.massey.ac.nz/~mjjohnso/notes/59302/l04.html

Author: Jayesh Chandrapal
Version: 1.0
"""

import queue as Q

def search(graph, start, end):
    if start not in graph:
        raise TypeError(str(start) + ' not found in graph !')
        return
    if end not in graph:
        raise TypeError(str(end) + ' not found in graph !')
        return
       
    visited = []
   
    queue = Q.PriorityQueue()
    queue.put((0, [start]))
    
    visited.append(start)
    
    while not queue.empty():
        node = queue.get()
        current = node[1][len(node[1]) - 1]
        print(current)
        if end in node[1]:
            print("Path found: " + str(node[1]) + ", Cost = " + str(node[0]))
            break
        
        cost = node[0]
        for neighbor in graph[current]:
            temp = node[1][:]
            temp.append(neighbor) 
            if(neighbor not in visited):   queue.put((cost + graph[current][neighbor], temp)) 
            visited.append(neighbor)
        
def readGraph():
    lines = int( input() )
    graph = {}
    
    for line in range(lines):
        line = input()
            
        tokens = line.split()
        node = tokens[0]
        graph[node] = {}
        
        for i in range(1, len(tokens) - 1, 2):
            # print(node, tokens[i], tokens[i + 1])
            # graph.addEdge(node, tokens[i], int(tokens[i + 1]))
            graph[node][tokens[i]] = int(tokens[i + 1])
    return graph

def main():
    graph = readGraph()
    search(graph, 'DeliSerdang', 'Pekanbaru')
    
if __name__ == "__main__":
    main()
    
"""
Sample Map Input:

22
DeliSerdang TebingTinggi 82 SerdangBedagai 51
SerdangBedagai DeliSerdang 51 TebingTinggi 35
TebingTinggi DeliSerdang 82 SerdangBedagai 35 BatuBara 58 PematangSiantar 47
BatuBara TebingTinggi 58 Asahan 66 
PematangSiantar TebingTinggi 47 TobaSamosir 126
TobaSamosir PematangSiantar 126 TapanuliUtara 96
Asahan BatuBara 66 TanjungBalai 32 LabuhanBatuUtara 81
TapanuliUtara TobaSamosir 96 TapanuliSelatan 106
TanjungBalai LabuhanBatuUtara 110 Asahan 32
TapanuliSelatan TapanuliUtara 106 PadangLawas 133
LabuhanBatuUtara TanjungBalai 110 LabuhanBatu 108 Asahan 81
LabuhanBatu LabuhanBatuUtara 108 LabuhanBatuSelatan 96
PadangLawas TapanuliSelatan 133 PadangLawasUtara 28
PadangLawasUtara PadangLawas 28 MandailingNatal 162
LabuhanBatuSelatan LabuhanBatu 96 RokanHilir 99 RokanHulu 189
MandailingNatal RokanHulu 365 PadangLawasUtara 162
RokanHulu LabuhanBatuSelatan 189 Kampar 106 MandailingNatal 365
RokanHilir LabuhanBatuSelatan 99 Bengkalis 213
Bengkalis RokanHilir 213 Siak 131
Kampar Pekanbaru 87 RokanHulu 106
Siak Bengkalis 131 Pekanbaru 91
Pekanbaru Siak 91 Kampar 87

"""
