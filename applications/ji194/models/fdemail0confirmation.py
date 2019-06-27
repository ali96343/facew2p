#
# table for controller: emailIIconfirmation
#

from gluon.contrib.populate import populate

db.define_table('demail0confirmation', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.demail0confirmation.id ).count():
    db.demail0confirmation.insert( f0= 'aa4707', f1= '(4707)Ace &copy; 2014')
    db.demail0confirmation.insert( f0= 'aa4708', f1= '(4708)twitter')
    db.demail0confirmation.insert( f0= 'aa4709', f1= '(4709)facebook')
    db.demail0confirmation.insert( f0= 'aa4710', f1= '(4710)google+')
    db.commit()
#
