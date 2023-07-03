from datetime import datetime
import pytz

now=datetime.now(pytz.timezone('Asia/Kolkata'))

users=[]
user1=[]
availablehouse=[]
request=[]
access=[]
history=[]
class homeapp:
    def __init__(self,userid:int,name:str,email:str,password:str,phn:int,gender:chr,role:str):
        self.userid=userid
        self.name=name
        self.email=email
        self.password=password
        self.phn=phn
        self.gender=gender
        self.role=role
    def hardcoded(self):
        users.append(self)
        
    def validateuser(self):
        self.validation=0
        self.useremail=input("Email: ")
        self.userpassword=input("password: ")
        for user in users:
            
            if user.email==self.useremail and user.password==self.userpassword:
                user1.append(user)
                self.validation=1
        if self.validation:
             self.welcomeuser() 
             
        else:
            print("Invalid details")
            self.validateuser()
        
    def welcomeuser(self):
            print("Loggin successful")
            print("Welcome user",user1[-1].name)

class house:
    def __init__(self,houseid,ownerid,location_id,location,typ,rent):
        self.houseid=houseid
        self.ownerid=ownerid
        self.location_id=location_id
        self.location=location
        self.typ=typ 
        self.rent=rent
    
    def hardcodedhouse(self):
       
        availablehouse.append(self)
    
    def showhouses(self):
        self.count=0
        location={1:'tambaram',2:'tnagar',3:'marina'}
        for i in location:
            print(location[i],i)
        c=int(input("Enter the location id of house: "))  
        for hous in  availablehouse:
            if hous.location_id==c:
                self.count=1 
                print("House id",hous.houseid)
                print('Owner id',hous.ownerid)
                print('Type',hous.typ)
                print('Rent',hous.rent)
                print('-------------------------')
                
        if not(self.count):
            print("No house avaliable near ",location[c])
    def bookhouse(self):
        self.avaliable=0
        n=int(input("ENter the location id "))
        m=int(input("Enter the house id "))
        for i in availablehouse:
            if i.location_id==n and i.houseid==m:
                self.avaliable+=1 
                request.append({'House_id':n,'Owner_id':i.ownerid,'Tenet_id':user1[-1].userid})
                break 
        if self.avaliable==0:
            print("Invalid ")
            self.bookhouse
    def seeacces(self):
        print(request)
        self.count=0
        while request!=[]:
            i=request[0]
            
            if i['Owner_id']==user1[-1].userid:
                print("User id ",i['Tenet_id'],'has requested to book your home',i['House_id'])
                if self.count<1:
                    s=input("Accept/decline request")
                    if s=='a':
                        self.count+=1
                        access.append({'Tenet_id':i['Tenet_id'],'House_id':i['House_id'],'Status':'Approved'})
                        request.remove(i)
                        print(request)
                        print(access)
                        self.count+=1 
                    else:
                        access.append({'Tenet_id':i['Tenet_id'],'House_id':i['House_id'],'Status':'Declined'})
                        request.remove(i)
                        print(access)
                else:
                    print(access) 
                    access.append({'Tenet_id':i['Tenet_id'],'House_id':i['House_id'],'Status':'Declined'})
                    request.remove(i)
                    
    def granted_rejected(self):
        for i in access:
            if i['Tenet_id']==user1[-1].userid:
                if i['Status']=='Declined':
                    print("Your request has been declined")
                    access.remove(i)
                else:
                    print("Your status has been accepted")
                    print("Proceed with payment to confirm your booking")
                    self.n=[]
                    self.n.append(i)
                    self.payment()
                    
    
        
    def payment(self):
        history=[]
        s=""
        self.paymentid=2
        self.paymentmethd='card'
        if self.paymentmethd=='card':
            self.cardno=input("card no")
            self.cvv=input("Enter cvv")
            self.expirydate=input("Enter cvv")
            payment="Successful"
            if payment=='Successful':
                self.paymentid+=1
                s+=str(user1[0].userid)+','
                s+=str((self.n[0])['House_id'])+','
                time=now.strftime('%H:%M:%S')
                date=now.strftime('%y-%m-%d')
                s+=str(time)+','
                s+=str(date)+','
                history.append(s)
                
                print("House booked")
                access.remove(self.n[0])
                for h in availablehouse:
                    d=(h.houseid)
                    c=((self.n[0])['House_id'])
                    if d==c:
                        availablehouse.remove(h)
        print(history)
    def see_history(self):
        print(history)
        for i in history:
            for j in i.split(','):
                print(j)
            
                

if __name__=="__main__":
    app=homeapp(1,'yoga','1','1',9876454636,'F','owner')
    app.hardcoded()
    app1=homeapp(2,'sanjay','2','2',8907654321,'M','tenet')
    app1.hardcoded()
    app2=homeapp(3,'sanjay','3','3',8907654321,'M','tenet')
    app2.hardcoded()
    while(True):
        
        
        app.validateuser()
        
        if user1[-1].role=='owner':
                houses=house(None,None,None,None,None,None)
                print("1. Add home ")
                print("2. See Request")
                print('3. Booking history')
                choice=int(input())
                if choice==1:
                    houses=house(1,1,1,'tambaram','2Bhk',15000)
                    houses.hardcodedhouse()
                    houses=house(2,1,1,'tambaram','1Bhk',10000)
                    houses.hardcodedhouse()
                    houses=house(2,2,2,'tnagar','2BHK',20000)
                    houses.hardcodedhouse()
                elif choice==2:
                    
                    houses.seeacces()
                elif choice==3:
                    houses.see_history()
                    
                    
                    
        else:
                print('1.See home')
                print('2.Book a home')
                print('3.Check status')
                print('4. Booking history')
                choice=int(input())
                houses=house(None,None,None,None,None,None)
                if choice==1:
                    houses.showhouses()
                elif choice==2:
                    houses.bookhouse()
                elif choice==3:
                    houses.granted_rejected()
                elif choice==4:
                    houses.see_history()
        
        
