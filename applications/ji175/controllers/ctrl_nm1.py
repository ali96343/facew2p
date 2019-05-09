

#@auth.requires_login()
def mygrid(tnm):
   return SQLFORM.grid(db[tnm], deletable= True, user_signature=False,  buttons_placement = 'left', showbuttontext=False, csv=False )
# 


#@auth.requires_login()
def ctrlone10():
    #db.one10.f0.writable = True
    response.view = 'ctrl_nm1/ctrlone10.html'
    return dict(grid= mygrid('one10'))
#
