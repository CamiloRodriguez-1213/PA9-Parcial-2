from config.database import db
from flask import flash,session
from models import createNewImage
from datetime import datetime
import time
from PIL import Image
cursor = db.cursor()
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def verifyExtend(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def uploadImage(nameProduct,fileProduct):
    try:
        if fileProduct and verifyExtend(fileProduct.filename):
            tiempo = str(time.time())
            image = Image.open(fileProduct)
            format = (image.format).lower()
            image.save('./static/images/'+tiempo+'.'+format)
            route = (tiempo+'.'+format)
            print(route)
            user = session['token']
            if createNewImage.setNewImage(nameProduct,route,user):
                    flash("La imagen ha sido guardada", "good")
            else:
                flash("Ha habido un error al subir la imagen", "error")
                flash("Vuelve a intentarlo", "error")
            #convertir = datetime.fromtimestamp(tiempo)
        else:
            flash('Tipo de archivo no admitido','error')
    except:
        print("Error occured in uploadImage")