db.define_table( 'dproduct_editform1',
   Field( 'f0', requires=IS_IN_SET(['l1-289', 'l1-290', ]), default= 'l1-289', widget=SQLFORM.widgets.radio.widget),
   Field( 'f1', requires=IS_IN_SET(['l1-292', 'l1-293', ]), default= 'l1-292', widget=SQLFORM.widgets.radio.widget),
   Field( 'f2', requires=IS_IN_SET(['l1-295', 'l1-296', ]), default= 'l1-295', widget=SQLFORM.widgets.radio.widget),
   )