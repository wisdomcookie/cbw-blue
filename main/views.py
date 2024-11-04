from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse( "Hello, world. You're at the polls index.")
    
    
def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def programs(request):
    return render(request, 'main/programs.html')

def shop(request, shopname):

    shop_templates = {
        'allentown-central': 'main/shops/allentown-central.html',
        'allentown-east': 'main/shops/allentown-east.html',
        'easton': 'main/shops/easton.html',
    }

    # Get the template for the given shopname, or raise a 404 if not found
    template = shop_templates.get(shopname)
    if template is None:
        raise Http404("Shop not found")
    

    team_members = [
        {
            'name': 'Kim Schaffer',
            'role': 'Executive Director',
            'description': 'Kim became Director of Community Bike Works in 2013. Under her leadership, the organization has grown...',
            'image': 'images/team/kim-schaffer.png',  # Replace with ImageField URL if using Django's media files
            'has_more_info': True,
        },
        {
            'name': 'Madeline M',
            'role': 'Office Manager & Jr. EAB Coordinator',
            'description': 'Madeline has a dual role at Bike Works: Her mornings are spent managing...',
            'image': 'images/team/madeline-m.png',
            'has_more_info': True,
        },
        # Add more team members here...
    ]

    return render(request, template, {'team_members': team_members})


def mission(request):
    return render(request, 'main/about/mission.html')

def people(request):
    return render(request, 'main/about/people.html')

def hiring(request):
    return render(request, 'main/about/hiring.html')