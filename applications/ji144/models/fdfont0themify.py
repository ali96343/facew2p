#
# table for controller: font_themify
#

from gluon.contrib.populate import populate

db.define_table('dfont0themify', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dfont0themify.id ).count():
    populate(db.dfont0themify, 5)
    db.commit()
#
