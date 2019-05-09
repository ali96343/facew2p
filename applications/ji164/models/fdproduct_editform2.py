db.define_table( 'dproduct_editform2',
   Field( 'f0', requires=IS_IN_SET(['l1-298', 'l1-299', ]), default= 'l1-298', widget=SQLFORM.widgets.radio.widget),
   Field( 'f1', requires=IS_IN_SET(['l1-301', 'l1-302', ]), default= 'l1-301', widget=SQLFORM.widgets.radio.widget),
   Field( 'f2', requires=IS_IN_SET(['l1-304', 'l1-305', ]), default= 'l1-304', widget=SQLFORM.widgets.radio.widget),
   )