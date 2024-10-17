from django.shortcuts import render
from django.views.generic import TemplateView
from home.controller import HomeInterface
from django.contrib import messages
from home.models import Contactus,Feedback
from django.shortcuts import render,redirect
	

#admin usename fathima password Admin@123
# Create your views here.

class HomeView(TemplateView):
	
	def get(self, request, *args, **kwargs):
		template_name = 'index.html'
		return HomeInterface(self.request).get_homeview_controller(request,template_name=template_name)

def contact(request):
	
	
	
	if request.method == 'POST':
		emai = request.POST['email']
		firstname=request.POST['name']
		subject=request.POST['subject']
		companyname=request.POST['companyname']
		phone=request.POST['phone']
		intsancecontactus=Contactus(email=emai,first_name=firstname,subject=subject,companyname=companyname,mobile=phone)
		intsancecontactus.save()
		messages.success(request,"Thank you for contacting Motor Mind! We have received your information and will contact you soon!")
		return redirect("home")
	return render(request,'home.html',)
from home.models import Blog
def blogs(request):
	
	slug_ref = request.GET.get("ref")
	blogs_obj=Blog.objects.all()
	if slug_ref:
		blog = blogs_obj.filter(slug=slug_ref).first()
		context={"data":blog,"mode":1}
		return render(request,'blogs.html',context)
	else:
		blogs = blogs_obj.filter(is_published=1).all()
		context={"data":list(blogs),"mode":0}
		return render(request,'blogs.html',context)

def blogdescript(request):
	
	slug_ref = request.GET.get("ref")
	blog_obj = Blog.objects.all()
	blog_list= blog_obj.filter(is_published=True).order_by('-blog_id')
	blog_list=list(blog_list)

	
	if slug_ref:
		blog = blog_obj.filter(slug=slug_ref).first()
		context={"data":blog,"mode":1,"blog_list":blog_list,}
		return render(request,'blogs.html',context)
	else:
		blogs = blog_obj.filter(is_published=1).first()
		context={"data":blogs,"mode":0,"blog_list":blog_list,
			}
		return render(request,'blogs.html',context)	
def blogreadmoredescript(request):
	
	slug_ref = request.GET.get("ref")
	blog_obj = Blog.objects.all()
	blog_list= blog_obj.filter(is_published=True).order_by('blog_id')
	
	blogfirst=blog_obj.filter(is_published=True)[0:1]
	
	if slug_ref:
		
		payload = []
		
		blog = blog_obj.filter(slug=slug_ref).first()
		context={"data":blog,"mode":1,"blog_list":list(blog_list),"blogfirst":blogfirst,}
		return render(request,'blogs.html',context)
	else:
		
		payload = []
		
		blogs = blog_obj.filter(is_published=1,).first()
		context={"data":blogs,"mode":0,"blog_list":list(blog_list),"blogfirst":blogfirst,
				}
		return render(request,'blogs.html',context)
	

def about(request):
	
	return render(request,'aboutus.html',)	

def services(request):
	from home.models import Services
	service_list = Services.objects.filter(is_active=True).values()[:8]
	service_list_dict = list(service_list)
	context={}
	context['service_list']=service_list_dict
	
	return render(request,'services.html',context)	
def contactus(request):
	print("hiii")
	

	if request.method == 'POST':	
		emai = request.POST['email']
		firstname=request.POST['name']
		subject=request.POST['subject']
		companyname=request.POST['companyname']
		phone=request.POST['phone']
		intsancecontactus=Contactus(email=emai,first_name=firstname,subject=subject,companyname=companyname,mobile=phone)
		intsancecontactus.save()
		messages.success(request,"Thank you for contacting Motor Mind! We have received your information and will contact you soon!")  
		return redirect("home")

	return render(request,'contactus.html',)	
def feedback(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		phone = request.POST.get('phone')
		customer_type = request.POST.get('customer_type')
		service_satisfaction = request.POST.get('service_satisfaction')
		vehicle_condition = request.POST.get('vehicle_condition')
		staff_friendliness = request.POST.get('staff_friendliness')
		price_rating = request.POST.get('price_rating')
		additional_feedback = request.POST.get('additional_feedback', '')
		print("price_rating",price_rating)

		# Save the feedback data to the database
		feedback = Feedback(
			name=name,
			phone=phone,
			customer_type=customer_type,
			service_satisfaction=service_satisfaction,
			vehicle_condition=vehicle_condition,
			staff_friendliness=staff_friendliness,
			price_rating=price_rating,
			additional_feedback=additional_feedback
		)
		feedback.save()

		# Redirect to a 'Thank You' page or wherever you want
		return redirect('home')
	return render(request,'feedback.html',)	
def feed(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		phone = request.POST.get('phone')
		customer_type = request.POST.get('customer_type')
		service_satisfaction = request.POST.get('service_satisfaction')
		vehicle_condition = request.POST.get('vehicle_condition')
		staff_friendliness = request.POST.get('staff_friendliness')
		price_rating = request.POST.get('price_rating')
		additional_feedback = request.POST.get('additional_feedback', '')
		print("price_rating",price_rating)

		# Save the feedback data to the database
		feedback = Feedback(
			name=name,
			phone=phone,
			customer_type=customer_type,
			service_satisfaction=service_satisfaction,
			vehicle_condition=vehicle_condition,
			staff_friendliness=staff_friendliness,
			price_rating=price_rating,
			additional_feedback=additional_feedback
		)
		feedback.save()

		# Redirect to a 'Thank You' page or wherever you want
		return redirect('home')
	return render(request,'feed.html',)	

def handler404(request, exception, template_name="404.html"):
    response = render(request, template_name)
    response.status_code = 404
    return response

def handler500(request, template_name="500.html"):
    response = render(request, template_name)
    response.status_code = 500
    return response

def handler403(request, exception, template_name="403.html"):
    response = render(request, template_name)
    response.status_code = 403
    return response