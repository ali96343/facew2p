#
# table for controller: index
#

from gluon.contrib.populate import populate

db.define_table('dindex', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dindex.id ).count():
    db.dindex.insert( f0= 'aa553', f1= '(553)Login')
    db.dindex.insert( f0= 'aa555', f1= '(555)Home')
    db.dindex.insert( f0= 'aa557', f1= '(557)Games')
    db.dindex.insert( f0= 'aa559', f1= '(559)Blog')
    db.dindex.insert( f0= 'aa561', f1= '(561)Forums')
    db.dindex.insert( f0= 'aa563', f1= '(563)Contact')
    db.dindex.insert( f0= 'sp565', f1= '(565)Games')
    db.dindex.insert( f0= 'hh566', f1= '(566)The Best')
    db.dindex.insert( f0= 'pc567', f1= '(567)Suspendisse cursus faucibus finibus.')
    db.dindex.insert( f0= 'pf568', f1= '(568)Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec malesuada')
    db.dindex.insert( f0= 'bd569', f1= '(569)lorem maximus mauris scelerisque, at rutrum nulla dictum. Ut ac ligula sapien.')
    db.dindex.insert( f0= 'aa570', f1= '(570)Read More')
    db.dindex.insert( f0= 'sp572', f1= '(572)Games')
    db.dindex.insert( f0= 'hh573', f1= '(573)The Best')
    db.dindex.insert( f0= 'pc574', f1= '(574)Suspendisse cursus faucibus finibus.')
    db.dindex.insert( f0= 'pf575', f1= '(575)Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec malesuada')
    db.dindex.insert( f0= 'bd576', f1= '(576)lorem maximus mauris scelerisque, at rutrum nulla dictum. Ut ac ligula sapien.')
    db.dindex.insert( f0= 'aa577', f1= '(577)Read More')
    db.dindex.insert( f0= 'di578', f1= '(578)Latest News')
    db.dindex.insert( f0= 'sx579', f1= '(579)new')
    db.dindex.insert( f0= 'sx580', f1= '(580)strategy')
    db.dindex.insert( f0= 'sx581', f1= '(581)racing')
    db.dindex.insert( f0= 'sx583', f1= '(583)new')
    db.dindex.insert( f0= 'aa584', f1= '(584)Suspendisse ut justo tem por, rutrum')
    db.dindex.insert( f0= 'pa585', f1= '(585)Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
    db.dindex.insert( f0= 'aa586', f1= '(586)3 Comments')
    db.dindex.insert( f0= 'sx588', f1= '(588)strategy')
    db.dindex.insert( f0= 'aa589', f1= '(589)Justo tempor, rutrum erat id, molestie')
    db.dindex.insert( f0= 'pa590', f1= '(590)Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
    db.dindex.insert( f0= 'aa591', f1= '(591)3 Comments')
    db.dindex.insert( f0= 'sx593', f1= '(593)new')
    db.dindex.insert( f0= 'aa594', f1= '(594)Nullam lacinia ex eleifend orci porttitor')
    db.dindex.insert( f0= 'pa595', f1= '(595)Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
    db.dindex.insert( f0= 'aa596', f1= '(596)3 Comments')
    db.dindex.insert( f0= 'sx598', f1= '(598)racing')
    db.dindex.insert( f0= 'aa599', f1= '(599)Lacinia ex eleifend orci suscipit')
    db.dindex.insert( f0= 'pa600', f1= '(600)Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
    db.dindex.insert( f0= 'aa601', f1= '(601)3 Comments')
    db.dindex.insert( f0= 'di603', f1= '(603)new')
    db.dindex.insert( f0= 'hh604', f1= '(604)Recent Games')
    db.dindex.insert( f0= 'di606', f1= '(606)new')
    db.dindex.insert( f0= 'hh607', f1= '(607)Suspendisse ut justo tem por, rutrum')
    db.dindex.insert( f0= 'pa608', f1= '(608)Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit amet, consectetur elit.')
    db.dindex.insert( f0= 'aa609', f1= '(609)3 Comments')
    db.dindex.insert( f0= 'di613', f1= '(613)racing')
    db.dindex.insert( f0= 'hh614', f1= '(614)Susce pulvinar metus nulla, vel facilisis sem')
    db.dindex.insert( f0= 'pa615', f1= '(615)Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit amet, consectetur elit.')
    db.dindex.insert( f0= 'aa616', f1= '(616)3 Comments')
    db.dindex.insert( f0= 'di620', f1= '(620)Adventure')
    db.dindex.insert( f0= 'hh621', f1= '(621)Suspendisse ut justo tem por, rutrum')
    db.dindex.insert( f0= 'pa622', f1= '(622)Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit amet, consectetur elit.')
    db.dindex.insert( f0= 'aa623', f1= '(623)3 Comments')
    db.dindex.insert( f0= 'di626', f1= '(626)Tournaments')
    db.dindex.insert( f0= 'di627', f1= '(627)Premium Tournament')
    db.dindex.insert( f0= 'hh629', f1= '(629)World Of WarCraft')
    db.dindex.insert( f0= 'sp630', f1= '(630)Tournament Beggins:')
    db.dindex.insert( f0= 'sp632', f1= '(632)Tounament Ends:')
    db.dindex.insert( f0= 'sp634', f1= '(634)Participants:')
    db.dindex.insert( f0= 'sp635', f1= '(635)Tournament Author:')
    db.dindex.insert( f0= 'sp636', f1= '(636)Prizes:')
    db.dindex.insert( f0= 'pc637', f1= '(637)1st place $2000, 2nd place: $1000, 3rd place: $500')
    db.dindex.insert( f0= 'di638', f1= '(638)Premium Tournament')
    db.dindex.insert( f0= 'hh640', f1= '(640)DOOM')
    db.dindex.insert( f0= 'sp641', f1= '(641)Tournament Beggins:')
    db.dindex.insert( f0= 'sp643', f1= '(643)Tounament Ends:')
    db.dindex.insert( f0= 'sp645', f1= '(645)Participants:')
    db.dindex.insert( f0= 'sp646', f1= '(646)Tournament Author:')
    db.dindex.insert( f0= 'sp647', f1= '(647)Prizes:')
    db.dindex.insert( f0= 'pc648', f1= '(648)1st place $2000, 2nd place: $1000, 3rd place: $500')
    db.dindex.insert( f0= 'di650', f1= '(650)new')
    db.dindex.insert( f0= 'hh651', f1= '(651)Recent Reviews')
    db.dindex.insert( f0= 'di653', f1= '(653)9.3')
    db.dindex.insert( f0= 'hh654', f1= '(654)Assasins Creed')
    db.dindex.insert( f0= 'pa655', f1= '(655)Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame.')
    db.dindex.insert( f0= 'di657', f1= '(657)9.5')
    db.dindex.insert( f0= 'hh658', f1= '(658)Doom')
    db.dindex.insert( f0= 'pa659', f1= '(659)Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame.')
    db.dindex.insert( f0= 'di661', f1= '(661)9.1')
    db.dindex.insert( f0= 'hh662', f1= '(662)Overwatch')
    db.dindex.insert( f0= 'pa663', f1= '(663)Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame.')
    db.dindex.insert( f0= 'di665', f1= '(665)9.7')
    db.dindex.insert( f0= 'hh666', f1= '(666)GTA')
    db.dindex.insert( f0= 'pa667', f1= '(667)Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame.')
    db.dindex.insert( f0= 'pa670', f1= '(670)Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame.')
    db.dindex.insert( f0= 'hd671', f1= '(671)Latest Posts')
    db.dindex.insert( f0= 'di673', f1= '(673)June 21, 2018')
    db.dindex.insert( f0= 'pa674', f1= '(674)Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum')
    db.dindex.insert( f0= 'aa675', f1= '(675)By Admin')
    db.dindex.insert( f0= 'di677', f1= '(677)June 21, 2018')
    db.dindex.insert( f0= 'pa678', f1= '(678)Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum')
    db.dindex.insert( f0= 'aa679', f1= '(679)By Admin')
    db.dindex.insert( f0= 'di681', f1= '(681)June 21, 2018')
    db.dindex.insert( f0= 'pa682', f1= '(682)Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum')
    db.dindex.insert( f0= 'aa683', f1= '(683)By Admin')
    db.dindex.insert( f0= 'hd684', f1= '(684)Top Comments')
    db.dindex.insert( f0= 'sp686', f1= '(686)on')
    db.dindex.insert( f0= 'pc687', f1= '(687)Lorem ipsum dolor sit amet, co')
    db.dindex.insert( f0= 'aa688', f1= '(688)James Smith')
    db.dindex.insert( f0= 'di689', f1= '(689)June 21, 2018')
    db.dindex.insert( f0= 'sp691', f1= '(691)on')
    db.dindex.insert( f0= 'pc692', f1= '(692)Lorem ipsum dolor sit amet, co')
    db.dindex.insert( f0= 'aa693', f1= '(693)James Smith')
    db.dindex.insert( f0= 'di694', f1= '(694)June 21, 2018')
    db.dindex.insert( f0= 'sp696', f1= '(696)on')
    db.dindex.insert( f0= 'pc697', f1= '(697)Lorem ipsum dolor sit amet, co')
    db.dindex.insert( f0= 'aa698', f1= '(698)James Smith')
    db.dindex.insert( f0= 'di699', f1= '(699)June 21, 2018')
    db.dindex.insert( f0= 'sp701', f1= '(701)on')
    db.dindex.insert( f0= 'pc702', f1= '(702)Lorem ipsum dolor sit amet, co')
    db.dindex.insert( f0= 'aa703', f1= '(703)James Smith')
    db.dindex.insert( f0= 'di704', f1= '(704)June 21, 2018')
    db.dindex.insert( f0= 'aa706', f1= '(706)Home')
    db.dindex.insert( f0= 'aa708', f1= '(708)Games')
    db.dindex.insert( f0= 'aa710', f1= '(710)Blog')
    db.dindex.insert( f0= 'aa712', f1= '(712)Forums')
    db.dindex.insert( f0= 'aa714', f1= '(714)Contact')
    db.commit()
#
