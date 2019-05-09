#
# table for controller: review
#

from gluon.contrib.populate import populate

db.define_table('dreview', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dreview.id ).count():
    populate(db.dreview, 5)
    db.commit()
#
