#
# table for controller: register
#

from gluon.contrib.populate import populate

db.define_table('dregister', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dregister.id ).count():
    db.dregister.insert( f0= 'sp14135', f1= '(14135)outdated')
    db.dregister.insert( f0= 'pc14136', f1= '(14136)to improve your experience.')
    db.dregister.insert( f0= 'aa14137', f1= '(14137)upgrade your browser')
    db.dregister.insert( f0= 'aa14139', f1= '(14139)Back to Dashboard')
    db.dregister.insert( f0= 'hh14140', f1= '(14140)Registration')
    db.dregister.insert( f0= 'pa14141', f1= '(14141)Admin template with very clean and aesthetic style prepared for your next app.')
    db.dregister.insert( f0= 'bu14142', f1= '(14142)Register')
    db.dregister.insert( f0= 'bu14143', f1= '(14143)Cancel')
    db.dregister.insert( f0= 'pc14144', f1= '(14144)All rights reserved.')
    db.dregister.insert( f0= 'pf14145', f1= '(14145)Copyright &copy; 2018')
    db.commit()
#
