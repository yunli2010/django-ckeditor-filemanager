#
# FileManager http://labs.corefive.com/Projects/FileManager/ Connector
# 
#
# Django Connector By Paul von Hoesslin
#
from django.http import HttpResponse
import os, urllib, time
from django.utils import simplejson
from django.core.servers.basehttp import FileWrapper

import traceback
import sys


encode_json = simplejson.JSONEncoder().encode

try:
    from PIL import Image
except ImportError:
    raise EnvironmentError('Must have the PIL (Python Imaging Library).')

try:
    from settings_local import PROJECT_DIR
except ImportError:
    from settings import PROJECT_DIR

path_exists = os.path.exists
normalize_path = os.path.normpath
absolute_path = os.path.abspath 
split_path = os.path.split
split_ext = os.path.splitext

def dirlist(request):
    r=['<ul class="jqueryFileTree" style="display: none;">']
    try:
        r=['<ul class="jqueryFileTree" style="display: none;">']
        d=urllib.unquote(request.POST.get('dir', PROJECT_DIR + '/static/upload/'))
        for f in os.listdir(d):
            ff=os.path.join(d,f)
            if os.path.isdir(ff):
                if f != ".svn" and f != ".DS_Store":
                    r.append('<li class="directory collapsed"><a href="#" rel="%s/">%s</a></li>' % (ff,f))
            else:
                if f != ".svn" and f != ".DS_Store": 
                    e=os.path.splitext(f)[1][1:] # get .ext and remove dot
                    r.append('<li class="file ext_%s"><a href="#" rel="%s">%s</a></li>' % (e,ff,f))
        r.append('</ul>')
    except Exception,e:
        r.append('Could not load directory: %s' % str(e))
    r.append('</ul>')

    request.session["upload_path"] = PROJECT_DIR + '/static/upload/'
    print request.session["upload_path"]

    return HttpResponse(''.join(r))

def getInfo(request, request_path):
    path = PROJECT_DIR + '/' + request_path
    preview = '../../../' + request_path
    imagetypes = ['.gif','.jpg','.jpeg','.png',]
    if os.path.isdir(PROJECT_DIR + '/' + request_path):
        thefile = {
            'Path' : request_path,
            'Filename' : split_path(path)[-1],
            'File Type' : split_path(path)[1][1:],
            'Preview' : 'images/fileicons/_Open.png',
            'Properties' : {
                    'Date Created' : '',
                    'Date Modified' : '',
                    'Width' : '',
                    'Height' : '',
                    'Size' : ''
                },
            'Return' : request_path[1:],
            'Error' : '',
            'Code' : 0,
            }        
        thefile['File Type'] = 'Directory'
    else:
        ext = split_ext(path)
        preview = '/static/js/filemanager/images/fileicons/'+ ext[1][1:] + '.png'
        thefile = {
            'Path' : request_path,
            'Filename' : split_path(path)[-1],
            'File Type' : split_path(path)[1][1:],
            'Preview' : preview,
            'Properties' : {
                    'Date Created' : '',
                    'Date Modified' : '',
                    'Width' : '',
                    'Height' : '',
                    'Size' : ''
                },
            'Return' : request_path[1:],
            'Error' : '',
            'Code' : 0,
            }        
        if ext[1] in imagetypes:
            try:
                img = Image.open(open(path,"r"))
                xsize, ysize = img.size
                thefile['Properties']['Width'] = xsize
                thefile['Properties']['Height'] = ysize
                thefile['Preview'] = request_path[1:]
            except:
                preview = '/static/js/filemanager/images/fileicons/'+ ext[1][1:] + '.png'
                thefile['Preview'] = preview

        thefile['File Type'] = os.path.splitext(path)[1][1:]

        thefile['Properties']['Date Created'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getctime(path))) 
        thefile['Properties']['Date Modified'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(path)))  
        thefile['Properties']['Size'] = os.path.getsize(path)
    return encode_json(thefile)


def handle_uploaded_file(request, f):
    upload_path = request.session.get("upload_path", PROJECT_DIR + '/static/upload/')
    destination = open((upload_path + f.name), 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    result = {
        'Name' : f.name,
        'Path' : upload_path.replace(PROJECT_DIR, "."),
        'Code' : "0",
        'Error' : ""
    }

    return result


def handler(request):
    if request.method == "POST":
        try:
            result = handle_uploaded_file(request, request.FILES["newfile"])     
            return HttpResponse('<textarea>' + encode_json(result) + '</textarea>')
        except:
            type, value, tb = sys.exc_info()
            print >> sys.stderr,  type.__name__, ":", value
            print >> sys.stderr, '\n'.join(traceback.format_tb(tb))
    else:
        if request.GET["mode"] == "getinfo":
            return HttpResponse(getInfo(request, request.GET["path"]))

        if request.GET["mode"] == "getfolder":
            result = []
            d=urllib.unquote(PROJECT_DIR + '/' + request.GET["path"])
            request.session["upload_path"] = PROJECT_DIR + request.GET["path"][1:]
            print request.session["upload_path"]
            result += " { "
            for i, filename in enumerate(os.listdir(d)):
                if filename != ".svn" and filename != ".DS_Store":
                    result += '"' + request.GET["path"][1:] + filename + '" : '
                    result += getInfo(request,request.GET["path"] + filename)
                    if i < (len(os.listdir(d)) - 1):
                        result += " , "
            result += " } "
            return HttpResponse(result)
    
        if request.GET["mode"] == "rename":
            old = PROJECT_DIR + request.GET["old"][1:]
            path = split_path(old)[0]

            oldname = split_path(old)[-1]

            if os.path.isdir(old+"/"):
                old += '/'

            newname = request.GET["new"]
            newpath = path + '/' + newname

            try:
                print "old:" + old
                print "newpath:" + newpath
                os.rename(old, newpath)
                error_message = newname
                success_code = "0"
            except:
                type, value, tb = sys.exc_info()
                print >> sys.stderr,  type.__name__, ":", value
                print >> sys.stderr, '\n'.join(traceback.format_tb(tb))
                success_code = "500"
                error_message = "There was an error renaming the file."

            if os.path.isdir(newpath+"/"):
                newpath += '/'
            
            result = {
                'Old Path' : old.replace(PROJECT_DIR, "."),
                'Old Name' : oldname,
                'New Path' : (newpath + "/").replace(PROJECT_DIR, "."),
                'New Name' : newname,
                'Error' : error_message,
                'Code' : success_code
            }
        
            return HttpResponse(encode_json(result))

        if request.GET["mode"] == "delete":
            fullpath = PROJECT_DIR + request.GET["path"][1:]
            if os.path.isdir(fullpath+"/"):
                if not fullpath[-1]=='/':
                    fullpath += '/'                

            try:
                directory = split_path(fullpath)[0]
                name = split_path(fullpath)[-1]
                os.remove(fullpath)
                error_message = name + ' was deleted successfully.'
                success_code = "0"
            except:
                error_message = "There was an error deleting the file. <br/> The operation was either not permitted or it may have already been deleted."
                success_code = "500"
            
            result = {
                'Path' : request.GET["path"],
                'Name' : name,
                'Error' : error_message,
                'Code' : success_code
            }        
            return HttpResponse(encode_json(result))


        if request.GET["mode"] == "addfolder":
            path = PROJECT_DIR + request.GET["path"][1:]
            newName = request.GET["name"].replace(" ", "_")

            newPath = path + newName + "/"
            print newPath
        
            if path_exists(path):
                try:
                    os.mkdir(newPath)
                    success_code = "0"
                    error_message = 'Successfully created folder.'
                except:
                    error_message = 'There was an error creating the directory.'
                    success_code = "500"
            else:
                success_code = "500"
                error_message = 'There is no Root Directory.'

            result = {
                'Path' : path,
                'Parent' : request.GET["path"] + "/",
                'Name' : newName,
                'New Path' : newPath,
                'Error' : error_message,
                'Code' : success_code
            }
            return HttpResponse(encode_json(result))
            
    
        if request.GET["mode"] == "download":
            abspath = PROJECT_DIR + request.GET["path"][1:]
            wrapper = FileWrapper(file(abspath))
            response = HttpResponse(wrapper)
            response['Content-Length'] = os.path.getsize(abspath)
            response['Content-Disposition'] = 'attachment; filename=%s' % split_path(abspath)[-1]
            return response

    return HttpResponse("failed")