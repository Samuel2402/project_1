from app import db, Users 
# from app import Users - as alternative 

db.drop_all()                      #- deletes existing ables 
db.create_all()                    #- re-populates ables 

test_user = Users(first_name='Grooty',last_name='Toot') # Example entry
db.session.add(test_user)           

db.session.commit()