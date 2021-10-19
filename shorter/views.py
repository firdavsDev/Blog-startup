from django.shortcuts import render,redirect
from .models import Urla
from django.http import HttpResponse
import logging

logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger=logging.getLogger()

# Create your views here.
def url(request):
    return render(request,'url.html')

import uuid

# Create
def create(request):
    if request.POST:
        logger.info("Post keldi")
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Urla(link=link,uuid=uid)
        new_url.save()
    else:
        logger.error('Xatolik')
    return HttpResponse(uid)

def go(request,pk):
    try:
        url_detail = Urla.objects.get(uuid=pk)
        logger.info('Url yaratildi')
        return redirect(url_detail.link)
    except Exception:
        return HttpResponse('Xato')