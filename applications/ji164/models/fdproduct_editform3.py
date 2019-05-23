db.define_table( 'dproduct_editform3',
   Field( 'f0', requires=IS_IN_SET(['l1-821', 'l1-822', ]), default= 'l1-821', widget=SQLFORM.widgets.radio.widget),
   Field( 'f1', requires=IS_IN_SET(['l1-824', 'l1-825', ]), default= 'l1-824', widget=SQLFORM.widgets.radio.widget),
   Field( 'f2', requires=IS_IN_SET(['l1-827', 'l1-828', ]), default= 'l1-827', widget=SQLFORM.widgets.radio.widget),
   )