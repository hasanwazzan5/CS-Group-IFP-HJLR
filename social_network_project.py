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

    ''''''
    '''code testing'''


# testing code Raghad section
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

'''end of code testing'''