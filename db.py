import mysql.connector as m1

class employee:

    db = m1.connect(
        host="localhost",
        user="root" ,
        password="@BHAY#$67&row",
        database='ak23'
        
        )
    cur=db.cursor()
    print(db)



    def create_emp(self,EmployeeId,EmployeeName,EmployeeDp,EmployeeNo):
        query="Insert into emp(EmployeeId,EmployeeName,EmployeeDp,EmployeeNo) values('"+EmployeeId+"','"+EmployeeName+"','"+EmployeeDp+"','"+EmployeeNo+"')"
        print(query)
        cur=self.db.cursor()
        cur.execute(query)
        self.db.commit()
        print("Employee successfully created")

    def show_Emp(self):
        query="select * from emp"
        cur=self.db.cursor()
        x=cur.execute(query)
        for x in cur:
            print("EmployeeId",x[0])
            print("EmployeeName",x[1])
            print("EmployeeDp",x[2])  
            print("EmployeeNo",x[3])   

    def delete_Emp(self,EmployeeId):
        query="delete from emp where EmployeeId=('"+EmployeeId+"')"
        cur=self.db.cursor()
        cur.execute(query)
        print("Employee successfully deleted")


    def update_Emp(self,EmployeeId,EmployeeName,EmployeeDp,EmployeeNo):
        query="update emp set EmployeeId='{}',EmployeeName='{}',EmployeeDp='{}',EmployeeNo='{}'".format(EmployeeId,EmployeeName,EmployeeDp,EmployeeNo) 
        print(query)
        cur=self.db.cursor()
        cur.execute(query)
        self.db.commit()
        print("Employee Succesfully Updated")


e1=employee()
e1.delete_Emp("1")
print(e1)
    


    






