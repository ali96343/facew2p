#
# table for controller: contact
#

from gluon.contrib.populate import populate

db.define_table('dcontact', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dcontact.id ).count():
    db.dcontact.insert( f0= 'aa281', f1= '(281)Login')
    db.dcontact.insert( f0= 'aa283', f1= '(283)Home')
    db.dcontact.insert( f0= 'aa285', f1= '(285)Games')
    db.dcontact.insert( f0= 'aa287', f1= '(287)Blog')
    db.dcontact.insert( f0= 'aa289', f1= '(289)Forums')
    db.dcontact.insert( f0= 'aa291', f1= '(291)Contact')
    db.dcontact.insert( f0= 'di292', f1= '(292)Latest News')
    db.dcontact.insert( f0= 'sx293', f1= '(293)new')
    db.dcontact.insert( f0= 'sx294', f1= '(294)strategy')
    db.dcontact.insert( f0= 'sx295', f1= '(295)racing')
    db.dcontact.insert( f0= 'hh297', f1= '(297)Contact us')
    db.dcontact.insert( f0= 'pa298', f1= '(298)Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec malesuada lorem maximus mauris scelerisque, at rutrum nulla dictum.')
    db.dcontact.insert( f0= 'hd299', f1= '(299)Contact us')
    db.dcontact.insert( f0= 'pa300', f1= '(300)Odio ultrices ut. Etiam ac erat ut enim maximus accumsan vel ac nisl. Duis feug iat bibendum orci, non elementum urna. Cras sit amet sapien aliquam.')
    db.dcontact.insert( f0= 'di301', f1= '(301)Address')
    db.dcontact.insert( f0= 'di302', f1= '(302)Phone')
    db.dcontact.insert( f0= 'di303', f1= '(303)E-mail')
    db.dcontact.insert( f0= 'hd304', f1= '(304)Leave a Reply')
    db.dcontact.insert( f0= 'pb305', f1= '(305)Name')
    db.dcontact.insert( f0= 'pb306', f1= '(306)Email')
    db.dcontact.insert( f0= 'pb307', f1= '(307)Subject')
    db.dcontact.insert( f0= 'pb308', f1= '(308)Message')
    db.dcontact.insert( f0= 'bu309', f1= '(309)Send')
    db.dcontact.insert( f0= 'pa312', f1= '(312)Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame.')
    db.dcontact.insert( f0= 'hd313', f1= '(313)Latest Posts')
    db.dcontact.insert( f0= 'di315', f1= '(315)June 21, 2018')
    db.dcontact.insert( f0= 'pa316', f1= '(316)Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum')
    db.dcontact.insert( f0= 'aa317', f1= '(317)By Admin')
    db.dcontact.insert( f0= 'di319', f1= '(319)June 21, 2018')
    db.dcontact.insert( f0= 'pa320', f1= '(320)Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum')
    db.dcontact.insert( f0= 'aa321', f1= '(321)By Admin')
    db.dcontact.insert( f0= 'di323', f1= '(323)June 21, 2018')
    db.dcontact.insert( f0= 'pa324', f1= '(324)Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum')
    db.dcontact.insert( f0= 'aa325', f1= '(325)By Admin')
    db.dcontact.insert( f0= 'hd326', f1= '(326)Top Comments')
    db.dcontact.insert( f0= 'sp328', f1= '(328)on')
    db.dcontact.insert( f0= 'pc329', f1= '(329)Lorem ipsum dolor sit amet, co')
    db.dcontact.insert( f0= 'aa330', f1= '(330)James Smith')
    db.dcontact.insert( f0= 'di331', f1= '(331)June 21, 2018')
    db.dcontact.insert( f0= 'sp333', f1= '(333)on')
    db.dcontact.insert( f0= 'pc334', f1= '(334)Lorem ipsum dolor sit amet, co')
    db.dcontact.insert( f0= 'aa335', f1= '(335)James Smith')
    db.dcontact.insert( f0= 'di336', f1= '(336)June 21, 2018')
    db.dcontact.insert( f0= 'sp338', f1= '(338)on')
    db.dcontact.insert( f0= 'pc339', f1= '(339)Lorem ipsum dolor sit amet, co')
    db.dcontact.insert( f0= 'aa340', f1= '(340)James Smith')
    db.dcontact.insert( f0= 'di341', f1= '(341)June 21, 2018')
    db.dcontact.insert( f0= 'sp343', f1= '(343)on')
    db.dcontact.insert( f0= 'pc344', f1= '(344)Lorem ipsum dolor sit amet, co')
    db.dcontact.insert( f0= 'aa345', f1= '(345)James Smith')
    db.dcontact.insert( f0= 'di346', f1= '(346)June 21, 2018')
    db.dcontact.insert( f0= 'aa348', f1= '(348)Home')
    db.dcontact.insert( f0= 'aa350', f1= '(350)Games')
    db.dcontact.insert( f0= 'aa352', f1= '(352)Blog')
    db.dcontact.insert( f0= 'aa354', f1= '(354)Forums')
    db.dcontact.insert( f0= 'aa356', f1= '(356)Contact')
    db.commit()
#
