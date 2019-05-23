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
    db.d405.insert( f0= 'hh5162', f1= '(5162)405')
    db.d405.insert( f0= 'pc5163', f1= '(5163)Oops, an error has occurred. Not allowed!')
    db.d405.insert( f0= 'pb5164', f1= '(5164)search ...')
    db.d405.insert( f0= 'aa5166', f1= '(5166)Return Dashboard')
    db.d405.insert( f0= 'aa5168', f1= '(5168)Return Website')
    db.commit()
#
