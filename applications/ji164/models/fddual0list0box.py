#
# table for controller: dual_list_box
#

from gluon.contrib.populate import populate

db.define_table('ddual0list0box', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.ddual0list0box.id ).count():
    populate(db.ddual0list0box, 5)
    db.commit()
#
