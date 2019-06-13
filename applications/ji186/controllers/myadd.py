

@auth.requires_login()
def mygrid(tnm):
   return SQLFORM.grid(db[tnm], deletable= False, user_signature=False,  buttons_placement = 'left', showbuttontext=False, csv=False )
# 

@auth.requires_login()
def search_site():
    import os
    form = SQLFORM.factory(
       Field('search', label='search for unique text ( or number label) from screen', requires=IS_NOT_EMPTY(),  ),
       Field('replace', 'text', label='replace with new text', requires=IS_NOT_EMPTY(), length= 1000, ),
       )
    if form.process( keepvalues = True  ).accepted: 
        search  = form.vars.search
        replace  = form.vars.replace
        replace=replace.strip()
        for table in db.tables():
             if any (['auth_' in table, 'form' in table,  not 'f1' in db[table].fields]) :
                     continue
             qu= db[table].f1.contains(search)
             rows = db(qu).select()
             if rows:
               if len(rows) == 1:
                 row = db(qu).select().first()
                 if row:
                    #session.flash = 'found!! %s' % row.f1
                    savef1= row.f1
                    db(db[table].id == row.id).update( f1= replace, f2= savef1  )
                    response.flash = 'replaced, found == 1!'
                    break
               else:
                    response.flash = 'do not replaced, found > 1!'
                    break
    elif form.errors:
        response.flash = 'Please correct the error(s).'
    else: 
        response.flash = 'Insert data please - no fields can be empty.' 
    return form


#https://stackoverflow.com/questions/37806801/can-not-post-data-via-ajax-to-web2py-rest-api-possible-cors-issue/37859336
#url_name='https://sun.minfindnr.ru/ji15/default/api/t0_tables.json'
#url_name='https://sun.minfindnr.ru/ji15/default/api/patterns.json'

@auth.requires_login()
@request.restful()
def api():
    from gluon.serializers import json
    response.view = 'generic.' + request.extension
    def GET(*args,**vars):
         patterns = 'auto'
         parser = db.parse_as_rest(patterns,args,vars)
         if parser.status == 200:
            return dict(content=parser.response)
         else:
            raise HTTP(parser.status,parser.error)
    def POST(table_name,**vars):
        #return db[table_name].validate_and_insert(**vars)
        #data = gluon.contrib.simplejson.loads(request.body.read())
        return json(db[table_name].validate_and_insert(**vars))
        return dict()
    def PUT(table_name,record_id,**vars):
        return db(db[table_name]._id==record_id).update(**vars)
    def DELETE(table_name,record_id):
        return db(db[table_name]._id==record_id).delete()
    def OPTIONS(*args,**vars):
        print ( 'OPTION called') 
        return True
    return dict(GET=GET,POST=POST,PUT=PUT,DELETE=DELETE,OPTIONS=OPTIONS)


@auth.requires_login()
def index():
    response.view = 'myadd/index.html'
    return dict(form=search_site())



@auth.requires_login()
def grid():
    db.dgrid.f0.writable = True
    response.view = 'myadd/grid.html'
    return dict(grid= mygrid('dgrid'))
#


@auth.requires_login()
def switch():
    db.dswitch.f0.writable = True
    response.view = 'myadd/switch.html'
    return dict(grid= mygrid('dswitch'))
#


@auth.requires_login()
def form():
    db.dform.f0.writable = True
    response.view = 'myadd/form.html'
    return dict(grid= mygrid('dform'))
#


@auth.requires_login()
def index4():
    db.dindex4.f0.writable = True
    response.view = 'myadd/index4.html'
    return dict(grid= mygrid('dindex4'))
#


@auth.requires_login()
def index2():
    db.dindex2.f0.writable = True
    response.view = 'myadd/index2.html'
    return dict(grid= mygrid('dindex2'))
#


@auth.requires_login()
def chart():
    db.dchart.f0.writable = True
    response.view = 'myadd/chart.html'
    return dict(grid= mygrid('dchart'))
#


@auth.requires_login()
def login():
    db.dlogin.f0.writable = True
    response.view = 'myadd/login.html'
    return dict(grid= mygrid('dlogin'))
#


@auth.requires_login()
def index3():
    db.dindex3.f0.writable = True
    response.view = 'myadd/index3.html'
    return dict(grid= mygrid('dindex3'))
#


@auth.requires_login()
def alert():
    db.dalert.f0.writable = True
    response.view = 'myadd/alert.html'
    return dict(grid= mygrid('dalert'))
#


@auth.requires_login()
def modal():
    db.dmodal.f0.writable = True
    response.view = 'myadd/modal.html'
    return dict(grid= mygrid('dmodal'))
#


@auth.requires_login()
def register():
    db.dregister.f0.writable = True
    response.view = 'myadd/register.html'
    return dict(grid= mygrid('dregister'))
#


@auth.requires_login()
def progress_bar():
    db.dprogress0bar.f0.writable = True
    response.view = 'myadd/progress-bar.html'
    return dict(grid= mygrid('dprogress0bar'))
#


@auth.requires_login()
def table():
    db.dtable.f0.writable = True
    response.view = 'myadd/table.html'
    return dict(grid= mygrid('dtable'))
#


@auth.requires_login()
def tab():
    db.dtab.f0.writable = True
    response.view = 'myadd/tab.html'
    return dict(grid= mygrid('dtab'))
#


@auth.requires_login()
def badge():
    db.dbadge.f0.writable = True
    response.view = 'myadd/badge.html'
    return dict(grid= mygrid('dbadge'))
#


@auth.requires_login()
def table_index1():
    db.dindex.f0.writable = True
    response.view = 'myadd/table_index1.html'
    return dict(grid= mygrid('dindex'))
#


@auth.requires_login()
def inbox():
    db.dinbox.f0.writable = True
    response.view = 'myadd/inbox.html'
    return dict(grid= mygrid('dinbox'))
#


@auth.requires_login()
def map():
    db.dmap.f0.writable = True
    response.view = 'myadd/map.html'
    return dict(grid= mygrid('dmap'))
#


@auth.requires_login()
def typo():
    db.dtypo.f0.writable = True
    response.view = 'myadd/typo.html'
    return dict(grid= mygrid('dtypo'))
#


@auth.requires_login()
def forget_pass():
    db.dforget0pass.f0.writable = True
    response.view = 'myadd/forget-pass.html'
    return dict(grid= mygrid('dforget0pass'))
#


@auth.requires_login()
def card():
    db.dcard.f0.writable = True
    response.view = 'myadd/card.html'
    return dict(grid= mygrid('dcard'))
#


@auth.requires_login()
def fontawesome():
    db.dfontawesome.f0.writable = True
    response.view = 'myadd/fontawesome.html'
    return dict(grid= mygrid('dfontawesome'))
#


@auth.requires_login()
def button():
    db.dbutton.f0.writable = True
    response.view = 'myadd/button.html'
    return dict(grid= mygrid('dbutton'))
#


@auth.requires_login()
def auth_eventctrl():
    response.view = 'myadd/auth_eventctrl.html'
    return dict(grid= mygrid('auth_event'))
#


@auth.requires_login()
def auth_userctrl():
    response.view = 'myadd/auth_userctrl.html'
    return dict(grid= mygrid('auth_user'))
#


@auth.requires_login()
def auth_groupctrl():
    response.view = 'myadd/auth_groupctrl.html'
    return dict(grid= mygrid('auth_group'))
#


@auth.requires_login()
def auth_membershipctrl():
    response.view = 'myadd/auth_membershipctrl.html'
    return dict(grid= mygrid('auth_membership'))
#


@auth.requires_login()
def indextable0ctrl():
    response.view = 'myadd/indextable0ctrl.html'
    return dict(grid= mygrid('indextable0'))
#


@auth.requires_login()
def tabletable0ctrl():
    response.view = 'myadd/tabletable0ctrl.html'
    return dict(grid= mygrid('tabletable0'))
#


@auth.requires_login()
def index4table0ctrl():
    response.view = 'myadd/index4table0ctrl.html'
    return dict(grid= mygrid('index4table0'))
#


@auth.requires_login()
def switchtable0ctrl():
    response.view = 'myadd/switchtable0ctrl.html'
    return dict(grid= mygrid('switchtable0'))
#


@auth.requires_login()
def index2table0ctrl():
    response.view = 'myadd/index2table0ctrl.html'
    return dict(grid= mygrid('index2table0'))
#


@auth.requires_login()
def dtypoform0ctrl():
    response.view = 'myadd/dtypoform0ctrl.html'
    return dict(grid= mygrid('dtypoform0'))
#


@auth.requires_login()
def dtabform0ctrl():
    response.view = 'myadd/dtabform0ctrl.html'
    return dict(grid= mygrid('dtabform0'))
#


@auth.requires_login()
def dprogress_barform0ctrl():
    response.view = 'myadd/dprogress_barform0ctrl.html'
    return dict(grid= mygrid('dprogress_barform0'))
#


@auth.requires_login()
def dindex3form0ctrl():
    response.view = 'myadd/dindex3form0ctrl.html'
    return dict(grid= mygrid('dindex3form0'))
#


@auth.requires_login()
def dmodalform0ctrl():
    response.view = 'myadd/dmodalform0ctrl.html'
    return dict(grid= mygrid('dmodalform0'))
#


@auth.requires_login()
def dforget_passform0ctrl():
    response.view = 'myadd/dforget_passform0ctrl.html'
    return dict(grid= mygrid('dforget_passform0'))
#


@auth.requires_login()
def dindexform0ctrl():
    response.view = 'myadd/dindexform0ctrl.html'
    return dict(grid= mygrid('dindexform0'))
#


@auth.requires_login()
def dindexform1ctrl():
    response.view = 'myadd/dindexform1ctrl.html'
    return dict(grid= mygrid('dindexform1'))
#


@auth.requires_login()
def dbuttonform0ctrl():
    response.view = 'myadd/dbuttonform0ctrl.html'
    return dict(grid= mygrid('dbuttonform0'))
#


@auth.requires_login()
def dtableform0ctrl():
    response.view = 'myadd/dtableform0ctrl.html'
    return dict(grid= mygrid('dtableform0'))
#


@auth.requires_login()
def dloginform0ctrl():
    response.view = 'myadd/dloginform0ctrl.html'
    return dict(grid= mygrid('dloginform0'))
#


@auth.requires_login()
def dindex4form0ctrl():
    response.view = 'myadd/dindex4form0ctrl.html'
    return dict(grid= mygrid('dindex4form0'))
#


@auth.requires_login()
def dindex4form1ctrl():
    response.view = 'myadd/dindex4form1ctrl.html'
    return dict(grid= mygrid('dindex4form1'))
#


@auth.requires_login()
def dgridform0ctrl():
    response.view = 'myadd/dgridform0ctrl.html'
    return dict(grid= mygrid('dgridform0'))
#


@auth.requires_login()
def dcardform0ctrl():
    response.view = 'myadd/dcardform0ctrl.html'
    return dict(grid= mygrid('dcardform0'))
#


@auth.requires_login()
def dalertform0ctrl():
    response.view = 'myadd/dalertform0ctrl.html'
    return dict(grid= mygrid('dalertform0'))
#


@auth.requires_login()
def dswitchform0ctrl():
    response.view = 'myadd/dswitchform0ctrl.html'
    return dict(grid= mygrid('dswitchform0'))
#


@auth.requires_login()
def dfontawesomeform0ctrl():
    response.view = 'myadd/dfontawesomeform0ctrl.html'
    return dict(grid= mygrid('dfontawesomeform0'))
#


@auth.requires_login()
def dbadgeform0ctrl():
    response.view = 'myadd/dbadgeform0ctrl.html'
    return dict(grid= mygrid('dbadgeform0'))
#


@auth.requires_login()
def dmapform0ctrl():
    response.view = 'myadd/dmapform0ctrl.html'
    return dict(grid= mygrid('dmapform0'))
#


@auth.requires_login()
def dformform0ctrl():
    response.view = 'myadd/dformform0ctrl.html'
    return dict(grid= mygrid('dformform0'))
#


@auth.requires_login()
def dformform1ctrl():
    response.view = 'myadd/dformform1ctrl.html'
    return dict(grid= mygrid('dformform1'))
#


@auth.requires_login()
def dformform2ctrl():
    response.view = 'myadd/dformform2ctrl.html'
    return dict(grid= mygrid('dformform2'))
#


@auth.requires_login()
def dformform3ctrl():
    response.view = 'myadd/dformform3ctrl.html'
    return dict(grid= mygrid('dformform3'))
#


@auth.requires_login()
def dformform4ctrl():
    response.view = 'myadd/dformform4ctrl.html'
    return dict(grid= mygrid('dformform4'))
#


@auth.requires_login()
def dformform5ctrl():
    response.view = 'myadd/dformform5ctrl.html'
    return dict(grid= mygrid('dformform5'))
#


@auth.requires_login()
def dformform6ctrl():
    response.view = 'myadd/dformform6ctrl.html'
    return dict(grid= mygrid('dformform6'))
#


@auth.requires_login()
def dformform7ctrl():
    response.view = 'myadd/dformform7ctrl.html'
    return dict(grid= mygrid('dformform7'))
#


@auth.requires_login()
def dformform8ctrl():
    response.view = 'myadd/dformform8ctrl.html'
    return dict(grid= mygrid('dformform8'))
#


@auth.requires_login()
def dformform9ctrl():
    response.view = 'myadd/dformform9ctrl.html'
    return dict(grid= mygrid('dformform9'))
#


@auth.requires_login()
def dformform10ctrl():
    response.view = 'myadd/dformform10ctrl.html'
    return dict(grid= mygrid('dformform10'))
#


@auth.requires_login()
def dformform11ctrl():
    response.view = 'myadd/dformform11ctrl.html'
    return dict(grid= mygrid('dformform11'))
#


@auth.requires_login()
def dformform12ctrl():
    response.view = 'myadd/dformform12ctrl.html'
    return dict(grid= mygrid('dformform12'))
#


@auth.requires_login()
def dformform13ctrl():
    response.view = 'myadd/dformform13ctrl.html'
    return dict(grid= mygrid('dformform13'))
#


@auth.requires_login()
def dformform14ctrl():
    response.view = 'myadd/dformform14ctrl.html'
    return dict(grid= mygrid('dformform14'))
#


@auth.requires_login()
def dformform15ctrl():
    response.view = 'myadd/dformform15ctrl.html'
    return dict(grid= mygrid('dformform15'))
#


@auth.requires_login()
def dregisterform0ctrl():
    response.view = 'myadd/dregisterform0ctrl.html'
    return dict(grid= mygrid('dregisterform0'))
#


@auth.requires_login()
def dinboxform0ctrl():
    response.view = 'myadd/dinboxform0ctrl.html'
    return dict(grid= mygrid('dinboxform0'))
#


@auth.requires_login()
def dinboxform1ctrl():
    response.view = 'myadd/dinboxform1ctrl.html'
    return dict(grid= mygrid('dinboxform1'))
#


@auth.requires_login()
def dinboxform2ctrl():
    response.view = 'myadd/dinboxform2ctrl.html'
    return dict(grid= mygrid('dinboxform2'))
#


@auth.requires_login()
def dindex2form0ctrl():
    response.view = 'myadd/dindex2form0ctrl.html'
    return dict(grid= mygrid('dindex2form0'))
#


@auth.requires_login()
def dchartform0ctrl():
    response.view = 'myadd/dchartform0ctrl.html'
    return dict(grid= mygrid('dchartform0'))
#
