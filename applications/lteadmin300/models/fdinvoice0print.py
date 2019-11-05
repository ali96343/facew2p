#
# table for controller: invoiceIIprint
#

from gluon.contrib.populate import populate

db.define_table('dinvoice0print', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dinvoice0print.id ).count():
    db.dinvoice0print.insert( f0= 'ic8561', f1= '(8561)Date: 2/10/2014')
    db.dinvoice0print.insert( f0= 'sp8562', f1= '(8562)Admin, Inc.')
    db.dinvoice0print.insert( f0= 'ma8563', f1= '(8563)info@almasaeedstudio.com')
    db.dinvoice0print.insert( f0= 'sp8564', f1= '(8564)John Doe')
    db.dinvoice0print.insert( f0= 'ma8565', f1= '(8565)john.doe@example.com')
    db.dinvoice0print.insert( f0= 'bb8566', f1= '(8566)Invoice #007612')
    db.dinvoice0print.insert( f0= 'bb8567', f1= '(8567)Order ID:')
    db.dinvoice0print.insert( f0= 'ba8568', f1= '(8568)4F3S8J')
    db.dinvoice0print.insert( f0= 'bb8569', f1= '(8569)Payment Due:')
    db.dinvoice0print.insert( f0= 'ba8570', f1= '(8570)2/22/2014')
    db.dinvoice0print.insert( f0= 'bb8571', f1= '(8571)Account:')
    db.dinvoice0print.insert( f0= 'pc8572', f1= '(8572)Payment Methods:')
    db.dinvoice0print.insert( f0= 'pc8577', f1= '(8577)Amount Due 2/22/2014')
    db.commit()
#
