db.define_table( 'dproduct_editform2',
   Field( 'f0', requires=IS_IN_SET(['l1-812', 'l1-813', ]), default= 'l1-812', widget=SQLFORM.widgets.radio.widget),
   Field( 'f1', requires=IS_IN_SET(['l1-815', 'l1-816', ]), default= 'l1-815', widget=SQLFORM.widgets.radio.widget),
   Field( 'f2', requires=IS_IN_SET(['l1-818', 'l1-819', ]), default= 'l1-818', widget=SQLFORM.widgets.radio.widget),
   )