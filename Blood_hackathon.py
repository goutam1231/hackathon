import sys
import pandas as pd
print('1.Admin login\n''2.user login')
n=int(input())  

GroupA={'HOSPITAL_NAME':["shusrutha","sanjeevani","apollo","care","NRI","Mahindra"],
 "BRANCH_NAMES":["Hubli","Dharwad","jagadamba","Kolar","Hosur","Gajuwaka"],
  "DONORS":["Murali","chandra sekhar","praveen","Naveen","sravan","Anand"],
    "phone numbers":[9346346524,2385726375,2356576454,9283746574,3948576584,1324567653]
}
GroupB={'HOSPITAL_NAME':["Kala hospital","omni R K","Q1 hodspital","Indus","pinnacle","sagar durga"],
 "BRANCH_NAMES":["Madhurawada","Anakapalli",'tirupati','vijayawada','Gannavaram','TAdepalligudam'],
  "DONORS":["kattappa",'prabhas','Bahubali','saaho','Mahesh babu','allu arjun'],
    "phone numbers":[312452355,4635754457,9568458468,463548578,9568734784,9457495739]
}
GroupAB={'HOSPITAL_NAME':["K.G.H","surya hospital","prathama","vijetha hospital",'My cure',"7 hills"],
 "BRANCH_NAMES":["Dwaraka",'bellari','Mangalore','Hospete','Kottayam','Gadag'],
  "DONORS":['thalaiva','vijay','rajnikanth','tom cruise','tobias eaton','gana'],
   "phone numbers":[3465474568,7988454746,57563573436,9456734755,683562467,94593449749]
}
GroupO={'HOSPITAL_NAME':["visakha hospital","sankar foundation","simhadri hospital",'apex hospital','sum multispeciality','kanaka durga'],
 "BRANCH_NAMES":["allahabad","shiridi","pune",'Bhubaneshwar','cuttack','kharagpur'],
  "DONORS":['jack sparrow','barbossa','johnny depp','turner','mano','cornado'],
   "phone numbers":[46345224,23673546,215678578,358469873,9578967956,6858474688]
}
if n==1:
    print('For admin purposes')
    print("Enter username and password")
    a=input("username: ")                            #username is username
    b=input("password: ")                            #password is password
    if a=='username':
        if b=='password':
            print("Congratulations Admin successfully logged in")
        else:
            print("incorrect password")
            sys.exit()
    else:
        print("incorrect username and password")
        sys.exit()
    print("Blood Group A\n")
    print(pd.DataFrame(GroupA))
    print("\nBlood Group B\n")
    print(pd.DataFrame(GroupB))
    print("\nBlood Group O\n")
    print(pd.DataFrame(GroupO))
    print("\nBlood Group AB\n")
    print("Rare blood group")
    print("\n")
    print(pd.DataFrame(GroupAB))
 
else:
    print('For user purposes')
    print("Enter username and password")
    a=input("username: ")                            #username is username
    b=input("password: ")                            #password is password
    if a=='username':
        if b=='password':
            print("Congratulations user successfully logged in")
        else:
            print("incorrect password")
            sys.exit()
    else:
        print("incorrect username and password")
    print("For blood group A type A")
    print("For blood group B type B")
    print("For blood group O type O")
    print("For blood group AB type AB")
    d=input("Type Your Requirement:")
    if d=="A" :
        print(pd.DataFrame(GroupA))
    elif d=="B" :
        print(pd.DataFrame(GroupB))
    elif d=="O" :   
        print(pd.DataFrame(GroupO))
    elif d=="AB" :
        print(pd.DataFrame(GroupAB))
    sys.exit()
