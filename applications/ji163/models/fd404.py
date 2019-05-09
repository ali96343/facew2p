#
# table for controller: X404
#

from gluon.contrib.populate import populate

db.define_table('d404', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.d404.id ).count():
    db.d404.insert( f0= 'hh5513', f1= '(5513)404')
    db.d404.insert( f0= 'pc5514', f1= '(5514)Nope, not here.')
    db.d404.insert( f0= 'pb5515', f1= '(5515)search ...')
    db.d404.insert( f0= 'aa5517', f1= '(5517)Return Dashboard')
    db.d404.insert( f0= 'aa5519', f1= '(5519)Return Website')
    db.commit()
#
