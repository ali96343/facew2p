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
    db.dinvoice0print.insert( f0= 'ic6484', f1= '(6484)Date: 2/10/2014')
    db.dinvoice0print.insert( f0= 'sp6485', f1= '(6485)Admin, Inc.')
    db.dinvoice0print.insert( f0= 'ma6486', f1= '(6486)info@almasaeedstudio.com')
    db.dinvoice0print.insert( f0= 'sp6487', f1= '(6487)John Doe')
    db.dinvoice0print.insert( f0= 'ma6488', f1= '(6488)john.doe@example.com')
    db.dinvoice0print.insert( f0= 'bb6489', f1= '(6489)Invoice #007612')
    db.dinvoice0print.insert( f0= 'bb6490', f1= '(6490)Order ID:')
    db.dinvoice0print.insert( f0= 'ba6491', f1= '(6491)4F3S8J')
    db.dinvoice0print.insert( f0= 'bb6492', f1= '(6492)Payment Due:')
    db.dinvoice0print.insert( f0= 'ba6493', f1= '(6493)2/22/2014')
    db.dinvoice0print.insert( f0= 'bb6494', f1= '(6494)Account:')
    db.dinvoice0print.insert( f0= 'pc6495', f1= '(6495)Payment Methods:')
    db.dinvoice0print.insert( f0= 'pc6500', f1= '(6500)Amount Due 2/22/2014')
    db.commit()
#
