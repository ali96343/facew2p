#
# table for controller: form_examples
#

from gluon.contrib.populate import populate

db.define_table('dform0examples', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dform0examples.id ).count():
    populate(db.dform0examples, 5)
    db.commit()
#
