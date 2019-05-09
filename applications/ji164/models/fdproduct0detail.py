#
# table for controller: product_detail
#

from gluon.contrib.populate import populate

db.define_table('dproduct0detail', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dproduct0detail.id ).count():
    populate(db.dproduct0detail, 5)
    db.commit()
#
