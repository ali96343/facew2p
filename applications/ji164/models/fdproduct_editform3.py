db.define_table( 'dproduct_editform3',
   Field( 'f0', requires=IS_IN_SET(['l1-307', 'l1-308', ]), default= 'l1-307', widget=SQLFORM.widgets.radio.widget),
   Field( 'f1', requires=IS_IN_SET(['l1-310', 'l1-311', ]), default= 'l1-310', widget=SQLFORM.widgets.radio.widget),
   Field( 'f2', requires=IS_IN_SET(['l1-313', 'l1-314', ]), default= 'l1-313', widget=SQLFORM.widgets.radio.widget),
   )