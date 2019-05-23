#
# table for controller: sm
#

from gluon.contrib.populate import populate

db.define_table('dsm', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dsm.id ).count():
    db.dsm.insert( f0= 'sx4898', f1= '(4898)Toggle navigation')
    db.dsm.insert( f0= 'aa4903', f1= '(4903)Dashboard')
    db.dsm.insert( f0= 'aa4905', f1= '(4905)Tables')
    db.dsm.insert( f0= 'aa4907', f1= '(4907)General')
    db.dsm.insert( f0= 'aa4909', f1= '(4909)Validation')
    db.dsm.insert( f0= 'aa4911', f1= '(4911)WYSIWYG')
    db.dsm.insert( f0= 'pb4913', f1= '(4913)Live Search ...')
    db.dsm.insert( f0= 'he4915', f1= '(4915)Archie')
    db.dsm.insert( f0= 'aa4916', f1= '(4916)Administrator')
    db.dsm.insert( f0= 'ba4917', f1= '(4917)Last Access :')
    db.dsm.insert( f0= 'lb4918', f1= '(4918)Menu')
    db.dsm.insert( f0= 'sx4920', f1= '(4920)Layouts')
    db.dsm.insert( f0= 'sx4939', f1= '(4939)Components')
    db.dsm.insert( f0= 'sx4951', f1= '(4951)Tables')
    db.dsm.insert( f0= 'aa4966', f1= '(4966)Level 2')
    db.dsm.insert( f0= 'aa4967', f1= '(4967)Level 2')
    db.dsm.insert( f0= 'aa4968', f1= '(4968)Level 3')
    db.dsm.insert( f0= 'aa4969', f1= '(4969)Level 3')
    db.dsm.insert( f0= 'aa4970', f1= '(4970)Level 4')
    db.dsm.insert( f0= 'aa4971', f1= '(4971)Level 4')
    db.dsm.insert( f0= 'aa4972', f1= '(4972)Level 5')
    db.dsm.insert( f0= 'aa4973', f1= '(4973)Level 5')
    db.dsm.insert( f0= 'aa4974', f1= '(4974)Level 5')
    db.dsm.insert( f0= 'aa4975', f1= '(4975)Level 4')
    db.dsm.insert( f0= 'aa4976', f1= '(4976)Level 2')
    db.dsm.insert( f0= 'aa4977', f1= '(4977)Level 1')
    db.dsm.insert( f0= 'aa4978', f1= '(4978)Level 2')
    db.dsm.insert( f0= 'aa4979', f1= '(4979)Level 2')
    db.dsm.insert( f0= 'aa4980', f1= '(4980)Level 2')
    db.dsm.insert( f0= 'hh4981', f1= '(4981)Code')
    db.dsm.insert( f0= 'bu4982', f1= '(4982)&times;')
    db.dsm.insert( f0= 'sp4983', f1= '(4983)Warning!')
    db.dsm.insert( f0= 'sx4984', f1= '(4984)1,4,4,7,5,9,10')
    db.dsm.insert( f0= 'sx4985', f1= '(4985)Loading..')
    db.dsm.insert( f0= 'sx4986', f1= '(4986)Loading..')
    db.dsm.insert( f0= 'sx4987', f1= '(4987)1,3,4,5,3,5')
    db.dsm.insert( f0= 'bu4988', f1= '(4988)Default')
    db.dsm.insert( f0= 'bu4989', f1= '(4989)Primary')
    db.dsm.insert( f0= 'bu4990', f1= '(4990)Info')
    db.dsm.insert( f0= 'bu4991', f1= '(4991)Success')
    db.dsm.insert( f0= 'bu4992', f1= '(4992)Danger')
    db.dsm.insert( f0= 'bu4993', f1= '(4993)Warning')
    db.dsm.insert( f0= 'bu4994', f1= '(4994)Inverse')
    db.dsm.insert( f0= 'bu4995', f1= '(4995)btn-metis-1')
    db.dsm.insert( f0= 'bu4996', f1= '(4996)btn-metis-2')
    db.dsm.insert( f0= 'bu4997', f1= '(4997)btn-metis-3')
    db.dsm.insert( f0= 'bu4998', f1= '(4998)btn-metis-4')
    db.dsm.insert( f0= 'bu4999', f1= '(4999)btn-metis-5')
    db.dsm.insert( f0= 'bu5000', f1= '(5000)btn-metis-6')
    db.dsm.insert( f0= 'si5001', f1= '(5001)20%')
    db.dsm.insert( f0= 'sp5002', f1= '(5002)Default')
    db.dsm.insert( f0= 'si5003', f1= '(5003)40%')
    db.dsm.insert( f0= 'sp5004', f1= '(5004)Success')
    db.dsm.insert( f0= 'si5005', f1= '(5005)60%')
    db.dsm.insert( f0= 'sp5006', f1= '(5006)warning')
    db.dsm.insert( f0= 'si5007', f1= '(5007)80%')
    db.dsm.insert( f0= 'sp5008', f1= '(5008)Danger')
    db.dsm.insert( f0= 'pa5009', f1= '(5009)2017 &copy; Metis Bootstrap Admin Template v2.4.2')
    db.dsm.insert( f0= 'bu5010', f1= '(5010)&times;')
    db.dsm.insert( f0= 'hd5011', f1= '(5011)Modal title')
    db.dsm.insert( f0= 'bu5012', f1= '(5012)Close')
    db.commit()
#
