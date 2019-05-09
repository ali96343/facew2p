#
# table for controller: view_email
#

from gluon.contrib.populate import populate

db.define_table('dview0email', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dview0email.id ).count():
    populate(db.dview0email, 5)
    db.commit()
#
