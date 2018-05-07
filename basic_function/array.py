
x = [1, 2, 3]
x.append([4, 5])
print (x)
#gives you: [1, 2, 3, [4, 5]]

#extend: Extends list by appending elements from the iterable.

x = [1, 2, 3]
x.extend([4, 5])
print (x)
#gives you: [1, 2, 3, 4, 5]


list = ['larry', 'curly', 'moe']
list.append('shemp')         ## append elem at end
list.insert(0, 'xxx')        ## insert elem at index 0
list.extend(['yyy', 'zzz'])  ## add list of elems at end
print list                   ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
print list.index('curly')    ## 2

list.remove('curly')         ## search and remove that element
list.pop(1)                  ## removes and returns 'larry'
print list  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']
#Common error: note that the above methods do not *return* the modified list, they just modify the original list.

list = [1, 2, 3]
print list.append(4)   ## NO, does not work, append() returns None
## Correct pattern:
list.append(4)
print list  ## [1, 2, 3, 4]
