#from __init__ import      #db, Countries, Cities     #db, Users 
## from app import Users - as alternative 

#db.drop_all()                      #- deletes existing ables 
#db.create_all()                    #- re-populates ables 

############################# latest ###########################################################

from my_project.app import db

db.drop_all() 
db.create_all()

###################### old - Cities + Countries #####################################################

#UK = Countries(name = 'United Kingdom') #Add example to countries table
#db.session.add(UK)
#db.session.commit()


#ldn = Cities(name='London', country = UK)
#mcr = Cities(name='Manchester', country = Countries.query.filter_by(name='United Kingdom').first())

#db.session.add(ldn)
#db.session.add(mcr)

####################### old - Users #####################################################

##test_user = Users(first_name='Grooty',last_name='Toot') # Example entry
##db.session.add(test_user)           

db.session.commit()