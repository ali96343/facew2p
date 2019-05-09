#
# table for controller: file_manager
#

from gluon.contrib.populate import populate

db.define_table('dfile0manager', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dfile0manager.id ).count():
    populate(db.dfile0manager, 5)
    db.commit()
#
