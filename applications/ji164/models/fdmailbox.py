#
# table for controller: mailbox
#

from gluon.contrib.populate import populate

db.define_table('dmailbox', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dmailbox.id ).count():
    populate(db.dmailbox, 5)
    db.commit()
#
