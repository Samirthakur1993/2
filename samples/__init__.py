from string import digits # digit is the module
import os
def rename_files():
    for i in [1, 2, 3, 4, 5]:
        if i == 3:
            pass
            print("Pass when value is", i)
        print(i)




#    n=153
#    sum=0
#    while n>0:
#        r=n%10
#        sum+=r
#        n=n/10
#    print (sum)


#    for i in range(1,6):
#        for j in range(1,i+1):
#            print (i, end= '\t'),
#        print("\n")

#    file_names = os.listdir(r'C:\Users\HP\Downloads\prank')
#    #print("He says,\"Hi,how are you\"")

#    os.chdir(r"C:\Users\HP\Downloads\prank")
#    current_working_directory = os.getcwd()
#    print(current_working_directory)

#    for filename in file_names:
#        os.rename(filename, filename.translate(str.maketrans('', '', '0123456789')))
#    new_files_list = os.listdir(r"C:\Users\HP\Downloads\prank")

#    print(new_files_list)


rename_files()  # call to the function