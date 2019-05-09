#
# table for controller: notification
#

from gluon.contrib.populate import populate

db.define_table('dnotification', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dnotification.id ).count():
    populate(db.dnotification, 5)
    db.commit()
#
