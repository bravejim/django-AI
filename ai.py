"""
Uniform Cost Search Implementation using PriorityQueue

Map and input taken from
http://www.massey.ac.nz/~mjjohnso/notes/59302/l04.html

Author: Jayesh Chandrapaal
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
		node = queue.get() #ambil cost dan list kota saat ini
		current = node[1][len(node[1]) - 1] #ambil kota terakhir yang dikunjungi pada queue
		
		if end in node[1]: #jika node tujuan ada #jika kota tujuan sudah dikunjungi
			print("Path found: " + str(node[1]) + ", Cost = " + str(node[0])) #print list kotanya, dan costnya
			break#keluar dr transversal
		 
		cost = node[0] #ambil cost saat ini
		for neighbor in graph[current]:#untuk tetangga2 dari kota terakhir yang dikunjungi
			temp = node[1][:]#ambil list kota yang telah dikunjungi hingga saat ini
			temp.append(neighbor)#tambahkan dengan kota tetangga kota terakhir
			if(neighbor not in visited):	queue.put((cost + graph[current][neighbor], temp))#masukkan ke queue
			visited.append(neighbor)
	
def readGraph():
	lines = int( input() ) #masukkan jumlah baris
	graph = {} #deklarasi graph
		
	for line in range(lines):
		line = input() #baca input 1 baris, masukin ke line
					 
		tokens = line.split() #pisahkan input yg dibaca berdasar spasi
		node = tokens[0] #simpan asal kota kedalam node			
		graph[node] = {} #kosongkan hubungan graf yang dimulai dari kota pada node
		 
		for i in range(1, len(tokens) - 1, 2):
			# print(node, tokens[i], tokens[i + 1])
			# graph.addEdge(node, tokens[i], int(tokens[i + 1]))
			graph[node][tokens[i]] = int(tokens[i + 1]) #hubungkan kota node dengan kota pada tokens[i] dengan jarak tokens[i+1]
	return graph #kembalikan graph gabungan

def main():
	graph = readGraph()#baca graph dr input
	search(graph, 'Arad', 'Bucharest')#cari arad ke bucharest
    
if __name__ == "__main__":
	main()
