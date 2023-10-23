from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from myapp.models import employlist
def indexpage(request):
    x=employlist.objects.all()
    return render(request,"index.html",{"x":x})
def submit(request):
    if request.method=="POST":
        a=request.POST["name"]
        b=request.POST["phone"]
        c=request.POST["email"]
        obj=employlist(name=a,phone=b,email=c)
        obj.save()
        x=employlist.objects.all()
        return  render(request,"index.html",{"x":x})
def delete(request,myid):
    v=employlist.objects.get(id=myid)
    v.delete()
    return redirect("/")
def view(request,myid):
    x=employlist.objects.get(id=myid)   
    return  render(request,"view.html",{"x":x})
def edit(request,myid):
    obj=get_object_or_404(employlist,id=myid) 
    if request.method=="POST":
        a=request.POST.get("name1")
        b=request.POST.get("name2")
        c=request.POST.get("name3")
        obj.name=a
        obj.phone=b
        obj.enail=c
        obj.save()
        return  HttpResponseRedirect('/') 
    return render(request,"edit.html")

   
        
    