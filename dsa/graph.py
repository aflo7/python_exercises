# from collections import deque

# graph = {}
# graph["you"] = ["bob", "alice", "claire"]
# graph["alice"] = ["anuj", "peggy"]
# graph["anuj"] = ["paul", "jordan"]
# graph["bob"] = []
# graph["claire"] = []
# graph["peggy"] = []
# graph["paul"] = []
# graph["jordan"] = []

# search_queue = deque()
# search_queue += graph["you"]


# def person_sells_mangoes(p):
#     if (p) == "anuj":
#         return True
#     return False


# def directed_graph_bfs():
#     # search queue at the start is bob, alice, and claire
#     while search_queue:  # while the queue is not empty (first in first out)
#         person = search_queue.popleft()
#         if person_sells_mangoes(person):
#             print(person, "sells mangoes")
#             return True
#         else:
#             search_queue += graph[person]
#     return False


# def undirected_graph_bfs(
#     person,
# ):  # keep an array "searched", which keeps track of people that have already been searched.
#     search_queue = deque()
#     search_queue += graph[person]
#     searched = []
#     while (
#         search_queue
#     ):  # while the queue isn't empty... (if it's empty and you still haven't found a mango seller, then return false)
#         curr = search_queue.popleft()  # pop the first person off the queue
#         if not curr in searched:
#             if person_sells_mangoes(curr):
#                 print("found a mango seller!", curr)
#                 return True
#             else:
#                 searched.append(curr)
#                 search_queue += graph[curr]
#     return False  # no mango sellers were found


# undirected_graph_bfs("you")


states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"]) 
stations = dict()
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])
final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    
    
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
              
    states_needed -= states_covered
    final_stations.add(best_station)
