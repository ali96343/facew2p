#
# table for controller: login_register
#

from gluon.contrib.populate import populate

db.define_table('dlogin0register', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dlogin0register.id ).count():
    db.dlogin0register.insert( f0= 'sp2041', f1= '(2041)outdated')
    db.dlogin0register.insert( f0= 'pc2042', f1= '(2042)to improve your experience.')
    db.dlogin0register.insert( f0= 'aa2043', f1= '(2043)upgrade your browser')
    db.dlogin0register.insert( f0= 'pb2044', f1= '(2044)Username')
    db.dlogin0register.insert( f0= 'pb2045', f1= '(2045)Password')
    db.dlogin0register.insert( f0= 'sp2046', f1= '(2046)Register')
    db.dlogin0register.insert( f0= 'sp2047', f1= '(2047)Forgot Password')
    db.dlogin0register.insert( f0= 'pb2048', f1= '(2048)Username')
    db.dlogin0register.insert( f0= 'pb2049', f1= '(2049)Email Address')
    db.dlogin0register.insert( f0= 'pb2050', f1= '(2050)Password')
    db.dlogin0register.insert( f0= 'sp2051', f1= '(2051)Sign in')
    db.dlogin0register.insert( f0= 'sp2052', f1= '(2052)Forgot Password')
    db.dlogin0register.insert( f0= 'pc2053', f1= '(2053)Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla eu risus. Curabitur commodo lorem fringilla enim feugiat commodo sed ac lacus.')
    db.dlogin0register.insert( f0= 'pb2054', f1= '(2054)Email Address')
    db.dlogin0register.insert( f0= 'sp2055', f1= '(2055)Sign in')
    db.dlogin0register.insert( f0= 'sp2056', f1= '(2056)Register')
    db.commit()
#
