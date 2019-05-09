#
# table for controller: font_fontawesome
#

from gluon.contrib.populate import populate

db.define_table('dfont0fontawesome', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dfont0fontawesome.id ).count():
    populate(db.dfont0fontawesome, 5)
    db.commit()
#
