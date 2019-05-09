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
    db.d403.insert( f0= 'hh4907', f1= '(4907)403')
    db.d403.insert( f0= 'pc4908', f1= '(4908)Oops, an error has occurred. Forbidden!')
    db.d403.insert( f0= 'pb4909', f1= '(4909)search ...')
    db.d403.insert( f0= 'aa4911', f1= '(4911)Return Dashboard')
    db.d403.insert( f0= 'aa4913', f1= '(4913)Return Website')
    db.commit()
#
