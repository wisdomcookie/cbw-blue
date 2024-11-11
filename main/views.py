from django.http import Http404, HttpResponse
from django.shortcuts import render

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

    template = shop_templates.get(shopname)
    if template is None:
        raise Http404("Shop not found")
    

    team_members = [
        {
            'name': 'Kim Schaffer',
            'role': 'Executive Director',
            'description': 'Kim became Director of Community Bike Works in 2013. Under her leadership, the organization has grown to engage more students in a range of cycling, literacy, and leadership programs. ',
            'image': 'images/team/franklin-park/kim-schaffer.png',  
            'has_more_info': True,
        },
        {
            'name': 'Madeline M',
            'role': 'Office Manager & Jr. EAB Coordinator',
            'description': 'Madeline has a dual role at Bike Works: Her mornings are spent managing our database and coordinating other office tasks, and afternoons she runs our Junior Earn a Bike program. ',
            'image': 'images/team/franklin-park/madeline-m.png',
            'has_more_info': True,
        },
        {
            'name': 'Adonis Cannon',
            'role': 'Downtown Allentown Program Manager & Cycling Coordinator',
            'description': 'Adonis manages Earn a Bike and Drop-in at our downtown bike shop, and our recreational, road riding, track cycling, and mountain biking programs for all our students. ',
            'image': 'images/team/franklin-park/adonis-cannon.png',
            'has_more_info': True,
        },
    ]

    return render(request, template, {'team_members': team_members})


def impact(request):
    return render(request, 'main/about/impact.html')

def people(request):
    return render(request, 'main/about/people.html')

def hiring(request):
    return render(request, 'main/about/hiring.html')