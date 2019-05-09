#
# table for controller: code_editor
#

from gluon.contrib.populate import populate

db.define_table('dcode0editor', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dcode0editor.id ).count():
    populate(db.dcode0editor, 5)
    db.commit()
#
