

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
    form.element('textarea[name=replace]')['_rows']='4'
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
def inline():
    db.dinline.f0.writable = True
    response.view = 'myadd/inline.html'
    return dict(grid= mygrid('dinline'))
#


@auth.requires_login()
def blank():
    db.dblank.f0.writable = True
    response.view = 'myadd/blank.html'
    return dict(grid= mygrid('dblank'))
#


@auth.requires_login()
def advanced():
    db.dadvanced.f0.writable = True
    response.view = 'myadd/advanced.html'
    return dict(grid= mygrid('dadvanced'))
#


@auth.requires_login()
def modals():
    db.dmodals.f0.writable = True
    response.view = 'myadd/modals.html'
    return dict(grid= mygrid('dmodals'))
#


@auth.requires_login()
def invoice():
    db.dinvoice.f0.writable = True
    response.view = 'myadd/invoice.html'
    return dict(grid= mygrid('dinvoice'))
#


@auth.requires_login()
def pace():
    db.dpace.f0.writable = True
    response.view = 'myadd/pace.html'
    return dict(grid= mygrid('dpace'))
#


@auth.requires_login()
def simple():
    db.dsimple.f0.writable = True
    response.view = 'myadd/simple.html'
    return dict(grid= mygrid('dsimple'))
#


@auth.requires_login()
def collapsed_sidebar():
    db.dcollapsed0sidebar.f0.writable = True
    response.view = 'myadd/collapsed-sidebar.html'
    return dict(grid= mygrid('dcollapsed0sidebar'))
#


@auth.requires_login()
def boxed():
    db.dboxed.f0.writable = True
    response.view = 'myadd/boxed.html'
    return dict(grid= mygrid('dboxed'))
#


@auth.requires_login()
def buttons():
    db.dbuttons.f0.writable = True
    response.view = 'myadd/buttons.html'
    return dict(grid= mygrid('dbuttons'))
#


@auth.requires_login()
def editors():
    db.deditors.f0.writable = True
    response.view = 'myadd/editors.html'
    return dict(grid= mygrid('deditors'))
#


@auth.requires_login()
def morris():
    db.dmorris.f0.writable = True
    response.view = 'myadd/morris.html'
    return dict(grid= mygrid('dmorris'))
#


@auth.requires_login()
def chartjs():
    db.dchartjs.f0.writable = True
    response.view = 'myadd/chartjs.html'
    return dict(grid= mygrid('dchartjs'))
#


@auth.requires_login()
def icons():
    db.dicons.f0.writable = True
    response.view = 'myadd/icons.html'
    return dict(grid= mygrid('dicons'))
#


@auth.requires_login()
def index2():
    db.dindex2.f0.writable = True
    response.view = 'myadd/index2.html'
    return dict(grid= mygrid('dindex2'))
#


@auth.requires_login()
def login():
    db.dlogin.f0.writable = True
    response.view = 'myadd/login.html'
    return dict(grid= mygrid('dlogin'))
#


@auth.requires_login()
def mailbox():
    db.dmailbox.f0.writable = True
    response.view = 'myadd/mailbox.html'
    return dict(grid= mygrid('dmailbox'))
#


@auth.requires_login()
def lockscreen():
    db.dlockscreen.f0.writable = True
    response.view = 'myadd/lockscreen.html'
    return dict(grid= mygrid('dlockscreen'))
#


@auth.requires_login()
def sliders():
    db.dsliders.f0.writable = True
    response.view = 'myadd/sliders.html'
    return dict(grid= mygrid('dsliders'))
#


@auth.requires_login()
def profile():
    db.dprofile.f0.writable = True
    response.view = 'myadd/profile.html'
    return dict(grid= mygrid('dprofile'))
#


@auth.requires_login()
def fixed():
    db.dfixed.f0.writable = True
    response.view = 'myadd/fixed.html'
    return dict(grid= mygrid('dfixed'))
#


@auth.requires_login()
def timeline():
    db.dtimeline.f0.writable = True
    response.view = 'myadd/timeline.html'
    return dict(grid= mygrid('dtimeline'))
#


@auth.requires_login()
def register():
    db.dregister.f0.writable = True
    response.view = 'myadd/register.html'
    return dict(grid= mygrid('dregister'))
#


@auth.requires_login()
def widgets():
    db.dwidgets.f0.writable = True
    response.view = 'myadd/widgets.html'
    return dict(grid= mygrid('dwidgets'))
#


@auth.requires_login()
def table_index1():
    db.dindex.f0.writable = True
    response.view = 'myadd/table_index1.html'
    return dict(grid= mygrid('dindex'))
#


@auth.requires_login()
def calendar():
    db.dcalendar.f0.writable = True
    response.view = 'myadd/calendar.html'
    return dict(grid= mygrid('dcalendar'))
#


@auth.requires_login()
def X500():
    db.d500.f0.writable = True
    response.view = 'myadd/500.html'
    return dict(grid= mygrid('d500'))
#


@auth.requires_login()
def top_nav():
    db.dtop0nav.f0.writable = True
    response.view = 'myadd/top-nav.html'
    return dict(grid= mygrid('dtop0nav'))
#


@auth.requires_login()
def general():
    db.dgeneral.f0.writable = True
    response.view = 'myadd/general.html'
    return dict(grid= mygrid('dgeneral'))
#


@auth.requires_login()
def starter():
    db.dstarter.f0.writable = True
    response.view = 'myadd/starter.html'
    return dict(grid= mygrid('dstarter'))
#


@auth.requires_login()
def flot():
    db.dflot.f0.writable = True
    response.view = 'myadd/flot.html'
    return dict(grid= mygrid('dflot'))
#


@auth.requires_login()
def data():
    db.ddata.f0.writable = True
    response.view = 'myadd/data.html'
    return dict(grid= mygrid('ddata'))
#


@auth.requires_login()
def X404():
    db.d404.f0.writable = True
    response.view = 'myadd/404.html'
    return dict(grid= mygrid('d404'))
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
def datatable0ctrl():
    response.view = 'myadd/datatable0ctrl.html'
    return dict(grid= mygrid('datatable0'))
#


@auth.requires_login()
def datatable1ctrl():
    response.view = 'myadd/datatable1ctrl.html'
    return dict(grid= mygrid('datatable1'))
#


@auth.requires_login()
def invoicetable0ctrl():
    response.view = 'myadd/invoicetable0ctrl.html'
    return dict(grid= mygrid('invoicetable0'))
#


@auth.requires_login()
def index2table0ctrl():
    response.view = 'myadd/index2table0ctrl.html'
    return dict(grid= mygrid('index2table0'))
#


@auth.requires_login()
def dboxedform0ctrl():
    response.view = 'myadd/dboxedform0ctrl.html'
    return dict(grid= mygrid('dboxedform0'))
#


@auth.requires_login()
def dboxedform1ctrl():
    response.view = 'myadd/dboxedform1ctrl.html'
    return dict(grid= mygrid('dboxedform1'))
#


@auth.requires_login()
def dfixedform0ctrl():
    response.view = 'myadd/dfixedform0ctrl.html'
    return dict(grid= mygrid('dfixedform0'))
#


@auth.requires_login()
def dfixedform1ctrl():
    response.view = 'myadd/dfixedform1ctrl.html'
    return dict(grid= mygrid('dfixedform1'))
#


@auth.requires_login()
def dadvancedform0ctrl():
    response.view = 'myadd/dadvancedform0ctrl.html'
    return dict(grid= mygrid('dadvancedform0'))
#


@auth.requires_login()
def dadvancedform1ctrl():
    response.view = 'myadd/dadvancedform1ctrl.html'
    return dict(grid= mygrid('dadvancedform1'))
#


@auth.requires_login()
def dX404form0ctrl():
    response.view = 'myadd/dX404form0ctrl.html'
    return dict(grid= mygrid('dX404form0'))
#


@auth.requires_login()
def dX404form1ctrl():
    response.view = 'myadd/dX404form1ctrl.html'
    return dict(grid= mygrid('dX404form1'))
#


@auth.requires_login()
def dX404form2ctrl():
    response.view = 'myadd/dX404form2ctrl.html'
    return dict(grid= mygrid('dX404form2'))
#


@auth.requires_login()
def dcollapsed_sidebarform0ctrl():
    response.view = 'myadd/dcollapsed_sidebarform0ctrl.html'
    return dict(grid= mygrid('dcollapsed_sidebarform0'))
#


@auth.requires_login()
def dcollapsed_sidebarform1ctrl():
    response.view = 'myadd/dcollapsed_sidebarform1ctrl.html'
    return dict(grid= mygrid('dcollapsed_sidebarform1'))
#


@auth.requires_login()
def dstarterform0ctrl():
    response.view = 'myadd/dstarterform0ctrl.html'
    return dict(grid= mygrid('dstarterform0'))
#


@auth.requires_login()
def dstarterform1ctrl():
    response.view = 'myadd/dstarterform1ctrl.html'
    return dict(grid= mygrid('dstarterform1'))
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
def dindexform2ctrl():
    response.view = 'myadd/dindexform2ctrl.html'
    return dict(grid= mygrid('dindexform2'))
#


@auth.requires_login()
def dgeneralform0ctrl():
    response.view = 'myadd/dgeneralform0ctrl.html'
    return dict(grid= mygrid('dgeneralform0'))
#


@auth.requires_login()
def dgeneralform1ctrl():
    response.view = 'myadd/dgeneralform1ctrl.html'
    return dict(grid= mygrid('dgeneralform1'))
#


@auth.requires_login()
def dbuttonsform0ctrl():
    response.view = 'myadd/dbuttonsform0ctrl.html'
    return dict(grid= mygrid('dbuttonsform0'))
#


@auth.requires_login()
def dbuttonsform1ctrl():
    response.view = 'myadd/dbuttonsform1ctrl.html'
    return dict(grid= mygrid('dbuttonsform1'))
#


@auth.requires_login()
def dtimelineform0ctrl():
    response.view = 'myadd/dtimelineform0ctrl.html'
    return dict(grid= mygrid('dtimelineform0'))
#


@auth.requires_login()
def dtimelineform1ctrl():
    response.view = 'myadd/dtimelineform1ctrl.html'
    return dict(grid= mygrid('dtimelineform1'))
#


@auth.requires_login()
def dsimpleform0ctrl():
    response.view = 'myadd/dsimpleform0ctrl.html'
    return dict(grid= mygrid('dsimpleform0'))
#


@auth.requires_login()
def dsimpleform1ctrl():
    response.view = 'myadd/dsimpleform1ctrl.html'
    return dict(grid= mygrid('dsimpleform1'))
#


@auth.requires_login()
def ddataform0ctrl():
    response.view = 'myadd/ddataform0ctrl.html'
    return dict(grid= mygrid('ddataform0'))
#


@auth.requires_login()
def ddataform1ctrl():
    response.view = 'myadd/ddataform1ctrl.html'
    return dict(grid= mygrid('ddataform1'))
#


@auth.requires_login()
def dinlineform0ctrl():
    response.view = 'myadd/dinlineform0ctrl.html'
    return dict(grid= mygrid('dinlineform0'))
#


@auth.requires_login()
def dinlineform1ctrl():
    response.view = 'myadd/dinlineform1ctrl.html'
    return dict(grid= mygrid('dinlineform1'))
#


@auth.requires_login()
def dloginform0ctrl():
    response.view = 'myadd/dloginform0ctrl.html'
    return dict(grid= mygrid('dloginform0'))
#


@auth.requires_login()
def dprofileform0ctrl():
    response.view = 'myadd/dprofileform0ctrl.html'
    return dict(grid= mygrid('dprofileform0'))
#


@auth.requires_login()
def dprofileform1ctrl():
    response.view = 'myadd/dprofileform1ctrl.html'
    return dict(grid= mygrid('dprofileform1'))
#


@auth.requires_login()
def dprofileform2ctrl():
    response.view = 'myadd/dprofileform2ctrl.html'
    return dict(grid= mygrid('dprofileform2'))
#


@auth.requires_login()
def dprofileform3ctrl():
    response.view = 'myadd/dprofileform3ctrl.html'
    return dict(grid= mygrid('dprofileform3'))
#


@auth.requires_login()
def deditorsform0ctrl():
    response.view = 'myadd/deditorsform0ctrl.html'
    return dict(grid= mygrid('deditorsform0'))
#


@auth.requires_login()
def deditorsform1ctrl():
    response.view = 'myadd/deditorsform1ctrl.html'
    return dict(grid= mygrid('deditorsform1'))
#


@auth.requires_login()
def deditorsform2ctrl():
    response.view = 'myadd/deditorsform2ctrl.html'
    return dict(grid= mygrid('deditorsform2'))
#


@auth.requires_login()
def deditorsform3ctrl():
    response.view = 'myadd/deditorsform3ctrl.html'
    return dict(grid= mygrid('deditorsform3'))
#


@auth.requires_login()
def dinvoiceform0ctrl():
    response.view = 'myadd/dinvoiceform0ctrl.html'
    return dict(grid= mygrid('dinvoiceform0'))
#


@auth.requires_login()
def dinvoiceform1ctrl():
    response.view = 'myadd/dinvoiceform1ctrl.html'
    return dict(grid= mygrid('dinvoiceform1'))
#


@auth.requires_login()
def dlockscreenform0ctrl():
    response.view = 'myadd/dlockscreenform0ctrl.html'
    return dict(grid= mygrid('dlockscreenform0'))
#


@auth.requires_login()
def dblankform0ctrl():
    response.view = 'myadd/dblankform0ctrl.html'
    return dict(grid= mygrid('dblankform0'))
#


@auth.requires_login()
def dblankform1ctrl():
    response.view = 'myadd/dblankform1ctrl.html'
    return dict(grid= mygrid('dblankform1'))
#


@auth.requires_login()
def dmorrisform0ctrl():
    response.view = 'myadd/dmorrisform0ctrl.html'
    return dict(grid= mygrid('dmorrisform0'))
#


@auth.requires_login()
def dmorrisform1ctrl():
    response.view = 'myadd/dmorrisform1ctrl.html'
    return dict(grid= mygrid('dmorrisform1'))
#


@auth.requires_login()
def diconsform0ctrl():
    response.view = 'myadd/diconsform0ctrl.html'
    return dict(grid= mygrid('diconsform0'))
#


@auth.requires_login()
def diconsform1ctrl():
    response.view = 'myadd/diconsform1ctrl.html'
    return dict(grid= mygrid('diconsform1'))
#


@auth.requires_login()
def dtop_navform0ctrl():
    response.view = 'myadd/dtop_navform0ctrl.html'
    return dict(grid= mygrid('dtop_navform0'))
#


@auth.requires_login()
def dmailboxform0ctrl():
    response.view = 'myadd/dmailboxform0ctrl.html'
    return dict(grid= mygrid('dmailboxform0'))
#


@auth.requires_login()
def dmailboxform1ctrl():
    response.view = 'myadd/dmailboxform1ctrl.html'
    return dict(grid= mygrid('dmailboxform1'))
#


@auth.requires_login()
def dpaceform0ctrl():
    response.view = 'myadd/dpaceform0ctrl.html'
    return dict(grid= mygrid('dpaceform0'))
#


@auth.requires_login()
def dpaceform1ctrl():
    response.view = 'myadd/dpaceform1ctrl.html'
    return dict(grid= mygrid('dpaceform1'))
#


@auth.requires_login()
def dflotform0ctrl():
    response.view = 'myadd/dflotform0ctrl.html'
    return dict(grid= mygrid('dflotform0'))
#


@auth.requires_login()
def dflotform1ctrl():
    response.view = 'myadd/dflotform1ctrl.html'
    return dict(grid= mygrid('dflotform1'))
#


@auth.requires_login()
def dchartjsform0ctrl():
    response.view = 'myadd/dchartjsform0ctrl.html'
    return dict(grid= mygrid('dchartjsform0'))
#


@auth.requires_login()
def dchartjsform1ctrl():
    response.view = 'myadd/dchartjsform1ctrl.html'
    return dict(grid= mygrid('dchartjsform1'))
#


@auth.requires_login()
def dwidgetsform0ctrl():
    response.view = 'myadd/dwidgetsform0ctrl.html'
    return dict(grid= mygrid('dwidgetsform0'))
#


@auth.requires_login()
def dwidgetsform1ctrl():
    response.view = 'myadd/dwidgetsform1ctrl.html'
    return dict(grid= mygrid('dwidgetsform1'))
#


@auth.requires_login()
def dwidgetsform2ctrl():
    response.view = 'myadd/dwidgetsform2ctrl.html'
    return dict(grid= mygrid('dwidgetsform2'))
#


@auth.requires_login()
def dwidgetsform3ctrl():
    response.view = 'myadd/dwidgetsform3ctrl.html'
    return dict(grid= mygrid('dwidgetsform3'))
#


@auth.requires_login()
def dwidgetsform4ctrl():
    response.view = 'myadd/dwidgetsform4ctrl.html'
    return dict(grid= mygrid('dwidgetsform4'))
#


@auth.requires_login()
def dwidgetsform5ctrl():
    response.view = 'myadd/dwidgetsform5ctrl.html'
    return dict(grid= mygrid('dwidgetsform5'))
#


@auth.requires_login()
def dwidgetsform6ctrl():
    response.view = 'myadd/dwidgetsform6ctrl.html'
    return dict(grid= mygrid('dwidgetsform6'))
#


@auth.requires_login()
def dwidgetsform7ctrl():
    response.view = 'myadd/dwidgetsform7ctrl.html'
    return dict(grid= mygrid('dwidgetsform7'))
#


@auth.requires_login()
def dslidersform0ctrl():
    response.view = 'myadd/dslidersform0ctrl.html'
    return dict(grid= mygrid('dslidersform0'))
#


@auth.requires_login()
def dslidersform1ctrl():
    response.view = 'myadd/dslidersform1ctrl.html'
    return dict(grid= mygrid('dslidersform1'))
#


@auth.requires_login()
def dregisterform0ctrl():
    response.view = 'myadd/dregisterform0ctrl.html'
    return dict(grid= mygrid('dregisterform0'))
#


@auth.requires_login()
def dmodalsform0ctrl():
    response.view = 'myadd/dmodalsform0ctrl.html'
    return dict(grid= mygrid('dmodalsform0'))
#


@auth.requires_login()
def dmodalsform1ctrl():
    response.view = 'myadd/dmodalsform1ctrl.html'
    return dict(grid= mygrid('dmodalsform1'))
#


@auth.requires_login()
def dcalendarform0ctrl():
    response.view = 'myadd/dcalendarform0ctrl.html'
    return dict(grid= mygrid('dcalendarform0'))
#


@auth.requires_login()
def dcalendarform1ctrl():
    response.view = 'myadd/dcalendarform1ctrl.html'
    return dict(grid= mygrid('dcalendarform1'))
#


@auth.requires_login()
def dindex2form0ctrl():
    response.view = 'myadd/dindex2form0ctrl.html'
    return dict(grid= mygrid('dindex2form0'))
#


@auth.requires_login()
def dindex2form1ctrl():
    response.view = 'myadd/dindex2form1ctrl.html'
    return dict(grid= mygrid('dindex2form1'))
#


@auth.requires_login()
def dindex2form2ctrl():
    response.view = 'myadd/dindex2form2ctrl.html'
    return dict(grid= mygrid('dindex2form2'))
#


@auth.requires_login()
def dX500form0ctrl():
    response.view = 'myadd/dX500form0ctrl.html'
    return dict(grid= mygrid('dX500form0'))
#


@auth.requires_login()
def dX500form1ctrl():
    response.view = 'myadd/dX500form1ctrl.html'
    return dict(grid= mygrid('dX500form1'))
#


@auth.requires_login()
def dX500form2ctrl():
    response.view = 'myadd/dX500form2ctrl.html'
    return dict(grid= mygrid('dX500form2'))
#
