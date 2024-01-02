name=" ayush kumar singh "
                 #stripping white space
print(name.strip()) # remove all the leading and trailing whitespaces from a string
print(name.lstrip())
print(name.rstrip())
                  #splitting string
    #Split strings into lists of smaller substrings with split().
namah=" ayush kumar singh "
print(namah.split())
                       #Joining List Elements Into a String
          #Join list element strings into single string in Python using join().
#reversing a string
om="Ayush"
print(om[::-1])
#uppercase and lowercase conversion
print(om.upper())#uppercase
print(om.lower())#lowercase
print(om.swapcase())#swapcase

#Checking for String Membership
a1="AYUSH"
a2="ayu"
print(a2 in a1) # by using in operator we know that membership

print(a1.lower())#change in lower case
print(a2.upper())#change in upper case
print(a2[0])#get vaalue on this index
print(a2.index("a"))#get the value of index
print(a2.replace("ayu","ashish"))#replace value of a2 variable

list3=[1,2,5,6,9,3,7,4]
print(max(list3)) #for maximum value
print(min(list3)) #for minimum value
print(sum(list3)) #for sum of list
print(len(list3))#for length of list


def sort(list3):
    pass


print(sort(list3))

