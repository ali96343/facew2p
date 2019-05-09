#
# table for controller: pages_forget
#

from gluon.contrib.populate import populate

db.define_table('dpages0forget', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dpages0forget.id ).count():
    populate(db.dpages0forget, 5)
    db.commit()
#
