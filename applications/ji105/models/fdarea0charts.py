#
# table for controller: area_charts
#

from gluon.contrib.populate import populate

db.define_table('darea0charts', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.darea0charts.id ).count():
    populate(db.darea0charts, 5)
    db.commit()
#
