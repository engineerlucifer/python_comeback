##lists => store diff data types elements. just like array.
#it is mutable;
# marks = [0,1,2,3,4,5];
# print(marks);
# marks[2] = 10;
# print(type(marks));
# print(len(marks));
from token import STRING

## list slicing ;
# this is same as string slicing

## list methods;;
##Python ke list methods jaise append(), sort(), reverse(), insert() generally original list ko modify karte hain aur kuch return nahi karte, i.e. None.
# list = [1,2,3,4,5];
# list2 = list[0:3]
# print(list2);
# print(list[2:])
# list.append(10)

# print(list);
# list.sort();
# print(list);
# list.sort(reverse=True);
# print(list);
# list.reverse();
# print(list);
# list.insert(10,100)
# print(list);
# print(list[6]);


## tuples in python => same as list but immutable .

## single string ya single integer ko usi data type se treat krega.
# tup = (1,2,3,4,5);
# tup[1] = 2;(immutable)
# print(tup[1]);
# print(tup[2, ])



## tuple methods;;
# tup = (2,1,23);
# print(tup.index(23)) #element kaha hai
# print(tup);
# print(tup.count(2));


## examples;;
# name1 = (input("enter the movie name"));
# name2 = (input("enter the movie name"));
# name3 = (input("enter the movie name"));
# list = [name1,name2,name3];
# print(list);

#############
# ques = [1,2,3,2,2];
# copy1 = ques[-1:-3:-1]; ##-1 extra for -1 <--
# copy2 = ques[-3:-6:-1];
# ans = copy1+copy2;
# print(ans);
#
# if(ques == ans):
#     print("palindrome");
# else:
#     print("nothing")
# print(copy2);
# print(copy1)

### ques[::-1] =>reverse full list or we can use .reverse();;
# ques = [1, 2, 3, 2, 1];
# copyonly = ques.copy();
# if(ques == copyonly[::-1]):
#     print("palindrome")
# else:
#     print("nothing")



###
tup = ("c","d","a","a","b","b","a");
# print(tup.count("a"));
list = [tup[0:len(tup)]];
list.sort();
print(list);