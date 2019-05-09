#
# table for controller: image_cropper
#

from gluon.contrib.populate import populate

db.define_table('dimage0cropper', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dimage0cropper.id ).count():
    populate(db.dimage0cropper, 5)
    db.commit()
#
