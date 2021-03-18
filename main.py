#data type 
print("Enter your favorite 2 digits number ");

num = input();



def check(z):
 if(len(z) == 2):
   x= int(z[0]);
   y = int(z[1]);
   result =str(x+y);
   print("The answer is "+result+".");
 else:
   print("Enter only 2 digits number");

check(num);

quit();