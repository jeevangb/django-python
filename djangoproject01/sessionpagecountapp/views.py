from django.shortcuts import render

# Create your views here.
def page_count_view(request):
    count=request.session.get('count',0)
    count=count+1
    request.session['count']=count
    print(count)
    return render(request,'pagecount.html',{'count':count})