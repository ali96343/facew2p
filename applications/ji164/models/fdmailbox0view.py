#
# table for controller: mailbox_view
#

from gluon.contrib.populate import populate

db.define_table('dmailbox0view', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dmailbox0view.id ).count():
    populate(db.dmailbox0view, 5)
    db.commit()
#
