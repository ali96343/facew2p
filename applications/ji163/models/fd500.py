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
    db.d500.insert( f0= 'hh4748', f1= '(4748)500')
    db.d500.insert( f0= 'pc4749', f1= '(4749)Oops, an error has occurred. Internal server error!')
    db.d500.insert( f0= 'pb4750', f1= '(4750)search ...')
    db.d500.insert( f0= 'aa4752', f1= '(4752)Return Dashboard')
    db.d500.insert( f0= 'aa4754', f1= '(4754)Return Website')
    db.commit()
#
