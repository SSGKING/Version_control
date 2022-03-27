import django.http
import django.views.decorators.csrf
import AccountManager

#@django.views.decorators.csrf.csrf_exempt
def register(req):
    if req.method != "POST":
        return django.http.HttpResponseBadRequest("Must use Post")
    uname = req.POST.get("username")
    pwd = req.POST.get("password")
    try:
        AccountManager.addAccount(uname,pwd)
        req.session["user"]= uname
        req.session.modified =True
        return django.http.HttpResponse("Ok")
    except AccountManager.AccountError as e:
        #print(e.args)
        return django.http.HttpResponseBadRequest()