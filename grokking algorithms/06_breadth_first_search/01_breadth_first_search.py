from collections import deque

def person_is_seller(name):
    return name[-1] == 'm'

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    # this is how you keep track of which person you've searched before
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        # only search this person if you haven't already searched them
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                # marks this person as searched
                searched.add(person)
    return False

search("you")