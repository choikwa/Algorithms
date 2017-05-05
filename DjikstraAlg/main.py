'''
Created on Nov 30, 2015

@author: thinkdoge
'''
GRIDL = 4
grid = []
import random
for i in range(GRIDL):
  tmp = []
  for j in range(GRIDL):
    tmp.append(random.randint(0, 3))
  grid.append(tmp)

class Node:
  def __init__(self, id, w, out):
    self.id = id
    self.weight = w
    self.out = out
    self.dist = -1
  def __repr__(self):
    return "(Node id:{0}, weight:{1}, dist:{2}, out-edges:{3})".format(self.id, self.weight, self.dist, self.out)
    
  def __str__(self):
    return self.__repr__()
  
nodelist = []
id = 0
for i,row in enumerate(grid):
  print(row)
  for j,entry in enumerate(row):
    newNode = Node(id, entry, [])
    if i < GRIDL-1:  # edge to below
      newNode.out.append((i+1)*GRIDL + j)
    if j < GRIDL-1:  # edge to right
      newNode.out.append(i*GRIDL + j+1)
    #if i < GRIDL-1 and j < GRIDL-1:   # diagonal edge to below right
    #  newNode.out.append((i+1)*GRIDL + j+1)
      
    nodelist.append(newNode)
    id+=1
    
for node in nodelist:
  print(node)
  
from queue import Queue

def Djikstra(nodelist):
  def findDist(node):
    for outEdge in node.out:
      outNode = nodelist[outEdge]
      sumDist = node.dist + outNode.weight
      if outNode.dist == -1:
        outNode.dist = sumDist
      else:
        if sumDist < outNode.dist:
          outNode.dist = sumDist
      
  node = nodelist[0]
  node.dist = node.weight
  
  # BFS
  Q = Queue()
  Q.put(node.id)
  while not Q.empty():
    node = nodelist[Q.get()]
    findDist(node)
    print(node.id, "pushing", node.out, "queue", Q.queue)
    for outId in node.out:
      if outId not in Q.queue:
        Q.put(outId)

Djikstra(nodelist)

print("------------------------------------------")
for node in nodelist:
  print(node)

print("------------------------------------------")
for i in range(GRIDL):
  ss = ""
  for j in range(GRIDL):
    ss += str(nodelist[i*GRIDL+j].weight).rjust(2) + ","
  ss = ss[:-1]
  print(ss)
  
print("------------------------------------------")
for i in range(GRIDL):
  ss = ""
  for j in range(GRIDL):
    ss += str(nodelist[i*GRIDL+j].dist).rjust(2) + ","
  ss = ss[:-1]
  print(ss)
  
def findReverseDigraph(nodelist):
  root = nodelist[0]
  rnodelist = []
  for node in nodelist:
    tmp = Node(node.id, 0, [])
    rnodelist.append(tmp)
  for node in nodelist:
    for outEdge in node.out:
      inList = rnodelist[outEdge].out
      if outEdge not in inList:
        inList.append(node.id)
  return rnodelist

print("------------------------------------------")
rnodelist = findReverseDigraph(nodelist)
for rnode in rnodelist:
  print(rnode)