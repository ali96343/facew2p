#
# table for controller: X500
#

from gluon.contrib.populate import populate

db.define_table('d500', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.d500.id ).count():
    db.d500.insert( f0= 'hh4922', f1= '(4922)500')
    db.d500.insert( f0= 'pc4923', f1= '(4923)Oops, an error has occurred. Internal server error!')
    db.d500.insert( f0= 'pb4924', f1= '(4924)search ...')
    db.d500.insert( f0= 'aa4926', f1= '(4926)Return Dashboard')
    db.d500.insert( f0= 'aa4928', f1= '(4928)Return Website')
    db.commit()
#
