#
# table for controller: X503
#

from gluon.contrib.populate import populate

db.define_table('d503', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.d503.id ).count():
    db.d503.insert( f0= 'hh3025', f1= '(3025)503')
    db.d503.insert( f0= 'pc3026', f1= '(3026)Oops, an error has occurred. Service unavailable!')
    db.d503.insert( f0= 'pb3027', f1= '(3027)search ...')
    db.d503.insert( f0= 'aa3029', f1= '(3029)Return Dashboard')
    db.d503.insert( f0= 'aa3031', f1= '(3031)Return Website')
    db.commit()
#
