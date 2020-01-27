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
    db.dinvoice0print.insert( f0= 'ic9096', f1= '(9096)Date: 2/10/2014')
    db.dinvoice0print.insert( f0= 'sp9097', f1= '(9097)Admin, Inc.')
    db.dinvoice0print.insert( f0= 'ma9098', f1= '(9098)info@almasaeedstudio.com')
    db.dinvoice0print.insert( f0= 'sp9099', f1= '(9099)John Doe')
    db.dinvoice0print.insert( f0= 'ma9100', f1= '(9100)john.doe@example.com')
    db.dinvoice0print.insert( f0= 'bb9101', f1= '(9101)Invoice #007612')
    db.dinvoice0print.insert( f0= 'bb9102', f1= '(9102)Order ID:')
    db.dinvoice0print.insert( f0= 'ba9103', f1= '(9103)4F3S8J')
    db.dinvoice0print.insert( f0= 'bb9104', f1= '(9104)Payment Due:')
    db.dinvoice0print.insert( f0= 'ba9105', f1= '(9105)2/22/2014')
    db.dinvoice0print.insert( f0= 'bb9106', f1= '(9106)Account:')
    db.dinvoice0print.insert( f0= 'pc9107', f1= '(9107)Payment Methods:')
    db.dinvoice0print.insert( f0= 'pc9112', f1= '(9112)Amount Due 2/22/2014')
    db.commit()
#
