from django.shortcuts import render
from listdata.models import FileData
from django.views import generic
from listdata.models import FileData
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    ''' This could be your actual view or a new one '''
    # Your code
    numFiles=FileData.objects.all().count()
    context={
            'num_files':numFiles,
            }
    return render(request,'index.html',context=context)
class DataListView(generic.ListView):
    model=FileData
    context_object_name = 'files_list'
    template_name = '/home/pzaninelli/TRABAJO/dataset_management/dataman_project/listdata/templates/listdata/files_list.html'
    paginated_by=10
class DataListDetailView(generic.DetailView):
    model = FileData
    def file_detail_view(request, primary_key):
       filedata = get_object_or_404(FileData, pk=primary_key)
       return render(request, 'listdata/datos_detail.html', context={'filedata': filedata})
class FileSearchView(generic.ListView):
    model=FileData
    context_object_name = 'searchfiles_list'
    template_name = 'listdata/search.html'
    paginated_by=10
    def get_context_data(self, **kwargs):
        context = super(FileSearchView, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context
    def get_queryset(self):
        FObj = FileData.objects.all()
        var_get_search = self.request.GET.get('search_box')
        var_get_order_by = self.request.GET.get('order')
        
        if var_get_search is not None:
            FObj = FObj.filter(name__icontains=var_get_search)
            
        if var_get_order_by is not None:
            FObj = FObj.order_by(var_get_order_by)
        return FObj