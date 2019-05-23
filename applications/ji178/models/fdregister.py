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
    db.dregister.insert( f0= 'ha761', f1= '(761)Create an Account!')
    db.dregister.insert( f0= 'pb762', f1= '(762)First Name')
    db.dregister.insert( f0= 'pb763', f1= '(763)Last Name')
    db.dregister.insert( f0= 'pb764', f1= '(764)Email Address')
    db.dregister.insert( f0= 'pb765', f1= '(765)Password')
    db.dregister.insert( f0= 'pb766', f1= '(766)Repeat Password')
    db.dregister.insert( f0= 'aa771', f1= '(771)Forgot Password?')
    db.dregister.insert( f0= 'aa773', f1= '(773)Already have an account? Login!')
    db.commit()
#
