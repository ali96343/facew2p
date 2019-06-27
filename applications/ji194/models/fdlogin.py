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
    db.dlogin.insert( f0= 'sx2482', f1= '(2482)Ace')
    db.dlogin.insert( f0= 'sx2483', f1= '(2483)Application')
    db.dlogin.insert( f0= 'hd2484', f1= '(2484)&copy; Company Name')
    db.dlogin.insert( f0= 'pb2485', f1= '(2485)Username')
    db.dlogin.insert( f0= 'pb2486', f1= '(2486)Password')
    db.dlogin.insert( f0= 'sx2487', f1= '(2487)Remember Me')
    db.dlogin.insert( f0= 'sx2488', f1= '(2488)Login')
    db.dlogin.insert( f0= 'sx2489', f1= '(2489)Or Login Using')
    db.dlogin.insert( f0= 'pb2490', f1= '(2490)Email')
    db.dlogin.insert( f0= 'sx2491', f1= '(2491)Send Me!')
    db.dlogin.insert( f0= 'pa2492', f1= '(2492)Enter your details to begin:')
    db.dlogin.insert( f0= 'pb2493', f1= '(2493)Email')
    db.dlogin.insert( f0= 'pb2494', f1= '(2494)Username')
    db.dlogin.insert( f0= 'pb2495', f1= '(2495)Password')
    db.dlogin.insert( f0= 'pb2496', f1= '(2496)Repeat password')
    db.dlogin.insert( f0= 'aa2497', f1= '(2497)User Agreement')
    db.dlogin.insert( f0= 'sx2498', f1= '(2498)Reset')
    db.dlogin.insert( f0= 'sx2499', f1= '(2499)Register')
    db.dlogin.insert( f0= 'aa2500', f1= '(2500)Dark')
    db.dlogin.insert( f0= 'aa2501', f1= '(2501)Blur')
    db.dlogin.insert( f0= 'aa2502', f1= '(2502)Light')
    db.commit()
#
