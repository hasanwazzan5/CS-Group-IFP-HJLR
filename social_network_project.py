#social network project

'''
editors:
parts 1 & 2 by Raghad
part 3 by Leen & Raghad
part 4 by Hasan
parts 5 & 6 by Jiaxi
part 7 by Jiaxi & Hasan
'''

'''part 1, 2, & 3'''

class Graph:
    # dictionary
    dic = {}

# child class of graph
class member(Graph):
    def __init__(self, name, age, interest):
        self.name = name
        self.age = age
        self.interest = interest

        # add a new member
        self.freinds = {}
        self.addmember()

    # add a new member
    def addmember(self):
        if self.name in Graph.dic.keys():
            print(False)
        else:
            Graph.dic[self.name] = self.freinds

    # remove a member and its relationship
    def removemeber(self):
        del Graph.dic[self.name]
        for friends in Graph.dic.values():
            for friend in friends.copy():
                if friend == self.name:
                    del friends[self.name]

    # add a relationship
    def addrelationship(self, friend, weight):
        if self.name in Graph.dic.keys() and friend.name in Graph.dic.keys():
            self.freinds[friend.name] = weight

    # print all the dic
    def str(self):
        for i in Graph.dic.keys():
            print("the key is ", i)
            for j in Graph.dic[i].keys():
                print("the value is ", j)

        '''end of part 1, 2, & 3'''

        '''part 4'''

    def direct_friends(self):  # returns list of all friends
        list = []
        for friend in Graph.dic[self.name].keys():
            list.append(friend)
        return list

    def mutual_friends(self, friend2):  # returns a list of all mutual friends
        if isinstance(friend2, member):  # turns friend2 from object to the name of the friend
            friend2 = friend2.name
        list = []
        for friend in self.direct_friends():
            if friend in Graph.dic[friend2].keys():
                list.append(friend)
        return list

    def suggest_friends(self):  # list of all friends of friends
        suggestions = set()  # using a set for no duplicates
        for friend in self.direct_friends():
            for friendfriend in Graph.dic[friend].keys():  # searches friends friends
                if friendfriend not in Graph.dic[
                    self.name].keys() and friendfriend != self.name:  # makes sure "friends friend" is not already a friend or yourself
                    suggestions.add(friendfriend)
        return list(suggestions)

    def print_graph(self):  # directly print the dictionary
        return Graph.dic

'''end of part 4'''

'''part 5 & 6'''


# child class of graph
class NetworkAnalysis(Graph):
    def __init__(self):
        pass

    # find the shortest path
    def shortest_path(self, start_name, end_name):
        # check names
        if start_name not in Graph.dic and end_name not in Graph.dic:
            return "The start name and end name not found:", start_name, end_name

        elif start_name not in Graph.dic:
            return "The start name not found：", start_name

        elif end_name not in Graph.dic:
            return "The end name not found：", end_name

        visited = set()  # initialize collection
        queue = [(start_name, [start_name])]  # queue to store the current node and path

        while queue:
            (current_node, path) = queue.pop(0)  # pop the top element
            if current_node not in visited:
                visited.add(current_node)  # mark as visited
                if current_node == end_name:
                    return path, len(path) - 1
                for neighbor in Graph.dic.get(current_node, {}):  # update through the current node's neighbors
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))  # add the neighbor and path to the queue
        return "Path not found", None

    # find the degrees of separation
    def degrees_of_separation(self, start_name, end_name):
        visited = set()  # initialize collection
        queue = [(start_name, 0)]  # queue to store the current node and current degree of separation

        while queue:
            (current_node, current_degree) = queue.pop(0)  # pop the top element
            if current_node not in visited:
                visited.add(current_node)  # mark as visited
                if current_node == end_name:
                    return current_degree
                for neighbor in Graph.dic.get(current_node, {}):  # update through the current node's neighbors
                    if neighbor not in visited:
                        queue.append((neighbor, current_degree + 1))  # add the neighbor and path to the queue
        return "Path not found"

    # fine the most connected member
    def most_connected_members(self):
        max_connections = 0
        most_connected = []  # list of most connected members

        for member_name, friends in Graph.dic.items():
            num_connections = len(friends)  # number of connections for the current member
            if num_connections > max_connections:
                max_connections = num_connections
                most_connected = [member_name]
            elif num_connections == max_connections:
                most_connected.append(member_name)
        return most_connected, max_connections


# child class of graph
class CommunityDetection(Graph):
    def __init__(self):
        pass

    # detect the clusters
    def detect_clusters(self):
        visited = set()  # initialize collection
        clusters = []  # create a list to store all communities

        for member_name in Graph.dic.keys():
            if member_name not in visited:
                cluster = self.community_analysis(member_name, visited)
                clusters.append(cluster)

        return clusters

    # analysis communities
    def community_analysis(self, start_name, visited):
        queue = [start_name]  # create a queue
        cluster = []  # create a list to store members

        while queue:
            current_name = queue.pop(0)  # pop a node from the queue

            if current_name not in visited:
                visited.add(current_name)  # mark the current node as visited
                cluster.append(current_name)
                for neighbor in Graph.dic.get(current_name, {}):
                    if neighbor not in visited:
                        queue.append(neighbor)

        return cluster

    def formatted_clusters(self):
        clusters = self.detect_clusters()
        for idx, cluster in enumerate(clusters, start=1):  # use enumerate to number communities
            print("", f"Community {idx}: {cluster}")

'''end of part 5 & 6'''

'''part 7'''

class AdvancedInsights(Graph):
    def __init__(self):
        pass

    # Jiaxi Part for calculate the average degree
    def average_degree(self):
        all_degree = 0
        num_nodes = len(Graph.dic)
        for node in Graph.dic.keys():
            degree = len(Graph.dic[node])
            all_degree += degree
        if num_nodes > 0:
            average_degree = all_degree / num_nodes
            return average_degree
        else:
            return 0

    # Hasan Part
    def network_density(self):
        n = len(Graph.dic) #number of nodes
        total_possible_edges = (n * (n - 1)) #total edges formula
        total_edges = 0
        for relations in Graph.dic.keys(): #loop to get total edges
            edges = len(Graph.dic[relations])
            total_edges += edges
        network_density = total_edges / total_possible_edges #network density formula
        return network_density

    # Jiaxi Part
    def clustering_coefficient(self):
        clustering_coefficients = {}  # dic for coefficients

        for node in Graph.dic.keys():
            neighbors = list(Graph.dic[node].keys())  # get the list of friends
            num_neighbors = len(neighbors)  # get the amount of friends

            if num_neighbors < 2:  # according to the function
                clustering_coefficients[node] = 0  # if k=0 or k=1 coefficient will be meaningless
                continue

            edge_existed = 0  # create a value to show the edges existed

            # check the edges between neighbors
            for i in range(num_neighbors):  # friends loop
                for neighbor_index in range(i + 1,
                                            num_neighbors):  # friends' friends loop # just need to check the relationship between each pair of neighbors once both positive and negative are the same
                    neighbor1 = neighbors[i]  # friends
                    neighbor2 = neighbors[neighbor_index]  # friends' friends
                    if neighbor2 in Graph.dic[
                        neighbor1]:  # if neighbor2 is a neighbor of neighbor1 it means there is an edge between neighbor1 and neighbor2 so the edges need be added 1
                        edge_existed += 1

            if num_neighbors >= 2:
                current_coefficient = (edge_existed) / (num_neighbors * (num_neighbors - 1))  # function
                clustering_coefficients[node] = current_coefficient  # store every nodes' clustering_coefficients

        return clustering_coefficients

    def centrality_analysis(self):
        pass

    def degree_centrality(self, membername): #counts how many friends a member has
        degree_centrality = len(Graph.dic[membername])
        return degree_centrality

    def betweenness_centrality(self, membername):
        total_betweenness_centrality = 0
        for member1 in Graph.dic:
            for member2 in Graph.dic:
                if member1 != member2 and member1 not in Graph.dic[member2]:
                    if self.all_shortest_paths(member1, member2):
                        paths = self.all_shortest_paths(member1, member2)
                        print(paths)
                        betweenness_centrality = 0
                        for path in paths:
                            path.pop(0)
                            path.pop()
                            for name in path:
                                if name == membername:
                                    betweenness_centrality += 1
                        betweenness_centrality /= len(self.all_shortest_paths(member1, member2))
                        total_betweenness_centrality += betweenness_centrality
        return total_betweenness_centrality

    def all_shortest_paths(self, start_name, end_name):
        # check names
        if start_name not in Graph.dic and end_name not in Graph.dic:
            return "The start name and end name not found:", start_name, end_name

        elif start_name not in Graph.dic:
            return "The start name not found：", start_name

        elif end_name not in Graph.dic:
            return "The end name not found：", end_name

        queue = [(start_name, [start_name])]  # queue to store the current node and path
        shortest_paths = []  #store shortest path (or paths if there are more than one)
        min_length = float('inf') #starts with min length as infinity

        while queue:
            (current_node, path) = queue.pop(0)  # pop the top element
            if current_node == end_name:
                if len(path) < min_length:
                    min_length = len(path) #updates the min path lenght
                    shortest_paths = [path]
                elif len(path) == min_length:
                    shortest_paths += [path] #adds another equally long path

            for friend in Graph.dic.get(current_node, {}):  # update through the current node's neighbors
                if friend not in path: #prevents going back
                    queue.append((friend, path + [friend]))  # add the neighbor and path to the queue

        return shortest_paths if shortest_paths else None

'''end of part 7'''

'''code testing'''

# testing code Raghad and Leen section
p1 = member("rara", 19, "piano")
p2 = member("Lolo", 18, "reading")
p3 = member("meme", 17, "drawing")
p4 = member("shosho", 20, "piano")
p5 = member("fofo", 16, "reading")
p1.addrelationship(p2, 4)
p1.addrelationship(p3, 2)
p2.addrelationship(p1, 4)
p2.addrelationship(p3, 3)
p3.addrelationship(p1, 2)

#adding p4 relations
p2.addrelationship(p4, 1)
p4.addrelationship(p2, 3)
p3.addrelationship(p4, 5)
p4.addrelationship(p3, 2)

# testing Hasan section
print("Original graph:", p1.print_graph())
print(f"Direct friends of {p1.name}:", p1.direct_friends())
print(f"Mutual friends of {p1.name} and {p2.name}:", p1.mutual_friends(p2))
print(f"Friend suggestions for {p3.name}:", p3.suggest_friends())
p1.removemeber()
print(f"Graph after removing {p1.name}:", p1.print_graph())
print()
p1 = member("rara", 19, "piano")
p1.addrelationship(p2, 4)
p1.addrelationship(p3, 2)
p2.addrelationship(p1, 4)
p3.addrelationship(p1, 2)

# testing Jiaxi section
# find shortest path
path, length = NetworkAnalysis().shortest_path(p3.name, p1.name)
print(f"Separation between {p3.name} & {p1.name}:", "\n", "Path:", path, "\n", "Length:", length)
# calculate degrees of separation
print(f"Degree of separation between {p3.name} & {p1.name}:", NetworkAnalysis().degrees_of_separation(p3.name, p1.name))
# find most connected members
most_connected, max_connections = NetworkAnalysis().most_connected_members()
print("Most connected members:", most_connected)
print("Maximum number of connections:", max_connections)

print("Detected Communities:")  # print detected communities
CommunityDetection().formatted_clusters()

# testing P7-1 code
average_degree = AdvancedInsights().average_degree()
print("Average degree:", average_degree)

# testing P7-2 code
analysis = AdvancedInsights()
density = analysis.network_density()
print("Network Density:", density)

# testing P7-3 code
clustering_coefficients = AdvancedInsights().clustering_coefficient()
print("Clustering Coefficients:", clustering_coefficients)

#testing P7-4 code

#print("GOT EQUAL PATH", path, "Shortest Paths", shortest_paths)

print(f"Degree centrality of {p1.name}:", AdvancedInsights().degree_centrality(p1.name))
print(f"Betweenness centrality of {p3.name}", AdvancedInsights().betweenness_centrality(p3.name))
'''end of code testing'''