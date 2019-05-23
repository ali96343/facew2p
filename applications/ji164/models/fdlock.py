#
# table for controller: lock
#

from gluon.contrib.populate import populate

db.define_table('dlock', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dlock.id ).count():
    db.dlock.insert( f0= 'sp17638', f1= '(17638)outdated')
    db.dlock.insert( f0= 'pc17639', f1= '(17639)to improve your experience.')
    db.dlock.insert( f0= 'aa17640', f1= '(17640)upgrade your browser')
    db.dlock.insert( f0= 'aa17642', f1= '(17642)Back to Dashboard')
    db.dlock.insert( f0= 'sp17643', f1= '(17643)Friday, February 27, 2015')
    db.dlock.insert( f0= 'sx17644', f1= '(17644)3:43:15 PM')
    db.dlock.insert( f0= 'pa17645', f1= '(17645)Your are in lock screen. Main app was shut down and you need to enter your passwor to go back to app.')
    db.dlock.insert( f0= 'pb17646', f1= '(17646)******')
    db.dlock.insert( f0= 'bu17647', f1= '(17647)Unlock')
    db.dlock.insert( f0= 'pc17648', f1= '(17648)All rights reserved.')
    db.dlock.insert( f0= 'pf17649', f1= '(17649)Copyright &copy; 2018')
    db.commit()
#
