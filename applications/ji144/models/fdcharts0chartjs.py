#
# table for controller: charts_chartjs
#

from gluon.contrib.populate import populate

db.define_table('dcharts0chartjs', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dcharts0chartjs.id ).count():
    populate(db.dcharts0chartjs, 5)
    db.commit()
#
