

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
def twoIImenuII1():
    db.dtwo0menu01.f0.writable = True
    response.view = 'myadd/two-menu-1.html'
    return dict(grid= mygrid('dtwo0menu01'))
#


@auth.requires_login()
def formIIelementsII2():
    db.dform0elements02.f0.writable = True
    response.view = 'myadd/form-elements-2.html'
    return dict(grid= mygrid('dform0elements02'))
#


@auth.requires_login()
def mobileIImenuII2():
    db.dmobile0menu02.f0.writable = True
    response.view = 'myadd/mobile-menu-2.html'
    return dict(grid= mygrid('dmobile0menu02'))
#


@auth.requires_login()
def blank():
    db.dblank.f0.writable = True
    response.view = 'myadd/blank.html'
    return dict(grid= mygrid('dblank'))
#


@auth.requires_login()
def jqueryIIui():
    db.djquery0ui.f0.writable = True
    response.view = 'myadd/jquery-ui.html'
    return dict(grid= mygrid('djquery0ui'))
#


@auth.requires_login()
def pricing():
    db.dpricing.f0.writable = True
    response.view = 'myadd/pricing.html'
    return dict(grid= mygrid('dpricing'))
#


@auth.requires_login()
def grid():
    db.dgrid.f0.writable = True
    response.view = 'myadd/grid.html'
    return dict(grid= mygrid('dgrid'))
#


@auth.requires_login()
def mobileIImenuII1():
    db.dmobile0menu01.f0.writable = True
    response.view = 'myadd/mobile-menu-1.html'
    return dict(grid= mygrid('dmobile0menu01'))
#


@auth.requires_login()
def treeview():
    db.dtreeview.f0.writable = True
    response.view = 'myadd/treeview.html'
    return dict(grid= mygrid('dtreeview'))
#


@auth.requires_login()
def typography():
    db.dtypography.f0.writable = True
    response.view = 'myadd/typography.html'
    return dict(grid= mygrid('dtypography'))
#


@auth.requires_login()
def invoice():
    db.dinvoice.f0.writable = True
    response.view = 'myadd/invoice.html'
    return dict(grid= mygrid('dinvoice'))
#


@auth.requires_login()
def elements():
    db.delements.f0.writable = True
    response.view = 'myadd/elements.html'
    return dict(grid= mygrid('delements'))
#


@auth.requires_login()
def buttons():
    db.dbuttons.f0.writable = True
    response.view = 'myadd/buttons.html'
    return dict(grid= mygrid('dbuttons'))
#


@auth.requires_login()
def formIIwizard():
    db.dform0wizard.f0.writable = True
    response.view = 'myadd/form-wizard.html'
    return dict(grid= mygrid('dform0wizard'))
#


@auth.requires_login()
def search():
    db.dsearch.f0.writable = True
    response.view = 'myadd/search.html'
    return dict(grid= mygrid('dsearch'))
#


@auth.requires_login()
def emailIIcontrast():
    db.demail0contrast.f0.writable = True
    response.view = 'myadd/email-contrast.html'
    return dict(grid= mygrid('demail0contrast'))
#


@auth.requires_login()
def jqgrid():
    db.djqgrid.f0.writable = True
    response.view = 'myadd/jqgrid.html'
    return dict(grid= mygrid('djqgrid'))
#


@auth.requires_login()
def tables():
    db.dtables.f0.writable = True
    response.view = 'myadd/tables.html'
    return dict(grid= mygrid('dtables'))
#


@auth.requires_login()
def login():
    db.dlogin.f0.writable = True
    response.view = 'myadd/login.html'
    return dict(grid= mygrid('dlogin'))
#


@auth.requires_login()
def email():
    db.demail.f0.writable = True
    response.view = 'myadd/email.html'
    return dict(grid= mygrid('demail'))
#


@auth.requires_login()
def formIIelements():
    db.dform0elements.f0.writable = True
    response.view = 'myadd/form-elements.html'
    return dict(grid= mygrid('dform0elements'))
#


@auth.requires_login()
def emailIInavbar():
    db.demail0navbar.f0.writable = True
    response.view = 'myadd/email-navbar.html'
    return dict(grid= mygrid('demail0navbar'))
#


@auth.requires_login()
def profile():
    db.dprofile.f0.writable = True
    response.view = 'myadd/profile.html'
    return dict(grid= mygrid('dprofile'))
#


@auth.requires_login()
def topIImenu():
    db.dtop0menu.f0.writable = True
    response.view = 'myadd/top-menu.html'
    return dict(grid= mygrid('dtop0menu'))
#


@auth.requires_login()
def timeline():
    db.dtimeline.f0.writable = True
    response.view = 'myadd/timeline.html'
    return dict(grid= mygrid('dtimeline'))
#


@auth.requires_login()
def twoIImenuII2():
    db.dtwo0menu02.f0.writable = True
    response.view = 'myadd/two-menu-2.html'
    return dict(grid= mygrid('dtwo0menu02'))
#


@auth.requires_login()
def contentIIslider():
    db.dcontent0slider.f0.writable = True
    response.view = 'myadd/content-slider.html'
    return dict(grid= mygrid('dcontent0slider'))
#


@auth.requires_login()
def dropzone():
    db.ddropzone.f0.writable = True
    response.view = 'myadd/dropzone.html'
    return dict(grid= mygrid('ddropzone'))
#


@auth.requires_login()
def nestableIIlist():
    db.dnestable0list.f0.writable = True
    response.view = 'myadd/nestable-list.html'
    return dict(grid= mygrid('dnestable0list'))
#


@auth.requires_login()
def gallery():
    db.dgallery.f0.writable = True
    response.view = 'myadd/gallery.html'
    return dict(grid= mygrid('dgallery'))
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
def faq():
    db.dfaq.f0.writable = True
    response.view = 'myadd/faq.html'
    return dict(grid= mygrid('dfaq'))
#


@auth.requires_login()
def calendar():
    db.dcalendar.f0.writable = True
    response.view = 'myadd/calendar.html'
    return dict(grid= mygrid('dcalendar'))
#


@auth.requires_login()
def errorII404():
    db.derror0404.f0.writable = True
    response.view = 'myadd/error-404.html'
    return dict(grid= mygrid('derror0404'))
#


@auth.requires_login()
def errorII500():
    db.derror0500.f0.writable = True
    response.view = 'myadd/error-500.html'
    return dict(grid= mygrid('derror0500'))
#


@auth.requires_login()
def emailIIconfirmation():
    db.demail0confirmation.f0.writable = True
    response.view = 'myadd/email-confirmation.html'
    return dict(grid= mygrid('demail0confirmation'))
#


@auth.requires_login()
def inbox():
    db.dinbox.f0.writable = True
    response.view = 'myadd/inbox.html'
    return dict(grid= mygrid('dinbox'))
#


@auth.requires_login()
def mobileIImenuII3():
    db.dmobile0menu03.f0.writable = True
    response.view = 'myadd/mobile-menu-3.html'
    return dict(grid= mygrid('dmobile0menu03'))
#


@auth.requires_login()
def wysiwyg():
    db.dwysiwyg.f0.writable = True
    response.view = 'myadd/wysiwyg.html'
    return dict(grid= mygrid('dwysiwyg'))
#


@auth.requires_login()
def emailIInewsletter():
    db.demail0newsletter.f0.writable = True
    response.view = 'myadd/email-newsletter.html'
    return dict(grid= mygrid('demail0newsletter'))
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
def widgetstable0ctrl():
    response.view = 'myadd/widgetstable0ctrl.html'
    return dict(grid= mygrid('widgetstable0'))
#


@auth.requires_login()
def tablestable0ctrl():
    response.view = 'myadd/tablestable0ctrl.html'
    return dict(grid= mygrid('tablestable0'))
#


@auth.requires_login()
def tablestable1ctrl():
    response.view = 'myadd/tablestable1ctrl.html'
    return dict(grid= mygrid('tablestable1'))
#


@auth.requires_login()
def tablestable2ctrl():
    response.view = 'myadd/tablestable2ctrl.html'
    return dict(grid= mygrid('tablestable2'))
#


@auth.requires_login()
def indextable0ctrl():
    response.view = 'myadd/indextable0ctrl.html'
    return dict(grid= mygrid('indextable0'))
#


@auth.requires_login()
def invoicetable0ctrl():
    response.view = 'myadd/invoicetable0ctrl.html'
    return dict(grid= mygrid('invoicetable0'))
#


@auth.requires_login()
def dwysiwygform0ctrl():
    response.view = 'myadd/dwysiwygform0ctrl.html'
    return dict(grid= mygrid('dwysiwygform0'))
#


@auth.requires_login()
def dwidgetsform0ctrl():
    response.view = 'myadd/dwidgetsform0ctrl.html'
    return dict(grid= mygrid('dwidgetsform0'))
#


@auth.requires_login()
def demailform0ctrl():
    response.view = 'myadd/demailform0ctrl.html'
    return dict(grid= mygrid('demailform0'))
#


@auth.requires_login()
def dmobileIImenuII2form0ctrl():
    response.view = 'myadd/dmobileIImenuII2form0ctrl.html'
    return dict(grid= mygrid('dmobileIImenuII2form0'))
#


@auth.requires_login()
def dtreeviewform0ctrl():
    response.view = 'myadd/dtreeviewform0ctrl.html'
    return dict(grid= mygrid('dtreeviewform0'))
#


@auth.requires_login()
def dtablesform0ctrl():
    response.view = 'myadd/dtablesform0ctrl.html'
    return dict(grid= mygrid('dtablesform0'))
#


@auth.requires_login()
def dtablesform1ctrl():
    response.view = 'myadd/dtablesform1ctrl.html'
    return dict(grid= mygrid('dtablesform1'))
#


@auth.requires_login()
def dtablesform2ctrl():
    response.view = 'myadd/dtablesform2ctrl.html'
    return dict(grid= mygrid('dtablesform2'))
#


@auth.requires_login()
def dtablesform3ctrl():
    response.view = 'myadd/dtablesform3ctrl.html'
    return dict(grid= mygrid('dtablesform3'))
#


@auth.requires_login()
def dtablesform4ctrl():
    response.view = 'myadd/dtablesform4ctrl.html'
    return dict(grid= mygrid('dtablesform4'))
#


@auth.requires_login()
def dtablesform5ctrl():
    response.view = 'myadd/dtablesform5ctrl.html'
    return dict(grid= mygrid('dtablesform5'))
#


@auth.requires_login()
def derrorII500form0ctrl():
    response.view = 'myadd/derrorII500form0ctrl.html'
    return dict(grid= mygrid('derrorII500form0'))
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
def dformIIelementsII2form0ctrl():
    response.view = 'myadd/dformIIelementsII2form0ctrl.html'
    return dict(grid= mygrid('dformIIelementsII2form0'))
#


@auth.requires_login()
def dformIIelementsII2form1ctrl():
    response.view = 'myadd/dformIIelementsII2form1ctrl.html'
    return dict(grid= mygrid('dformIIelementsII2form1'))
#


@auth.requires_login()
def dbuttonsform0ctrl():
    response.view = 'myadd/dbuttonsform0ctrl.html'
    return dict(grid= mygrid('dbuttonsform0'))
#


@auth.requires_login()
def dgalleryform0ctrl():
    response.view = 'myadd/dgalleryform0ctrl.html'
    return dict(grid= mygrid('dgalleryform0'))
#


@auth.requires_login()
def dmobileIImenuII3form0ctrl():
    response.view = 'myadd/dmobileIImenuII3form0ctrl.html'
    return dict(grid= mygrid('dmobileIImenuII3form0'))
#


@auth.requires_login()
def dcalendarform0ctrl():
    response.view = 'myadd/dcalendarform0ctrl.html'
    return dict(grid= mygrid('dcalendarform0'))
#


@auth.requires_login()
def dloginform0ctrl():
    response.view = 'myadd/dloginform0ctrl.html'
    return dict(grid= mygrid('dloginform0'))
#


@auth.requires_login()
def dloginform1ctrl():
    response.view = 'myadd/dloginform1ctrl.html'
    return dict(grid= mygrid('dloginform1'))
#


@auth.requires_login()
def dloginform2ctrl():
    response.view = 'myadd/dloginform2ctrl.html'
    return dict(grid= mygrid('dloginform2'))
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
def dinvoiceform0ctrl():
    response.view = 'myadd/dinvoiceform0ctrl.html'
    return dict(grid= mygrid('dinvoiceform0'))
#


@auth.requires_login()
def dmobileIImenuII1form0ctrl():
    response.view = 'myadd/dmobileIImenuII1form0ctrl.html'
    return dict(grid= mygrid('dmobileIImenuII1form0'))
#


@auth.requires_login()
def derrorII404form0ctrl():
    response.view = 'myadd/derrorII404form0ctrl.html'
    return dict(grid= mygrid('derrorII404form0'))
#


@auth.requires_login()
def derrorII404form1ctrl():
    response.view = 'myadd/derrorII404form1ctrl.html'
    return dict(grid= mygrid('derrorII404form1'))
#


@auth.requires_login()
def dtwoIImenuII2form0ctrl():
    response.view = 'myadd/dtwoIImenuII2form0ctrl.html'
    return dict(grid= mygrid('dtwoIImenuII2form0'))
#


@auth.requires_login()
def delementsform0ctrl():
    response.view = 'myadd/delementsform0ctrl.html'
    return dict(grid= mygrid('delementsform0'))
#


@auth.requires_login()
def delementsform1ctrl():
    response.view = 'myadd/delementsform1ctrl.html'
    return dict(grid= mygrid('delementsform1'))
#


@auth.requires_login()
def dtimelineform0ctrl():
    response.view = 'myadd/dtimelineform0ctrl.html'
    return dict(grid= mygrid('dtimelineform0'))
#


@auth.requires_login()
def dblankform0ctrl():
    response.view = 'myadd/dblankform0ctrl.html'
    return dict(grid= mygrid('dblankform0'))
#


@auth.requires_login()
def dcontentIIsliderform0ctrl():
    response.view = 'myadd/dcontentIIsliderform0ctrl.html'
    return dict(grid= mygrid('dcontentIIsliderform0'))
#


@auth.requires_login()
def dtypographyform0ctrl():
    response.view = 'myadd/dtypographyform0ctrl.html'
    return dict(grid= mygrid('dtypographyform0'))
#


@auth.requires_login()
def dtopIImenuform0ctrl():
    response.view = 'myadd/dtopIImenuform0ctrl.html'
    return dict(grid= mygrid('dtopIImenuform0'))
#


@auth.requires_login()
def dformIIelementsform0ctrl():
    response.view = 'myadd/dformIIelementsform0ctrl.html'
    return dict(grid= mygrid('dformIIelementsform0'))
#


@auth.requires_login()
def dformIIelementsform1ctrl():
    response.view = 'myadd/dformIIelementsform1ctrl.html'
    return dict(grid= mygrid('dformIIelementsform1'))
#


@auth.requires_login()
def dformIIelementsform2ctrl():
    response.view = 'myadd/dformIIelementsform2ctrl.html'
    return dict(grid= mygrid('dformIIelementsform2'))
#


@auth.requires_login()
def dformIIelementsform3ctrl():
    response.view = 'myadd/dformIIelementsform3ctrl.html'
    return dict(grid= mygrid('dformIIelementsform3'))
#


@auth.requires_login()
def dformIIelementsform4ctrl():
    response.view = 'myadd/dformIIelementsform4ctrl.html'
    return dict(grid= mygrid('dformIIelementsform4'))
#


@auth.requires_login()
def djqgridform0ctrl():
    response.view = 'myadd/djqgridform0ctrl.html'
    return dict(grid= mygrid('djqgridform0'))
#


@auth.requires_login()
def dnestableIIlistform0ctrl():
    response.view = 'myadd/dnestableIIlistform0ctrl.html'
    return dict(grid= mygrid('dnestableIIlistform0'))
#


@auth.requires_login()
def djqueryIIuiform0ctrl():
    response.view = 'myadd/djqueryIIuiform0ctrl.html'
    return dict(grid= mygrid('djqueryIIuiform0'))
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
def dformIIwizardform0ctrl():
    response.view = 'myadd/dformIIwizardform0ctrl.html'
    return dict(grid= mygrid('dformIIwizardform0'))
#


@auth.requires_login()
def dformIIwizardform1ctrl():
    response.view = 'myadd/dformIIwizardform1ctrl.html'
    return dict(grid= mygrid('dformIIwizardform1'))
#


@auth.requires_login()
def dformIIwizardform2ctrl():
    response.view = 'myadd/dformIIwizardform2ctrl.html'
    return dict(grid= mygrid('dformIIwizardform2'))
#


@auth.requires_login()
def ddropzoneform0ctrl():
    response.view = 'myadd/ddropzoneform0ctrl.html'
    return dict(grid= mygrid('ddropzoneform0'))
#


@auth.requires_login()
def ddropzoneform1ctrl():
    response.view = 'myadd/ddropzoneform1ctrl.html'
    return dict(grid= mygrid('ddropzoneform1'))
#


@auth.requires_login()
def dgridform0ctrl():
    response.view = 'myadd/dgridform0ctrl.html'
    return dict(grid= mygrid('dgridform0'))
#


@auth.requires_login()
def dpricingform0ctrl():
    response.view = 'myadd/dpricingform0ctrl.html'
    return dict(grid= mygrid('dpricingform0'))
#


@auth.requires_login()
def dsearchform0ctrl():
    response.view = 'myadd/dsearchform0ctrl.html'
    return dict(grid= mygrid('dsearchform0'))
#


@auth.requires_login()
def dsearchform1ctrl():
    response.view = 'myadd/dsearchform1ctrl.html'
    return dict(grid= mygrid('dsearchform1'))
#


@auth.requires_login()
def dsearchform2ctrl():
    response.view = 'myadd/dsearchform2ctrl.html'
    return dict(grid= mygrid('dsearchform2'))
#


@auth.requires_login()
def dfaqform0ctrl():
    response.view = 'myadd/dfaqform0ctrl.html'
    return dict(grid= mygrid('dfaqform0'))
#
