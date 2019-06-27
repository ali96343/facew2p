#
# table for controller: emailIIcontrast
#

from gluon.contrib.populate import populate

db.define_table('demail0contrast', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.demail0contrast.id ).count():
    db.demail0contrast.insert( f0= 'di2068', f1= '(2068)Phasellus dictum sapien a neque luctus cursus. Pellentesque sem dolor, fringilla et pharetra vitae.')
    db.demail0contrast.insert( f0= 'sx2072', f1= '(2072)click here to unsubscribe')
    db.commit()
#
