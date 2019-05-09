db.define_table( 'dform_generalform4',
   Field( 'f0', 'string', label= 'f0', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'f1', default= 'w2p f1' ), 
   Field( 'f2', 'string', label= 'f2', default= 'w2p f2' ), 
   Field( 'f3', requires=IS_IN_SET( ['l1-434','l1-435','l1-436'] ), default= 'l1-435' ),
   Field( 'f4', requires=IS_IN_SET( ['l1-437','l1-438','l1-439'] ), default= 'l1-438' ),
   )