db.define_table( 'dform_generalform3',
   Field( 'f0', 'boolean', label= 'f0' , default= True), 
   Field( 'f1', 'boolean', label= 'f1' , default= True), 
   Field( 'f2', 'boolean', label= 'f2' , default= True), 
   Field( 'f3', 'boolean', label= 'f3' , default= True), 
   Field( 'f4', requires=IS_IN_SET(['l1-361', 'l1-362', ]), default= 'l1-361', widget=SQLFORM.widgets.radio.widget),
   Field( 'f5', requires=IS_IN_SET(['l1-364', 'l1-365', ]), default= 'l1-364', widget=SQLFORM.widgets.radio.widget),
   Field( 'f6', requires=IS_IN_SET(['l1-367', 'l1-368', ]), default= 'l1-367', widget=SQLFORM.widgets.radio.widget),
   Field( 'f7', requires=IS_IN_SET(['l1-370', 'l1-371', ]), default= 'l1-370', widget=SQLFORM.widgets.radio.widget),
   Field( 'f8', 'boolean', label= 'f8' , default= True), 
   Field( 'f9', 'boolean', label= 'f9' , default= True), 
   Field( 'f10', 'boolean', label= 'f10' , default= True), 
   Field( 'f11', 'boolean', label= 'f11' , default= True), 
   Field( 'f12', 'boolean', label= 'f12' , default= True), 
   Field( 'f13', 'boolean', label= 'f13' , default= True), 
   Field( 'f14', 'boolean', label= 'f14' , default= True), 
   Field( 'f15', 'boolean', label= 'f15' , default= True), 
   Field( 'f16', 'boolean', label= 'f16' , default= True), 
   Field( 'f17', 'boolean', label= 'f17' , default= True), 
   Field( 'f18', 'boolean', label= 'f18' , default= True), 
   Field( 'f19', 'boolean', label= 'f19' , default= True), 
   Field( 'f20', 'boolean', label= 'f20' , default= True), 
   )