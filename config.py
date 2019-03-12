from sys import argv

# Please run the program as follow "python3.7 config.py pbject-name.txt private-ip.txt public-ip.txt
script, object_name, private_ip, public_ip = argv

# Open each file and reading it by lines - make sure you update the file with the nat and IP you need to generate the file. 
open_object = [i.strip() for i in open(object_name).readlines()]  # i is to retrieve every sentence from the file
open_private = [i.strip() for i in open(private_ip).readlines()]
open_public = [i.strip() for i in open(public_ip).readlines()]

print("Enter the filename: ")
name = input()
result = open("Result/" + name, "w") # To write the output in the new file

i = 1
c = 0 # using C to help count + 1 in for loop
for object in open_object:  # main file to write every output in new line
    r = "object network {} \n".format(object)

    for z in range (i):
        p = r +  " host {} \n".format(open_private[c + z])

        for x in range(i):
            pu = p + "nat (inside,outside) static {} \n".format(open_public[c + x]) + \
                 "access-list outside_access_in extended permit object-group Http_s_Ports any object {} \n".format(object) + \
                 "access-list outside_access_in extended permit icmp any object {} object-group ICMP_Access \n\n".format(object)


    c = c + i
    final = pu
    result.write(final)






