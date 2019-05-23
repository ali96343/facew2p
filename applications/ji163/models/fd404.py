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
    db.d404.insert( f0= 'hh5319', f1= '(5319)404')
    db.d404.insert( f0= 'pc5320', f1= '(5320)Nope, not here.')
    db.d404.insert( f0= 'pb5321', f1= '(5321)search ...')
    db.d404.insert( f0= 'aa5323', f1= '(5323)Return Dashboard')
    db.d404.insert( f0= 'aa5325', f1= '(5325)Return Website')
    db.commit()
#
