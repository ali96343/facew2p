#
# table for controller: buttons
#

from gluon.contrib.populate import populate

db.define_table('dbuttons', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dbuttons.id ).count():
    populate(db.dbuttons, 5)
    db.commit()
#
