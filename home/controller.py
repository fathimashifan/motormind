from .models import *
from django.shortcuts import render,redirect


class HomeInterface(object):
    def __init__(self, request):
        self.request = request
        if request.method == 'POST':
            self.data = request.POST
        try:
            self.name = request.session['name']
            self.id = request.session['id']
            self.type = request.session['type']
        except Exception as e:
            self.name = request.session['name'] = None
            self.id = request.session['id'] = None
            self.type = request.session['type'] = None


    def get_homeview_controller(self, request, template_name):
        service_list = Services.objects.filter(is_active=True).values()[:8]
        service_list_dict = list(service_list)
        context={}
        context['service_list']=service_list_dict
        brands_list=Brands.objects.filter(is_active=True).all()
        brands_list_dict = list(brands_list)
        context['brands_list']=brands_list_dict
        recent_works_list=RecentWorks.objects.filter(is_active=True).all()
        recent_works_list_dict = list(recent_works_list)
        context['recent_works_list']=recent_works_list_dict
        testimonial_list=Testimonials.objects.filter(is_active=True).all()
        testimonial_list_dict = list(testimonial_list)
        context['testmonial_list']=testimonial_list_dict
        print("testmonial_list",testimonial_list_dict)
        slug_ref = self.request.GET.get("ref",None)
        if slug_ref:
            blogs = Blog.objects.filter(slug=slug_ref).first()
        else:
            blogs = Blog.objects.filter(is_published=True).order_by('-blog_id').all()[0:3]
        blogs = list(blogs)    
        context['data']=blogs
        context['mode']=0
         

  
        return render(request, template_name,context)