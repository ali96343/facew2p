#
# table for controller: mailbox_compose
#

from gluon.contrib.populate import populate

db.define_table('dmailbox0compose', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dmailbox0compose.id ).count():
    populate(db.dmailbox0compose, 5)
    db.commit()
#
