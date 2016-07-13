from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import loader

from .models import CorrTissue, CorrRun, CorrTrack

from PIL import Image, ImageDraw
import random

class IndexView(generic.ListView):
    template_name = 'correlations/index.html'
    context_object_name = 'tissue_list'

    def get_queryset(self):
    	return CorrTissue.objects.all()

def runs(request, tissue_id):
    template_name = 'correlations/runs.html'
    context_object_name = 'run_list'
    tissue = CorrTissue.objects.get(id=tissue_id)
    run_list = CorrRun.objects.filter(track1__tissue=tissue_id, track2__tissue=tissue_id)
    
#    return response
    return render(request, template_name, {'tissue':tissue, 'run_list': run_list})
def get_image(request, tissue_id):
    print("in get_image, id=" + str(tissue_id))
    img = Image.new("RGB", (300,300), "#FFFFFF")
    data = [(i,random.randint(100,200)) for i in range(0,300,10)]
    draw = ImageDraw.Draw(img)
    draw.polygon(data, fill="#000000")
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response
    
def get_tracks(request):
    #get fg files by tissue id
    template = loader.get_template('correlations/get_tracks.html')
    context = {}
    return HttpResponse(template.render(context, request))
    
def got_tracks(request):
    #get fg files by tissue id
    template = loader.get_template('correlations/got_tracks.html')
    if request.POST["mark"]:
        run_list = CorrRun.objects.filter(
        mark_list = CorrTrack.objects.filter(mark__mark = request.POST["mark"])
    	context = {"track_list": mark_list}
    elif request.POST["tissue"]:
        tissue_list = CorrTrack.objects.filter(tissue__tissue = request.POST["tissue"])
        context = {"track_list": tissue_list}
    return HttpResponse(template.render(context, request))
