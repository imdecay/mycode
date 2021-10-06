#!/usr/bin/python3

# parse CSV file
loginfail = 0 # counter for fails
loginsuccess = 0 # counter for successes

# open the file for reading
with open("/home/student/mycode/credmaker/csv_users.txt") as cfile:

    # loop over the file
    for line in cfile:
        # pull out user first to make outfile
        User = line.split(",")[3]
        URL = line.split(",")[0]
        Proj = line.split(",")[1]
        Domain = line.split(",")[2]
        UserDomain = line.split(",")[4]
        Password = line.split(",")[5]
        verison = URL.split("/")[-2][-1]  # determine the version of the API
        
        
        
        #filename = print(f"admin.rc.{User}")
        filename = f"admin.rc.{User}"
        

        with open(filename, "a") as outFile:
            print(f"export OS_AUTH_URL={URL}", file=outFile)
            print(f"export OS_IDENTITY_API_VERSION={version}", file=outFile)
            print(f"export OS_PROJECT_NAME={Proj}", file=outFile)
            print(f"export OS_PROJECT_DOMAIN_NAME={Domain}", file=outFile)
            print(f"export OS_USERNAME={User}", file=outFile)
            print(f"export OS_USER_DOMAIN_NAME={UserDomain}", file=outFile)
            print(f"export OS_PASSWORD={Password}", file=outFile)
            #print(URL.split("/")[-2][-1])
                                

#http://controller:35357/v2/,myproject20,default,xavier,default,alta24
#http://controller:35357/v2/,myproject21,default,yammy,default,alta25
#http://controller:35357/v2/,myproject22,default,zorro,default,alta26
