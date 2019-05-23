#
# table for controller: X403
#

from gluon.contrib.populate import populate

db.define_table('d403', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.d403.id ).count():
    db.d403.insert( f0= 'hh4733', f1= '(4733)403')
    db.d403.insert( f0= 'pc4734', f1= '(4734)Oops, an error has occurred. Forbidden!')
    db.d403.insert( f0= 'pb4735', f1= '(4735)search ...')
    db.d403.insert( f0= 'aa4737', f1= '(4737)Return Dashboard')
    db.d403.insert( f0= 'aa4739', f1= '(4739)Return Website')
    db.commit()
#
