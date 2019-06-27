db.define_table( 'dformIIelementsII2form1',
   Field( 'f0', 'string',  label= 'f0', default= 'w2p f0' ), 
   Field( 'f1', requires=IS_IN_SET( ['l1-876','l1-877','l1-878'] ), default= 'l1-877' ),
   Field( 'f2', requires=IS_IN_SET( ['l1-879','l1-880','l1-881'] ), default= 'l1-880' ),
   Field( 'f3', requires=IS_IN_SET( ['l1-882','l1-883','l1-884'] ), default= 'l1-883' ),
   )