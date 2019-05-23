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
    db.d503.insert( f0= 'hh2919', f1= '(2919)503')
    db.d503.insert( f0= 'pc2920', f1= '(2920)Oops, an error has occurred. Service unavailable!')
    db.d503.insert( f0= 'pb2921', f1= '(2921)search ...')
    db.d503.insert( f0= 'aa2923', f1= '(2923)Return Dashboard')
    db.d503.insert( f0= 'aa2925', f1= '(2925)Return Website')
    db.commit()
#
