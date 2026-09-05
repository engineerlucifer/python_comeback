#PYTHON : DAY 1
# case-sensitive language
#code=>translator(compiler, interpreter) => machine


# print("hello python");
# print("my name is lucifer");
# print("my age is 23");
# print(1+12);


# variable => is a container in which we can store data types.it directly stored in memory.
# if you want to add variable in print then it must like this print("this is: ",name);
# variable name can be A-Z,a-z,0-9, _ . thats it and note =>it must not start with any digit.

# name = "king";
# age = 23;
# worth = 25.70;
# age2 = age;

# print("person :",name + " has networth of :",worth);
# print(age2);
# print(type(name));
# print(type(age));
# print(type(worth));


# data types => 5 strings,boolean,integers,none,float. (25.99 is also comes in float not double),
# you can write string in any of these 3 format.
# name1= "sk";
# name2 = 'sk';
# name3 = '''sk''';
# print(name3);

##keywords for python;
## and , as , assert, break, class, continue, def , del , elif, else ,except, finally , False ,
# for , from, global , if ,import ,in , is , lambda, nolocal , None,not, or, pass , raise, return , True , try, with , while , yeild.

"""a = 10;
b = 20;
sum = a+b;
print(sum);"""


## types of operators;
# an operator is a symbol that performs a certain operation between operands
# arithmetic (+,-,*,/,%, **);
# comparision/relational (==,!=,>,<.>=,<=);
# assignment (=, +=,-=,);
#logical (not, and, or),

## conversion
# 2 ways => automatically(conversion) , casting(manual)

# a = 3;
# b = 4.545678;
# print(a+b); #automatically convert int to float.

# a=1;
# b= "2";
#type casting
# c=int(b);
# print(a+c);

### input/output;;
## we can also do typecasting before input int(input()); ,, float(input());;
# age = input("enter your age");
# print(type(age));
# print("my age is:",age); # we always get a string



# examples;;
#take input of 2num and write its sum;
# a = float((input("enter first no.")));
# b = float((input("enter 2nd no.")));
# print(a+b);

# take side of square and write its area;
# a = int((input("whats the side?")));
# area  = a*a;
# print(area);

# average of 2 no.
# a = float(input("enter any integer"));
# b = float(input("enter any integer"));
# average = (a+b)/2;
# print(average);

## take 2 input and show true or false accroding to which is larger.
a = int(input("enter a number"));
b = int(input("enter another number"));
print(a>b);











































