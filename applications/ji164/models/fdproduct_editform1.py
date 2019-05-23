db.define_table( 'dproduct_editform1',
   Field( 'f0', requires=IS_IN_SET(['l1-803', 'l1-804', ]), default= 'l1-803', widget=SQLFORM.widgets.radio.widget),
   Field( 'f1', requires=IS_IN_SET(['l1-806', 'l1-807', ]), default= 'l1-806', widget=SQLFORM.widgets.radio.widget),
   Field( 'f2', requires=IS_IN_SET(['l1-809', 'l1-810', ]), default= 'l1-809', widget=SQLFORM.widgets.radio.widget),
   )