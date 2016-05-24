from collections import deque 

def answer(words):
    tree = getTree(words)
    uniques = set(tree)
    sorted = deque()

    def traverseNode(node):
        for edge in tree.get(node, []):
            alreadySorted = edge in sorted

            if alreadySorted: 
                continue

            uniques.discard(edge)
            traverseNode(edge)

        sorted.appendleft(node)

    while uniques: 
        traverseNode(uniques.pop()) 
   
    return "".join(sorted)

def getTree(words): 

    tree = {}

    while(len(words) > 1):
        current = words.pop(0)
        next = words[0]

        if current == next: continue

        for i in range( min(len(current), len(next)) ):
            if current[i] != next[i]:
                diffIndex = i
                earlyChar = current[i]
                laterChar = next[i]

                if earlyChar in tree:
                    if laterChar not in tree[earlyChar]:
                        tree[earlyChar].append(laterChar)
                else:
                    tree[earlyChar] = [laterChar]

                break 
        
    return tree 
