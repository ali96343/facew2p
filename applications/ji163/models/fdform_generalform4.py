db.define_table( 'dform_generalform4',
   Field( 'f0', 'string',  label= 'f0', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'f1', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'f2', default= 'w2p f2' ), 
   Field( 'f3', requires=IS_IN_SET( ['l1-904','l1-905','l1-906'] ), default= 'l1-905' ),
   Field( 'f4', requires=IS_IN_SET( ['l1-907','l1-908','l1-909'] ), default= 'l1-908' ),
   )