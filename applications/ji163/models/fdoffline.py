#
# table for controller: offline
#

from gluon.contrib.populate import populate

db.define_table('doffline', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.doffline.id ).count():
    db.doffline.insert( f0= 'hh6367', f1= '(6367)Offline')
    db.doffline.insert( f0= 'pc6368', f1= '(6368)We will back shortly')
    db.doffline.insert( f0= 'pb6369', f1= '(6369)search ...')
    db.doffline.insert( f0= 'aa6371', f1= '(6371)Return Dashboard')
    db.doffline.insert( f0= 'aa6373', f1= '(6373)Return Website')
    db.commit()
#
