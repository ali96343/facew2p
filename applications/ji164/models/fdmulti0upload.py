#
# table for controller: multi_upload
#

from gluon.contrib.populate import populate

db.define_table('dmulti0upload', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dmulti0upload.id ).count():
    populate(db.dmulti0upload, 5)
    db.commit()
#
