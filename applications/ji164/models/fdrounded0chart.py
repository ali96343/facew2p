#
# table for controller: rounded_chart
#

from gluon.contrib.populate import populate

db.define_table('drounded0chart', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.drounded0chart.id ).count():
    populate(db.drounded0chart, 5)
    db.commit()
#
