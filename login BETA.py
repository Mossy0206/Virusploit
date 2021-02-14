import mysql.connector
mydb = mysql.connector.connect(user='root', password='Porthedland0206',
                               host='localhost', database='LOGININFO',
                               port=3306)





def sighnup():
    while True:

        usnam = input("enter your new username:")
        uspass = input("Enter you new password:")
        uspass1 = input("confirm your password:")
        email = input("enter your email address")
        if uspass == uspass1:
            details = "INSERT INTO users (username, email, passw) VALUES (%s, %s, %s)"
            TestLog = (usnam, uspass, email)
            cursor.execute(details, TestLog)
            mydb.commit()
            print("account made successfully")
            time.sleep(1)
            print("----------------------------------------LOADING----------------------------------------")
            time.sleep(1)
            print("---------------------------------------------------------------------------------------")
            time.sleep(1)
            print("---------------------------------------------------------------------------------------")
            time.sleep(1)
            print("---------------------------------------------------------------------------------------")
            time.sleep(1)
            break
        else:
            print("passwords do not match try again:")


def login():
    while True:
        print("please login")
        lognam = input("please enter your username or email:")
        logpass = input("please enter your password:")
        det = "SELECT * FROM users WHERE username OR email=(%s"
        nam = lognam
        cursor.execute(det, (nam,))
        passw = cursor.fetchall()
        for pas in passw:
            cpass = (pas[1])
            cnam = (pas[0])
        try:
            if lognam == cnam and logpass == cpass:
                print("Username is correct and password is correct you may continue.....")
                time.sleep(1)
                print("----------------------------------------LOADING----------------------------------------")
                time.sleep(1)
                print("---------------------------------------------------------------------------------------")
                time.sleep(1)
                print("---------------------------------------------------------------------------------------")
                break
        except UnboundLocalError:
            print(" username or password incorrect please try again:")