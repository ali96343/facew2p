#
# table for controller: product_list
#

from gluon.contrib.populate import populate

db.define_table('dproduct0list', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dproduct0list.id ).count():
    populate(db.dproduct0list, 5)
    db.commit()
#
