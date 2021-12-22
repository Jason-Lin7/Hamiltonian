    def getHamiltonian(self):
        """
        Returns a Hamiltonian circuit of type Walk for the graph if one exists,
        or None if none exists.
        """
        self.clearVisited() #Initially clears all visited
        tot_visit = 1 #Initializes total visit to 1
        walk_Distance = Walk(self.totalVertices()+1) #Distance of the walk
        vx = 0 #Starts at vertex 0
        self.tryVisiting(vx, tot_visit, walk_Distance) #visits unvisited vertices one by one to build hamiltonian
        if (self.totalV < 3): #If total vertex is less than 3
            return None #It is not a hamiltonian
        return walk_Distance #returns the walk distance
        
    def tryVisiting(self, vertex, totalvisited, Hamiltonian):
        """
        Recursive backtracking algorithm tries visiting adjacent unvisited vertices one by one
        building a Hamiltonian circuit along the way.

        Parameters:
            int vertex: vertex being visited for the first time
            int totalvisited: total number of vertices visited so far
            Walk Hamiltonian: Hamiltonian Walk built so far

        Side Effects:
            Hamiltonian is modified

        Returns True iff a Hamiltonian circuit has been found and False otherwise
        """
        Hamiltonian.addVertex(vertex) #This adds the initial vertex for hamiltonian
        self.visitedV[vertex]=True #This checks if the visited vertex is true
        visit_V=self.visitedV  #Keep track of visited vertex
        edge_zero=self.edges[vertex][0]  #Checks initial edge
        tot_V=self.totalV #Checks for total vertex
        edge_v=self.edges[vertex]  #Finds corresponding edge with vertex

        #Makes sure it doesn't go through previously visited edge
        if(tot_V==totalvisited):    
            if(edge_zero>0):
                Hamiltonian.addVertex(0)
                return True

        #Goes through each vertex, check each edge and visited vertex in 2-D array
        for i in range(tot_V):
            if edge_v[i]>0:
                if not visit_V[i]:
                    if(self.tryVisiting(i,totalvisited+1,Hamiltonian)): 
                        return True
                    else:
                        Hamiltonian.removeLastVertex()#Removes the last vertex added to the walk
                        
        visit_V[vertex]=False
        return False
       
