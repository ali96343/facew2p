#
# table for controller: typography
#

from gluon.contrib.populate import populate

db.define_table('dtypography', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dtypography.id ).count():
    populate(db.dtypography, 5)
    db.commit()
#
