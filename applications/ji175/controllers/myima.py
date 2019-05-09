

@auth.requires_login()
def index():
    response.view = 'myima/index.html'
    return dict(key='value')



@auth.requires_login()
def myupload():
    import os, shutil 
    from PIL import Image

    def png2jpg(fnm_png, fnm_jpg):
        im = Image.open(fnm_png)
        rgb_im = im.convert('RGB')
        rgb_im.save(fnm_jpg)

    def jpg2png(fnm_jpg, fnm_png):
        im = Image.open(fnm_jpg)
        im.save(fnm_png)

    sh_cp= shutil.copyfile
    func_dict= { 'svg2svg':sh_cp,   'gif2gif': sh_cp ,'png2png':  sh_cp , 'PNG2png': sh_cp ,  
                'jpg2jpg': sh_cp , 'jpg2jpeg': sh_cp, 'jpeg@jpg': sh_cp ,
                'JPG2jpg': sh_cp , 'JPG2jpeg': sh_cp, 'JPEG@jpg': sh_cp ,
                              'png2jpg': png2jpg ,  'jpg2png': jpg2png , 
                              'PNG2jpg': png2jpg ,  'JPG2png': jpg2png , 
                              'png2jpeg': png2jpg , 'jpeg2png': jpg2png , 'JPEG2png': jpg2png ,   } 

    new_image_file_path='' 
    param= request.vars.imgnm # controller arg, replaced image
    ctrl_ima= request.vars.imgctrl # controller name for image
    img_file_path= os.path.join( request.folder, 'static/template', param  )
    size_str= 'size unknown'
    if not param.endswith('.svg'):
        im = Image.open(img_file_path)
        width, height = im.size
        size_str='image size: width= {} height= {}'.format( width, height)
    size_str +=  ', %s' % ctrl_ima 
    param_ext= param.split('.')[-1]
    upfolder= os.path.join(request.folder, 'uploads')
    form=SQLFORM.factory( Field('new_image_file', 'upload',uploadfolder= upfolder, requires=IS_NOT_EMPTY()  ))
    if form.process().accepted:
        new_image_file_path = os.path.join(upfolder, form.vars.new_image_file)
        jenka_fnm = request.vars.new_image_file.filename # origin file name
        jenka_ext= jenka_fnm.split('.')[-1]
        if not jenka_fnm.endswith('.svg'):
            try: 
               test = Image.open(new_image_file_path) 
            except: 
               session.flash= 'bad %s' % jenka_fnm
               #session.flash= 'bad file format! check file type and try again!'
               redirect(URL('myima', 'index'))

        param_ext= param.split('.')[-1]
        func_key= '{}2{}'.format( jenka_ext, param_ext )
        if func_key in func_dict:
            request.flash='image file replaced!' 
            func_dict[func_key](new_image_file_path, img_file_path  )
            #shutil.copyfile(new_image_file_path, img_file_path  )
            session.flash= 'write %s' % jenka_fnm
            #session.flash= 'replaced'
            #redirect(URL('default', 'index'))
        else:
            response.flash = 'not %s file, not replaced! maybe bad extension?' % param_ext
            if os.path.isfile(new_image_file_path): 
                   os.remove(new_image_file_path) 

    response.view = 'myima/myupload.html'
    return dict(form=form, param= param, ext=param_ext, size_str= size_str, ctrl_ima= ctrl_ima )
