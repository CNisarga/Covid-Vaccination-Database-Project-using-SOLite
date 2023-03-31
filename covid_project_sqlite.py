import sqlite3

import datetime


connection_obj = sqlite3.connect('vaccination_data.db')

cursor_obj = connection_obj.cursor()

connection_obj.execute('''CREATE TABLE IF NOT EXISTS AADHAAR_INFO (
 AADHAAR_NO INTEGER PRIMARY KEY,
 NAME TEXT NOT NULL,
 DATE_OF_BIRTH DATE NOT NULL,
 GENDER TEXT NOT NULL,
 ADDRESS TEXT  );''')


connection_obj.execute('''CREATE TABLE IF NOT EXISTS VACCINATION_INFO (
 AADHAAR_no INTEGER NOT NULL,
 VACCINATION_DATE DATE,
 DOSE_no INT,
 vaccination_site varchar(50),
 FOREIGN KEY (AADHAAR_no) references AADHAAR_INFO (AADHAAR_NO) );''')

connection_obj.execute('''INSERT INTO AADHAAR_INFO VALUES(12345678, 'Ram', '1990-02-04', 'M', 'Bangalore' );''')
connection_obj.execute('''INSERT INTO AADHAAR_INFO VALUES(23456789, 'Hanuman', '1986-07-11', 'M', 'Bangalore' );''')
connection_obj.execute('''INSERT INTO AADHAAR_INFO VALUES(34567891, 'Krishna', '1986-07-11', 'M', 'Mysore' );''')
connection_obj.execute('''INSERT INTO AADHAAR_INFO VALUES(45678912, 'Radha', '1986-07-11', 'F', 'Hassan' );''')
connection_obj.execute('''INSERT INTO AADHAAR_INFO VALUES(56789123, 'Laxman', '1986-07-11', 'M', 'Bangalore' );''')
connection_obj.execute('''INSERT INTO AADHAAR_INFO VALUES(67891234, 'Sita', '1986-07-11', 'F', 'Bangalore' );''')
connection_obj.execute('''INSERT INTO AADHAAR_INFO VALUES(78912345, 'Balram', '1986-07-11', 'M', 'Mysore' );''')
connection_obj.execute('''INSERT INTO AADHAAR_INFO VALUES(89123456, 'Suma', '1986-07-11', 'F', 'Mangalore' );''')
connection_obj.execute('''INSERT INTO AADHAAR_INFO VALUES(91234567, 'Lily', '1986-07-11', 'F', 'Tumkur' );''')
connection_obj.execute('''INSERT INTO AADHAAR_INFO VALUES(78965432, 'John', '1986-07-11', 'M', 'Tumkur' );''')
connection_obj.execute('''INSERT INTO AADHAAR_INFO VALUES(65437891, 'Aditya', '1986-07-11', 'M', 'Shivmogga' );''')
connection_obj.execute('''INSERT INTO AADHAAR_INFO VALUES(12356784, 'Divya', '1986-07-11', 'F', 'Darwad' );''')
connection_obj.execute('''INSERT INTO AADHAAR_INFO VALUES(54321678, 'Abhi', '1986-07-11', 'M', 'Udupi' );''')
connection_obj.execute('''INSERT INTO AADHAAR_INFO VALUES(45673216, 'Pooja', '1986-07-11', 'F', 'Kodagu' );''')
connection_obj.execute('''INSERT INTO AADHAAR_INFO VALUES(65478932, 'Ramya', '1986-07-11', 'F', 'Kolar' );''')

def check():       
        if num_doses == None or num_doses == 1 or num_doses == 2:
            print('Doses given: ', num_doses)
        


while True:

    AADHAAR_NO = input('Enter Aadhaar ID: ')

    cursor_obj.execute('''SELECT COUNT(*) FROM AADHAAR_INFO WHERE AADHAAR_NO = ?''',(AADHAAR_NO,))

    if cursor_obj.fetchone()[0]==0:
        print()
        print('AADHAAR_INFO not present for the given AADHAAR_NO.')
    
    else:
        cursor_obj.execute('''SELECT count(*) FROM VACCINATION_INFO WHERE AADHAAR_no = ?''',(AADHAAR_NO,))
        num_doses = cursor_obj.fetchone()[0]
    
        if num_doses >= 3:
            print('\nAlready dosed')
            
        
        else:
            
            check()
            
            print('Date:',end='')
            VACCINATION_DATE = print(datetime.datetime.now().date())
            
            while True:
                DOSE_no = int(input('Dose: '))
                if DOSE_no in [1,2,3]:
                    break
                else:
                    print('Please enter correct input\n')
                    
            vaccination_site = input("Enter vaccination site: ")
            print()
            cursor_obj.execute('''INSERT INTO VACCINATION_INFO 
                           (AADHAAR_no, VACCINATION_DATE, DOSE_no, vaccination_site)
                           VALUES (?, ?, ?, ?)''', 
                           (AADHAAR_NO, datetime.datetime.now().date(), DOSE_no, vaccination_site))
        
            cursor_obj.execute('SELECT * FROM VACCINATION_INFO WHERE AADHAAR_no = ?',(AADHAAR_NO,))
        
            result_vac = cursor_obj.fetchall()
            for record_vac in result_vac:
                print(record_vac)
            print("\n Vaccination information inserted successfully.\n")
            print("To insert vaccination info press 'enter'. \nTo view all present vaccination data type 'end'.")
    en = input()
    if en=='end':
        break
    
    
    
print('\n Vaccination Data \n')
cursor_obj.execute('''SELECT AADHAAR_INFO.AADHAAR_NO, AADHAAR_INFO.NAME, AADHAAR_INFO.ADDRESS, VACCINATION_INFO.VACCINATION_DATE, VACCINATION_INFO.DOSE_no, VACCINATION_INFO.vaccination_site FROM AADHAAR_INFO
                   left JOIN VACCINATION_INFO
                   ON AADHAAR_INFO.AADHAAR_NO = VACCINATION_INFO.AADHAAR_no
                   ''')

results = cursor_obj.fetchall()
for record in results:
    print(record)

connection_obj.commit()
cursor_obj.close()
connection_obj.close()

