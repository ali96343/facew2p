#
# table for controller: sparkline
#

from gluon.contrib.populate import populate

db.define_table('dsparkline', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dsparkline.id ).count():
    populate(db.dsparkline, 5)
    db.commit()
#
