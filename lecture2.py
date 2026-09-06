# string study and then conditional statements
# string is data type that stores characters;
# + -> means concatenation (adding 2 strings)
# str1 = "this is king raza";
# str2 = "your's king ,";
# print(str2, str1);

# str1 = "this is me\nand python";
# print(str1);

# str2= "hello ji";
# print(len(str2)); # count with 1 not 0;
# str1= "hello";
# str2 = "ji";
# str3 = str1 + " "+ str2;
# print(str3);



#[] character of string;
# str5 = "new world";
# print(str5[5]);
#
# str5[0] = "W";
## error , strings are immutable;
# print(str5);


## slicing =>accessing some part of strings
## indexing hai toh wahi 0 se start hogi.
# str = "engineer raza";
# str1 = str[1:4];
# str2 = str[0:5];
# #both are same;
# str3 = str[:5];
#
# str4 = str[1:len(str)];
# #both are same
# str5 = str[1: ];
#
# print(str3);
# print(str5);

###slicing but from negative
# str = "qwerty" =>-6,-5,-4,-3,-2,-1,
# str10 = "RAZA KING";
# print(str10[-4:len(str10)])


## string functions;;
# str  = "i am coder raza";
# print(str)
# # print(str.endswith("er"));
# # print(str.capitalize());
# print(str.replace("raza", "king"));
# # print(str.find("coder"));
# # print(str.count("am"));
# print(str)

### examples;
#take user name and write its length;
# str1 = str(input("enter your name pls: "));
# print(len(str1));


# occurences;
# STR = "$ $123ufhwefh";
# print(STR.count("$"));
# print(STR.find("$"));


#########
##conditional statements;;
# age = 3;
# if(age>=18) :
#     print("valid");
# elif(age>=16):
#     print("teenage");
# else:
#     print("underage");


## number odd or even;
# number = int(input("enter the number"));
# if(number%2==0):
#     print("even");
# else:
#     print("odd")


#greatest of 3 number;
# no1 = input("enter 1 no");
# no2 = input("enter 2 no");
# no3 = input("enter 3 no");
# if(no1>no2 and no1>no3):
#     print("no1 is greatest")
# elif(no2>no1 and no2>no3):
#     print("2nd is greatest number")
# else:
#     print("3rd one is great");


## multiple of 7 or not?

number = int(input("enter your number"));
if(number%7==0):
    print("multiple of 7")
else:
    print("not multiple of 7")






























