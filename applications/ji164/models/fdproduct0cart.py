#
# table for controller: product_cart
#

from gluon.contrib.populate import populate

db.define_table('dproduct0cart', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dproduct0cart.id ).count():
    populate(db.dproduct0cart, 5)
    db.commit()
#
