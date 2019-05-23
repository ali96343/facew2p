db.define_table( 'dformform2',
   Field( 'f0', 'string',  label= 'f0', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'f1', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'f2', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'f3', default= 'w2p f3' ), 
   Field( 'f4', requires=IS_IN_SET(['l1-601', 'l1-602', ]), default= 'l1-601', widget=SQLFORM.widgets.radio.widget),
   Field( 'f5', requires=IS_IN_SET(['l1-604', 'l1-605', ]), default= 'l1-604', widget=SQLFORM.widgets.radio.widget),
   Field( 'f6', requires=IS_IN_SET(['l1-607', 'l1-608', ]), default= 'l1-607', widget=SQLFORM.widgets.radio.widget),
   Field( 'f7', requires=IS_IN_SET(['l1-610', 'l1-611', ]), default= 'l1-610', widget=SQLFORM.widgets.radio.widget),
   Field( 'f8', requires=IS_IN_SET(['l1-613', 'l1-614', ]), default= 'l1-613', widget=SQLFORM.widgets.radio.widget),
   Field( 'f9', requires=IS_IN_SET(['l1-616', 'l1-617', ]), default= 'l1-616', widget=SQLFORM.widgets.radio.widget),
   Field( 'f10', 'boolean', label= 'f10' , default= True), 
   Field( 'f11', 'boolean', label= 'f11' , default= True), 
   Field( 'f12', 'boolean', label= 'f12' , default= True), 
   Field( 'f13', 'boolean', label= 'f13' , default= True), 
   Field( 'f14', 'boolean', label= 'f14' , default= True), 
   Field( 'f15', 'boolean', label= 'f15' , default= True), 
   Field( 'f16', 'string',  label= 'f16', default= 'w2p f16' ), 
   Field( 'f17', 'string',  label= 'f17', default= 'w2p f17' ), 
   Field( 'f18', 'text',    label= 'f18' , default= 'w2p f18'), 
   Field( 'f19', requires=IS_IN_SET( ['l1-646','l1-647','l1-648'] ), default= 'l1-647' ),
   Field( 'f20', requires=IS_IN_SET( ['l1-649','l1-650','l1-651'] ), default= 'l1-650' ),
   Field( 'f21', requires=IS_IN_SET( ['l1-652','l1-653','l1-654'] ), default= 'l1-653' ),
   Field( 'f22', requires=IS_IN_SET( ['l1-655','l1-656','l1-657'] ), default= 'l1-656' ),
   Field( 'f23', requires=IS_IN_SET( ['l1-658','l1-659','l1-660'] ), default= 'l1-659' ),
   )