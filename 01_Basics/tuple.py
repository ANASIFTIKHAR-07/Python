#  In this file we will learn and practice about tuple.

#  List is mutable while tuple is immutable. 
#  Tuple was generated to be a immutable datatype with list like features


superheroes = ("Batman", "Superman", "Spiderman", "Iron Man")

#  Just like list

superheroes[0] 
#  'Batman'

#  We can also the do the slicing, dicing on it and also the [:] operations

more_superheroes = ("Green Lantern", "Captain America")

all_superheroes = superheroes + more_superheroes
#  Can combine them like this via concatenate

if "Superman" in all_superheroes :
    print("Superman Is Here!")

# (superman, batman, spidey, iron man) = superheroes 
#  An operation which we can set to access tuple data by specific names
