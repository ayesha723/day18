Subject={'bio':'' , 'chem':'' , 'phy':'' , 'isl' :''}

key = input("Enter the key for which you want retrieve value if it exist in dict i will assign otw error")

try:
    value=Subject[key]

except KeyError:
    print("The key you have entered doesnt exist in dict ")

if (key=='bio'):
    print(f"The value of key of bio is {10}")

elif (key=='chem'):
    print(f"The value of key of chem  is {20}")

elif (key=='phy'):
    print(f"The value of key of phy is {30}")

elif (key=='isl'):
    print(f"The value of key of isl is {40}")

else:
    print("Try agaian")

