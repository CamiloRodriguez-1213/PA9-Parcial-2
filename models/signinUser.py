from flask import redirect
from werkzeug.security import check_password_hash

from config.database import db
cursor = db.cursor()

def User(email,passwordCod):
    print(passwordCod)
    try:
        cursor.execute("SELECT * FROM users WHERE email = '"+email+"'")
        myresult = cursor.fetchone()
        check_password_hash(myresult[3],passwordCod)
        if(check_password_hash):
            print("Autenticación correcta")
        else:
            print("Usuario incorrecto")
        
        print("Query Excecuted successfully")
    except:
        db.rollback()
        print("Error occured")
    
    
    
    