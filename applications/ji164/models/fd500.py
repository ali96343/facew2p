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
    db.d500.insert( f0= 'sp17175', f1= '(17175)outdated')
    db.d500.insert( f0= 'pc17176', f1= '(17176)to improve your experience.')
    db.d500.insert( f0= 'aa17177', f1= '(17177)upgrade your browser')
    db.d500.insert( f0= 'aa17179', f1= '(17179)Back to Dashboard')
    db.d500.insert( f0= 'sx17180', f1= '(17180)500')
    db.d500.insert( f0= 'hh17181', f1= '(17181)Internal Server Error')
    db.d500.insert( f0= 'pa17182', f1= '(17182)The server encountered something unexpected that didn t allow it to complete the request. We apologize.')
    db.d500.insert( f0= 'aa17183', f1= '(17183)Report Problem')
    db.d500.insert( f0= 'pc17184', f1= '(17184)All rights reserved.')
    db.d500.insert( f0= 'pf17185', f1= '(17185)Copyright  2018')
    db.commit()
#
