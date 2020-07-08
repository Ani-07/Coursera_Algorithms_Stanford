# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 10:41:03 2020

@author: Anirudh Raghavan
"""
import random

def min_cut_algo(vertices, edges):

    k = len(vertices)
    
    random_edges = []
    
    while k > 2:
        
        n = len(edges)
        
        array = list(range(n))
        
        random_edge = random.sample(array,1)[0]
        
        random_edges.append(random_edge)
        
        contract_edge = edges[random_edge]
        
        edges.pop(random_edge)
        
        edges = [edge for edge in edges if edge != contract_edge]
        
        n = len(edges)
        
        for i in range(n):
            for j in [0,1]:
                if edges[i][j] == contract_edge[1]:
                    edges[i][j] = contract_edge[0]
                    edges[i].sort()
        
        
        vertices.remove(contract_edge[1])
        
        k = len(vertices)
    
    min_cut = len(edges)
    print(edges)
    return min_cut, random_edges


#Data Cleaning and Edges Implementation

file = open("kargerMinCut.txt", "r")

karger = file.readlines()
    
karger = [i.replace("\t", " ") for i in karger]

karger = [i.replace("\n", "") for i in karger]

karger_strip = [i.split(" ") for i in karger]

for i in karger_strip:
    i.pop(-1)



array_e = []


for i in karger_strip:
    vert = i[0]
    for j in i[1:]:
        edge = []
        edge.append(int(i[0]))
        edge.append(int(j))
        edge.reverse()
        
        if edge not in array_e :
            edge.reverse()
            array_e.append(edge)

array_v = list(range(1,201))

karger_min = []

for i in range(1000):
    array_e = []


    for i in karger_strip:
        vert = i[0]
        for j in i[1:]:
            edge = []
            edge.append(int(i[0]))
            edge.append(int(j))
            edge.reverse()
            
            if edge not in array_e :
                edge.reverse()
                array_e.append(edge)

    array_v = list(range(1,201))

    if i == 0:
        
        karger_cut = min_cut_algo(array_v, array_e)
        min_cut = karger_cut[0]
    else:
        karger_cut = min_cut_algo(array_v, array_e)
        
        if karger_cut[0] < min_cut:
            min_cut = karger_cut[0]
   
    karger_min.append(karger_cut)

min_cuts = [item[0] for item in karger_min]

min(min_cuts)

# TO DO

#Remove the contract edge correctly without adjusting edges array