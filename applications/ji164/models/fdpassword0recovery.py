#
# table for controller: password_recovery
#

from gluon.contrib.populate import populate

db.define_table('dpassword0recovery', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dpassword0recovery.id ).count():
    db.dpassword0recovery.insert( f0= 'sp2090', f1= '(2090)outdated')
    db.dpassword0recovery.insert( f0= 'pc2091', f1= '(2091)to improve your experience.')
    db.dpassword0recovery.insert( f0= 'aa2092', f1= '(2092)upgrade your browser')
    db.dpassword0recovery.insert( f0= 'aa2094', f1= '(2094)Back to Dashboard')
    db.dpassword0recovery.insert( f0= 'hh2095', f1= '(2095)PASSWORD RECOVER')
    db.dpassword0recovery.insert( f0= 'pa2096', f1= '(2096)Please fill the form to recover your password')
    db.dpassword0recovery.insert( f0= 'pb2097', f1= '(2097)example@gmail.com')
    db.dpassword0recovery.insert( f0= 'sx2098', f1= '(2098)Your registered email address')
    db.dpassword0recovery.insert( f0= 'bu2099', f1= '(2099)Reset password')
    db.dpassword0recovery.insert( f0= 'pc2100', f1= '(2100)All rights reserved.')
    db.dpassword0recovery.insert( f0= 'pf2101', f1= '(2101)Copyright &copy; 2018')
    db.commit()
#
