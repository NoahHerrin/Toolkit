import heapq

class Algorithm(object):
    def calculateShortestPath(self, vertextList, startVertex):
        queue = []
        startVertex.minDistance = 0
        heapq.heappush(queue,startVertex)

        while len(queue) > 0:
            actualVertex = heapq.heappop(queue)
            for edge in actualVertex.adjacenciesList:
                u = edge.startVertex
                v = edge.targetVertex
                newDistance = u.minDistance + edge.weight
                if newDistance < v.minDistance:
                    v.predecessor = u
                    v.minDistance = newDistance
                    heapq.heappush(queue,v)

    def getShortestPathTo(self, targetVertex):
        print("Shorest path to target is: ", targetVertex.minDistance)
        node = targetVertex
        path = []
        while node is not None:
            path.append(node.name)
            node = node.predecessor

        for i in range(len(path) - 1, 0, -1):
            print("{} -> ".format(path[i]),end="")
        print(targetVertex.name)
