#
# table for controller: product_payment
#

from gluon.contrib.populate import populate

db.define_table('dproduct0payment', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dproduct0payment.id ).count():
    populate(db.dproduct0payment, 5)
    db.commit()
#
