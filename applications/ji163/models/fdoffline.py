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
    db.doffline.insert( f0= 'hh6093', f1= '(6093)Offline')
    db.doffline.insert( f0= 'pc6094', f1= '(6094)We will back shortly')
    db.doffline.insert( f0= 'pb6095', f1= '(6095)search ...')
    db.doffline.insert( f0= 'aa6097', f1= '(6097)Return Dashboard')
    db.doffline.insert( f0= 'aa6099', f1= '(6099)Return Website')
    db.commit()
#
