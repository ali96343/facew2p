#
# table for controller: X405
#

from gluon.contrib.populate import populate

db.define_table('d405', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.d405.id ).count():
    db.d405.insert( f0= 'hh5351', f1= '(5351)405')
    db.d405.insert( f0= 'pc5352', f1= '(5352)Oops, an error has occurred. Not allowed!')
    db.d405.insert( f0= 'pb5353', f1= '(5353)search ...')
    db.d405.insert( f0= 'aa5355', f1= '(5355)Return Dashboard')
    db.d405.insert( f0= 'aa5357', f1= '(5357)Return Website')
    db.commit()
#
