#
# table for controller: login
#

from gluon.contrib.populate import populate

db.define_table('dlogin', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dlogin.id ).count():
    db.dlogin.insert( f0= 'sp10222', f1= '(10222)outdated')
    db.dlogin.insert( f0= 'pc10223', f1= '(10223)to improve your experience.')
    db.dlogin.insert( f0= 'aa10224', f1= '(10224)upgrade your browser')
    db.dlogin.insert( f0= 'aa10226', f1= '(10226)Back to Dashboard')
    db.dlogin.insert( f0= 'hh10227', f1= '(10227)PLEASE LOGIN TO APP')
    db.dlogin.insert( f0= 'pa10228', f1= '(10228)This is the best app ever!')
    db.dlogin.insert( f0= 'pb10229', f1= '(10229)example@gmail.com')
    db.dlogin.insert( f0= 'sx10230', f1= '(10230)Your unique username to app')
    db.dlogin.insert( f0= 'pb10231', f1= '(10231)******')
    db.dlogin.insert( f0= 'sx10232', f1= '(10232)Yur strong password')
    db.dlogin.insert( f0= 'pc10233', f1= '(10233)(if this is a private computer)')
    db.dlogin.insert( f0= 'bu10234', f1= '(10234)Login')
    db.dlogin.insert( f0= 'aa10235', f1= '(10235)Register')
    db.dlogin.insert( f0= 'pc10236', f1= '(10236)All rights reserved.')
    db.dlogin.insert( f0= 'pf10237', f1= '(10237)Copyright &copy; 2018')
    db.commit()
#
