from models import models

models.db.create_all()

class CONTROLLER:
    def __init__(self):
        print "hello"
    def storeData(self, data_number):
        # check data is already present
        email = data_number["email"]
        name =  data_number["name"]
        number = str(data_number["number"])
        designation = data_number["designation"]
        data = models.EMPLOYEEDATA(name=name, email=email, number=number, designation=designation)
        try:
            models.db.session.add(data)
            try:
                models.db.session.commit()
            except:
                models.db.session().rollback()
        except:  # pylint: disable = W0702
            models.db.session.close()
        return True

    def deletedata(self, email):
 
        resp = models.EMPLOYEEDATA.query.filter_by(email=email).all()
        print resp
        if len(resp) == 0:
            return False
        models.EMPLOYEEDATA.query.filter_by(email=email).delete()
        models.db.session.commit()
        return True

    def editdata(self, data):
        email = data['email']
        del data['email']
        models.EMPLOYEEDATA.query.filter_by(
                        email=email).update(data)
        try:
            try:
                models.db.session.commit()
            except:
                models.db.session().rollback()
        except:  # pylint: disable = W0702
            models.db.session.close()
            return False
        return True

    def searchdata(self, email):
        resp = models.EMPLOYEEDATA.query.filter_by(email=email).all()

        print resp

        if len(resp) != 0:
            for item in resp:
                data = item.__json__()
            return data
        else:
            return False

