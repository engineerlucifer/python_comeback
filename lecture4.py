# dictionaries => key:value  , just like object
# unordered , mutable, no duplicate;

# dict = {
#     "name" : "raza",
#     "age" : 23,
#     "graduation" : True
# }
# dict["cgpa"] = 9.50; ## to add new key
# print(dict);
# print(dict["age"])

## nested dictionaries;;
# student = {
#     "name" : "king raza",
#     "score" : {
#         "phy" : 89,
#         "math" : 90
#     }
# }

# print(type(student["score"]));
# student["score"]["phy"] = 100;
# print(student)


## dictionary methods;
# .keys() => return all keys;
# .values() => return all values;
# .items() => return all key value as tuples () form;
# .get("key") => return key according to value;
# .update(newDict) => insert item in dictionary or update any thing ;;

# student = {
#     "name" : "king raza",
#     "score" : {
#         "phy" : 89,
#         "math" : 90
#     }
# }

# print(student.keys());
# print(student.values());
# print(student["score"].values());  # for nested loop
# print(student.items())
# print(student.get("name"))
# student.update({"name" : "raza king" , "age" : 23});
# print(student)



######## set in python;;
# set is collection of unordered items;
## unique and immutable

# nums = {1,2,3,4,5,5,5,};
# print(nums);

## set methods;
# nums.add("hello ji"); # add new value
# nums.remove(5); # remove a element
# nums.clear(); # all elements remove
# nums.pop(); # remove a random element

# print(nums);



## union and intersection;;
# sets = {5,4,3,2,1};
# sets2 = {10,3};
# print(sets.union(sets2))
# print(sets.intersection(sets2))

## examples;;;
# dict = {
#     "table" : ["a piece of furniture" , "list of facts and figures"],
#     "cat" : "a small animal"
# }

# subjects = {"python" , "java","c++","python","javascript","java","python","java","c++","c"};
# print(len(subjects));






## subject wise marking ;
# marks1 = float(input("enter marks of  math : "));
# marks2 = float(input("enter marks of  chem : "));
# marks3 = float(input("enter marks of  phy : "));
# dict = {};
# dict.update({"math" : marks1, "chem" : marks2, "phy" : marks3});
# print(dict);


#
# sets12 = {int(9),float(9.0)}; ## will fail
# sets13 = {9,"9.0"};
# print(sets13);
##or
# sets14 = {
#     ("float",9.0),
#     ("int", 9)
# }
# print(sets14);




































































































































