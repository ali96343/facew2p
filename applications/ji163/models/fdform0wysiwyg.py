#
# table for controller: form_wysiwyg
#

from gluon.contrib.populate import populate

db.define_table('dform0wysiwyg', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dform0wysiwyg.id ).count():
    db.dform0wysiwyg.insert( f0= 'sx5370', f1= '(5370)Toggle navigation')
    db.dform0wysiwyg.insert( f0= 'sx5373', f1= '(5373)5')
    db.dform0wysiwyg.insert( f0= 'sx5374', f1= '(5374)4')
    db.dform0wysiwyg.insert( f0= 'aa5377', f1= '(5377)Dashboard')
    db.dform0wysiwyg.insert( f0= 'aa5379', f1= '(5379)Tables')
    db.dform0wysiwyg.insert( f0= 'aa5381', f1= '(5381)General')
    db.dform0wysiwyg.insert( f0= 'aa5383', f1= '(5383)Validation')
    db.dform0wysiwyg.insert( f0= 'aa5385', f1= '(5385)WYSIWYG')
    db.dform0wysiwyg.insert( f0= 'aa5387', f1= '(5387)Wizard &amp; File Upload')
    db.dform0wysiwyg.insert( f0= 'pb5388', f1= '(5388)Live Search ...')
    db.dform0wysiwyg.insert( f0= 'sx5390', f1= '(5390)16')
    db.dform0wysiwyg.insert( f0= 'he5391', f1= '(5391)Archie')
    db.dform0wysiwyg.insert( f0= 'aa5392', f1= '(5392)Administrator')
    db.dform0wysiwyg.insert( f0= 'ba5393', f1= '(5393)Last Access :')
    db.dform0wysiwyg.insert( f0= 'lb5394', f1= '(5394)Menu')
    db.dform0wysiwyg.insert( f0= 'sx5396', f1= '(5396)&nbsp;Dashboard')
    db.dform0wysiwyg.insert( f0= 'sx5397', f1= '(5397)Layouts')
    db.dform0wysiwyg.insert( f0= 'sx5416', f1= '(5416)Components')
    db.dform0wysiwyg.insert( f0= 'sx5428', f1= '(5428)Tables')
    db.dform0wysiwyg.insert( f0= 'aa5443', f1= '(5443)Level 2')
    db.dform0wysiwyg.insert( f0= 'aa5444', f1= '(5444)Level 2')
    db.dform0wysiwyg.insert( f0= 'aa5445', f1= '(5445)Level 3')
    db.dform0wysiwyg.insert( f0= 'aa5446', f1= '(5446)Level 3')
    db.dform0wysiwyg.insert( f0= 'aa5447', f1= '(5447)Level 4')
    db.dform0wysiwyg.insert( f0= 'aa5448', f1= '(5448)Level 4')
    db.dform0wysiwyg.insert( f0= 'aa5449', f1= '(5449)Level 5')
    db.dform0wysiwyg.insert( f0= 'aa5450', f1= '(5450)Level 5')
    db.dform0wysiwyg.insert( f0= 'aa5451', f1= '(5451)Level 5')
    db.dform0wysiwyg.insert( f0= 'aa5452', f1= '(5452)Level 4')
    db.dform0wysiwyg.insert( f0= 'aa5453', f1= '(5453)Level 2')
    db.dform0wysiwyg.insert( f0= 'aa5454', f1= '(5454)Level 1')
    db.dform0wysiwyg.insert( f0= 'aa5455', f1= '(5455)Level 2')
    db.dform0wysiwyg.insert( f0= 'aa5456', f1= '(5456)Level 2')
    db.dform0wysiwyg.insert( f0= 'aa5457', f1= '(5457)Level 2')
    db.dform0wysiwyg.insert( f0= 'hh5458', f1= '(5458)Basic Editor')
    db.dform0wysiwyg.insert( f0= 'hh5459', f1= '(5459)CKEditor')
    db.dform0wysiwyg.insert( f0= 'hh5460', f1= '(5460)Markdown Editor')
    db.dform0wysiwyg.insert( f0= 'aa5461', f1= '(5461)Markdown')
    db.dform0wysiwyg.insert( f0= 'aa5462', f1= '(5462)Preview')
    db.dform0wysiwyg.insert( f0= 'hh5463', f1= '(5463)epiceditor')
    db.dform0wysiwyg.insert( f0= 'bu5464', f1= '(5464)&times;')
    db.dform0wysiwyg.insert( f0= 'sp5465', f1= '(5465)Warning!')
    db.dform0wysiwyg.insert( f0= 'sx5466', f1= '(5466)1,4,4,7,5,9,10')
    db.dform0wysiwyg.insert( f0= 'sx5467', f1= '(5467)Loading..')
    db.dform0wysiwyg.insert( f0= 'sx5468', f1= '(5468)Loading..')
    db.dform0wysiwyg.insert( f0= 'sx5469', f1= '(5469)1,3,4,5,3,5')
    db.dform0wysiwyg.insert( f0= 'bu5470', f1= '(5470)Default')
    db.dform0wysiwyg.insert( f0= 'bu5471', f1= '(5471)Primary')
    db.dform0wysiwyg.insert( f0= 'bu5472', f1= '(5472)Info')
    db.dform0wysiwyg.insert( f0= 'bu5473', f1= '(5473)Success')
    db.dform0wysiwyg.insert( f0= 'bu5474', f1= '(5474)Danger')
    db.dform0wysiwyg.insert( f0= 'bu5475', f1= '(5475)Warning')
    db.dform0wysiwyg.insert( f0= 'bu5476', f1= '(5476)Inverse')
    db.dform0wysiwyg.insert( f0= 'bu5477', f1= '(5477)btn-metis-1')
    db.dform0wysiwyg.insert( f0= 'bu5478', f1= '(5478)btn-metis-2')
    db.dform0wysiwyg.insert( f0= 'bu5479', f1= '(5479)btn-metis-3')
    db.dform0wysiwyg.insert( f0= 'bu5480', f1= '(5480)btn-metis-4')
    db.dform0wysiwyg.insert( f0= 'bu5481', f1= '(5481)btn-metis-5')
    db.dform0wysiwyg.insert( f0= 'bu5482', f1= '(5482)btn-metis-6')
    db.dform0wysiwyg.insert( f0= 'si5483', f1= '(5483)20%')
    db.dform0wysiwyg.insert( f0= 'sp5484', f1= '(5484)Default')
    db.dform0wysiwyg.insert( f0= 'si5485', f1= '(5485)40%')
    db.dform0wysiwyg.insert( f0= 'sp5486', f1= '(5486)Success')
    db.dform0wysiwyg.insert( f0= 'si5487', f1= '(5487)60%')
    db.dform0wysiwyg.insert( f0= 'sp5488', f1= '(5488)warning')
    db.dform0wysiwyg.insert( f0= 'si5489', f1= '(5489)80%')
    db.dform0wysiwyg.insert( f0= 'sp5490', f1= '(5490)Danger')
    db.dform0wysiwyg.insert( f0= 'pa5491', f1= '(5491)2017 &copy; Metis Bootstrap Admin Template v2.4.2')
    db.dform0wysiwyg.insert( f0= 'bu5492', f1= '(5492)&times;')
    db.dform0wysiwyg.insert( f0= 'hd5493', f1= '(5493)Modal title')
    db.dform0wysiwyg.insert( f0= 'bu5494', f1= '(5494)Close')
    db.commit()
#
