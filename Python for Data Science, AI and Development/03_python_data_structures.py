# Course 4
# Python for Data Science, AI & Development
# 3-Tuples

#Tuples

# Create your first tuple
tuple1 = ("disco",10,1.2 )
tuple1

# Print the type of the tuple you created
type(tuple1)

#Indexing

# Print the variable on each index
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

# Print the type of value on each index
print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))

# Use negative index to get the value of the last element
tuple1[-1]

# Use negative index to get the value of the second last element
tuple1[-2]

# Use negative index to get the value of the third last element
tuple1[-3]

# Concatenate two tuples
tuple2 = tuple1 + ("hard rock", 10)
tuple2

#Slicing

# Slice from index 0 to index 2
tuple2[0:3]

# Slice from index 3 to index 4
tuple2[3:5]

# Get the length of tuple
len(tuple2)

#Sorting

# A sample tuple
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)

# Sort the tuple
RatingsSorted = sorted(Ratings)
RatingsSorted

#Nested Tuple

# Create a nest tuple
NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))

# Print element on each index
print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])

# Print element on each index, including nest indexes
print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1])

# Print the first element in the second nested tuples
NestedT[2][1][0]

# Print the second element in the second nested tuples
NestedT[2][1][1]

# Print the first element in the second nested tuples
NestedT[4][1][0]

# Print the second element in the second nested tuples
NestedT[4][1][1]

#Quiz on Tuples

# sample tuple

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco") 
genres_tuple

#Find the length of the tuple, genres_tuple:

# Write your code below and press Shift+Enter to execute
print(len(genres_tuple))

#Access the element, with respect to index 3:

# Write your code below and press Shift+Enter to execute
print(genres_tuple[3])

#Use slicing to obtain indexes 3, 4 and 5:
# Write your code below and press Shift+Enter to execute
print(genres_tuple[3:6])

#Find the first two elements of the tuple genres_tuple:
# Write your code below and press Shift+Enter to execute
print(genres_tuple[0:2])

#Find the first index of "disco":
# Write your code below and press Shift+Enter to execute
print(genres_tuple.index("disco"))

#Generate a sorted List from the Tuple C_tuple=(-5, 1, -3):
# Write your code below and press Shift+Enter to execute
c_tuple = (-5,1,-3)
c_list = sorted(c_tuple)
c_list

# Course 4
# Python for Data Science, AI & Development
# 3-Dictionary


# Create the dictionary
Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
Dict

# Access to the value by the key
Dict["key1"]

# Access to the value by the key
Dict[(0, 1)]

# Create a sample dictionary
release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
release_year_dict

#Keys

# Get value by keys
release_year_dict['Thriller']

# Get value by key
release_year_dict['The Bodyguard']

# Get all the keys in dictionary
release_year_dict.keys()

# Get all the values in dictionary
release_year_dict.values()

# Append value with key into dictionary
release_year_dict['Graduation'] = '2007'
release_year_dict

# Delete entries by key
del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
release_year_dict

# Verify the key is in the dictionary
'The Bodyguard' in release_year_dict

#Quiz on Dictionaries

# Question sample dictionary
soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
soundtrack_dic

#a) In the dictionary soundtrack_dic what are the keys ?

# Write your code b
# Write your code below and press Shift+Enter to execute
soundtrack_dic.keys()

#b) In the dictionary soundtrack_dic what are the values ?

# Write your code below and press Shift+Enter to execute
soundtrack_dic.values() # The values are "1992" and "1977"

# a) Create a dictionary album_sales_dict where the keys are the album name and the sales in millions are the values.

# Write your code below and press Shift+Enter to execute
album_sales_dict = {"The Bodyguard":50, "Back in Black":50, "Thriller":65}

#b) Use the dictionary to find the total sales of Thriller:

# Write your code below and press Shift+Enter to execute
album_sales_dict["Thriller"]

#c) Find the names of the albums from the dictionary using the method keys():

# Write your code below and press Shift+Enter to execute
album_sales_dict.keys()

#d) Find the values of the recording sales from the dictionary using the method values:

# Write your code below and press Shift+Enter to execute
album_sales_dict.values()

# Course 4
# Python for Data Science, AI & Development
# 3-Sets

#Sets

# Create a set
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
set1

# Convert list to set
album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
album_set

# Convert list to set
music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", \
                    "progressive rock", "soft rock", "R&B", "disco"])
music_genres

#Set Operations

# Sample set
A = set(["Thriller", "Back in Black", "AC/DC"])
A

# Add element to set
A.add("NSYNC")
A

# Try to add duplicate element to the set
A.add("NSYNC")
A

# Remove the element from set
A.remove("NSYNC")
A

# Verify if the element is in the set
"AC/DC" in A

#Sets Logic Operations

# Sample Sets
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

# Print two sets
album_set1, album_set2

# Find the intersections
intersection = album_set1 & album_set2
intersection

# Find the difference in set1 but not set2
album_set1.difference(album_set2)

#You only need to consider elements in album_set1;
#all the elements in album_set2, including the intersection, are not included.

#The elements in album_set2 but not in album_set1 is given by:
album_set2.difference(album_set1)

#You can also find the intersection of album_list1 and album_list2,
#using the intersection method:

# Use intersection method to find the intersection of album_list1 and album_list2
album_set1.intersection(album_set2)  

#This corresponds to the intersection of the two circles:

#The union corresponds to all the elements in both sets,
#which is represented by coloring both circles:

#The union is given by:

# Find the union of two sets
album_set1.union(album_set2)

# Check if superset
set(album_set1).issuperset(album_set2)

# Check if subset
set(album_set2).issubset(album_set1)

# Check if subset
set({"Back in Black", "AC/DC"}).issubset(album_set1)

# Check if superset
album_set1.issuperset({"Back in Black", "AC/DC"})

#Quiz on Sets
#Convert the list ['rap','house','electronic music', 'rap'] to a set:
set(['rap','house','electronic music','rap'])

#Consider the list A = [1, 2, 2, 1] and set B = set([1, 2, 2, 1]), does sum(A) = sum(B)
A = [1, 2, 2, 1]  
B = set([1, 2, 2, 1])
print("the sum of A is:", sum(A))
print("the sum of B is:", sum(B))

#Create a new set album_set3 that is the union of album_set1 and album_set2:
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
album_set3 = album_set1.union(album_set2)
album_set3

#Find out if album_set1 is a subset of album_set3:
album_set1.issubset(album_set3)