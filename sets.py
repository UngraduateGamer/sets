# set is the collection of well defined distinct objects
s={1,2,51,7,8,9,1,2,5}
print(s)   # dont repeat elements print and its containts not order

sets={'rahul','friend',None,0,"Raghav"}
for values in sets:
    print(values)
    
    
# empty set

empty_Set=set()
print(type(empty_Set))

# empty dictionary

empty_Set={}
print(type(empty_Set))

# sets methods
S1={'africa','usa','delhi','india','japan','singapore'}
S2={'africa','india','China','Malaysia'}
S1=S1.union(S2) # union merge of two sets but the main sets dont change
print(S1)

S1={'africa','usa','delhi','india','japan','singapore'}
S2={'africa','india','China','Malaysia'}
S1.update(S2) # update function used for the union of two sets and then update the main sets
print(S1)

S1={'africa','usa','delhi','india','japan','singapore'}
S2={'africa','india','China','Malaysia'}
s=S1.intersection(S2) #intersection function used for the print the common in the two sets
print(s)

S1={'africa','usa','delhi','india','japan','singapore'}
S2={'africa','india','China','Malaysia'}
S1.intersection_update(S2) #intersection function used for the print the common in the two sets
print(S1)


S1={'africa','usa','delhi','india','japan','singapore'}
S2={'africa','india','China','Malaysia'}
S1.symmetric_difference(S2) # print not common in the two sets
print(S1)

S1={'africa','usa','delhi','berlin','india','japan','singapore'}
S2={'africa','india','China','Malaysia','berlin'}
S1.difference(S2) # print not common in the two sets
print(S1)

S1={'africa','usa','delhi','berlin','india','japan','singapore'}
S1.add('canada') # add elements in set 1
print(S1)

S1={'africa','usa','delhi','berlin','india','japan','singapore'}
S1.remove('usa') #remove usa in set 1. if they are not present throws an error
print(S1)

S1={'africa','usa','delhi','berlin','india','japan','singapore'}
S1.discard('Usa') #discard usa in set 1. if they are not present throws not error
print(S1)

S1={'africa','usa','delhi','berlin','india','japan','singapore'}
S2=S1.pop() #remove present elements randomly 
print(S1)
print(S2)

if 'africa' in S1:
    print("Yes africa is Present")
else:
    print ("africa  is not present")









