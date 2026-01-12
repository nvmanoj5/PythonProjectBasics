str = "Mridhu Sree"
str2 = "Manoj"
str3 = "Sushmi"
str4 = "Mridhu Sree"
str5 = "Sree"
str6 = " Mridhu Sree "
str7 = " Mridhu Sree"
str8 = "Mridhu Sree "


print(str[1]) #r

print(str2[0:4]) #mano

print(str2+str3) #ManojSushmi

print(str in str4) #full string check

print(str5 in str)  #contains

var = str.split(" ")  #split using empty space
print(var)
print(var[0])

print(str6.strip())   #removing white spaces in front and back

print(str7.lstrip())  #remvoing front white space

print(str8.rstrip()) #remvoing back white space