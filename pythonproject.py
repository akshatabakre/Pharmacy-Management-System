# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 15:51:46 2022

@author: hp
"""

import pandas as pd
import matplotlib.pyplot as plt

def menu():
    
    print()
    print("-------------------------------------------------------")
    print("      PHARMACY MANAGEMENT SYSTEM")
    print("-------------------------------------------------------")
    print("     Press '1' for Reading file Stock")
    print("     Press '2' to Make an entry of New Medicine")
    print("     Press '3' to Delete Medicine details")
    print("     Press '4' to Update details of Medicine")
    print("     Press '5' to Show Records of Staff")
    print("     Press '6' to Add new Employee Record")
    print("     Press '7' to Find Maximum Salary of Staff")
    print("     Press '8' to Find Minimum Salary of Staff")
    print("     Press '9' for Sale Entry")
    print("     Press '10' to Show Horizontal bar chart between Medicine Name and Quantity")
    print("     Press '11' to Show Line Plot between Staff Members and Salary")
    print("     Press '12' to Show Information related to program")
    print("     Press any other number (excluding the above options) to Exit the program")
    print("-------------------------------------------------------")
    print("Note: Only numeric entries are accepted.")
    print("-------------------------------------------------------")
    print()
    print()
    
menu()
  


def option():
       
    opt=int(input('Enter your choice: '))    
      
    
    if opt==1:
                
                df=pd.read_csv("D:\\IP\\Stock.csv",index_col=0)
                print()
                print(df)
                print()
                print()
                menu()
                option()
        
        
        
    if opt==2:
                
                df=pd.read_csv("D:\\IP\\Stock.csv",index_col=0)
                print(df)
                a=int(input("Enter Batch_no.: "))
                b=(input("Enter Medicine Name: "))
                c=(input("Enter Date of Expiry: "))
                d=int(input("Enter Quantity: "))
                e=(input("Enter type of Medicine: "))
                f=int(input("Enter Price: "))
                df.loc[a]=[b,c,d,e,f]
                df.to_csv("D:\\IP\\Stock.csv")
                print(df)
                print()
                print()
                menu()
                option()



            
    if opt==3:
                
                print('Deleting Medicine Details') 
                df=pd.read_csv("D:\\IP\\Stock.csv",index_col=0)
                print(df)
                batchno=int(input("enter batch_no.: "))
                df.drop(batchno,axis=0,inplace=True)
                print("Medicine Deleted from Record")
                print()
                df.to_csv("D:\\IP\\Stock.csv")
                print(df) 
                print()
                print()
                menu()
                option()
        
        
    if opt==4:
                df=pd.read_csv("D:\\IP\\Stock.csv",index_col=0)
                print(df)
                a=int(input("Enter Batch_no. to be Updated: "))
                b=(input("Enter Medicine Name: "))
                c=(input("Enter Date of Expiry: "))
                d=int(input("Enter Quantity: "))
                e=(input("Enter type of Medicine: "))
                f=int(input("Enter Price: "))
                df.loc[a]=[b,c,d,e,f]
                print("Data successfully updated")
                df.to_csv("D:\\IP\\Stock.csv")
                print(df) 
                print()
                print()
                menu()
                option()
         
         
         
    if opt==5:
                 
                 print('Reading File Staff')
                 print()
                 print()
                 df=pd.read_csv("D:\\IP\\Staff.csv",index_col=0)
                 print(df)
                 print()
                 print()
                 menu()
                 option()
                 
         
         
         
    if opt==6:
                 
                 print()
                 print(df)
                 df=pd.read_csv("D:\\IP\\Staff.csv",index_col=0)
                 m=int(input("Enter Staff id: "))
                 n=(input("Enter Name: "))
                 o=int(input("Enter Age: "))
                 p=int(input("Enter Mobile no.: "))
                 q=int(input("Enter Salary: "))
                 df.loc[m]=[n,o,p,q]
                 df.to_csv("D:\\IP\\Staff.csv")
                 print(df)
                 print()
                 print()
                 menu()
                 option()


          
           

    if opt==7:
                
                df=pd.read_csv("D:\\IP\\Staff.csv",index_col=0)
                print(df)
                print()
                print('Highest Salary of Staff')
                print(df.Salary.max())
                print()
                print()
                menu()
                option()
           
    if opt==8:
                
                df=pd.read_csv("D:\\IP\\Staff.csv",index_col=0)
                print(df)
                print()
                print('Lowest Salary of Staff')
                print(df.Salary.min())
                print()
                print()
                menu()
                option()
          
          
    if opt==9:
              
              df=pd.read_csv("D:\\IP\\Bill.csv",index_col=0)
              g=(input('Enter Medicine Name:'))
              h=int(input('Enter Quantity:'))
              i=int(input('Enter MRP:'))
              j=int(input('Enter Mobile No.:'))
              k=input('Enter your name:')
              df.loc[g]=[h,i,j]
              df.to_csv("D:\\IP\\Bill.csv")
              bill=h*i
              print()
              print('Hello ',k,'  contact no.-',j)
              print('You have purchased ',h,' ',g,' and your bill is Rs.',bill)
              print()
              print()
              menu()
              option()
          
          
          
    if opt==10:
              
              print('Horizontal Bar Chart between Medicine and Quantity available in Stock')
              df=pd.read_csv("D:\\IP\\Stock.csv",index_col=0)
              print(df)
              x=df['M_name']
              y=df['Quantity']
              plt.title('Medicine Names and Quantity in Stock')
              plt.xlabel('Medicine Name')
              plt.ylabel('Quantity')
              plt.barh(x,y,color='b',edgecolor='m')
              plt.show()
              print()
              print()
              menu()
              option()
    
    
    if opt==11:
            
            print('Line Plot between Staff Members and their Salary')
            df=pd.read_csv("D:\\IP\\Staff.csv",index_col=0)
            print(df)
            x=df['Name']
            y=df['Salary']
            plt.title('Staff Members and Salary')
            plt.xlabel('Names')
            plt.ylabel('Salary')
            plt.plot(x,y,marker='X',ls='dashed',color='b')
            plt.show()    
            print()
            print()
            menu()
            option()
        
        
        
        
        
    if opt==12:
            
            print()
            print('This program is created by-')
            print('Roll No.         Name')
            print('12111            Akshata Bakre')
            print('12110            Akash Kumar Nirmalkar')
            print('under the guidance of our IP teachers.')
            print()
            print('We have used 3 csv files, namely-')
            print('1. Stock')
            print('2. Staff')
            print('3. Bill')
            print()
            print()
            menu()
            option()
   
    
    else:
       print('You exited the program.')
        
    


option()

    
    
    
    