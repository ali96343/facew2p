

#@auth.requires_login()
def mygrid(tnm):
   return SQLFORM.grid(db[tnm], deletable= True, user_signature=False,  buttons_placement = 'left', showbuttontext=False, csv=False )
# 

#@auth.requires_login()
def index():
    response.view = 'ctrl_nm1/index.html'
    mydict=dict()
    return dict(mydict=mydict)


#@auth.requires_login()
def ctrlone10():
    #db.one10.f0.writable = True
    response.view = 'ctrl_nm1/ctrlone10.html'
    return dict(grid= mygrid('one10'))
#


#@auth.requires_login()
def ctrlo2m11o():
    #db.o2m11o.f0.writable = True
    response.view = 'ctrl_nm1/ctrlo2m11o.html'
    return dict(grid= mygrid('o2m11o'))
#


#@auth.requires_login()
def ctrlo2m12m():
    #db.o2m12m.f0.writable = True
    response.view = 'ctrl_nm1/ctrlo2m12m.html'
    return dict(grid= mygrid('o2m12m'))
#


#@auth.requires_login()
def ctrlm2m13():
    #db.m2m13.f0.writable = True
    response.view = 'ctrl_nm1/ctrlm2m13.html'
    return dict(grid= mygrid('m2m13'))
#


#@auth.requires_login()
def ctrlm2m14():
    #db.m2m14.f0.writable = True
    response.view = 'ctrl_nm1/ctrlm2m14.html'
    return dict(grid= mygrid('m2m14'))
#


#@auth.requires_login()
def ctrlm2m15ref():
    #db.m2m15ref.f0.writable = True
    response.view = 'ctrl_nm1/ctrlm2m15ref.html'
    return dict(grid= mygrid('m2m15ref'))
#
