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
    
   
    team_members_allentown_central = [
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
        {
            'name': 'Jeff Varrone',
            'role': 'Grants Coordinator & Program Instructor',
            'description': 'In the mornings and evenings, he coordinates fundraising and grants, and in the afternoon, he co-coordinates our in-school Jr. Earn a Bike Program. “There’s definitely a lot to learn from our kids. You just have to take the time to listen and never forget to stay silly.”',
            'image': 'images/team/franklin-park/jeff-varrone.png',
            'has_more_info': True,
        },
        {
            'name': 'Florrie Stoop',
            'role': 'Role',
            'description': 'Description',
            'image': 'images/logo.webp',
            'has_more_info': True,
        },
        {
            'name': 'Brittany Smith',
            'role': 'Role',
            'description': 'Description',
            'image': 'images/logo.webp',
            'has_more_info': True,
        },
        {
            'name': 'Jose Monte De Oca',
            'role': 'Role',
            'description': 'Description',
            'image': 'images/logo.webp',
            'has_more_info': True,
        },
    ]

    team_members_allentown_east = [
        {
            'name': 'Dave Edinger',
            'role': 'Deputy Director',
            'description': 'As Deputy Executive Director, Dave manages all internal operations and current programming.',
            'image': 'images/team/keck-park/dave-edinger.png',  
            'has_more_info': True,
        },
        {
            'name': 'James Williams',
            'role': 'Director of Programs',
            'description': 'As the Director of Programs, James oversees all of our programs across the Lehigh Valley, helping to provide opportunities for students to see their strengths and potential.',
            'image': 'images/team/keck-park/james-williams.png',
            'has_more_info': True,
        },
        {
            'name': 'Sadie Aten',
            'role': 'Keck Park Program Manager & Social Media Coordinator',
            'description': 'She loves getting to work and build meaningful relationships with the students.',
            'image': 'images/team/keck-park/sadie-aten.png',
            'has_more_info': True,
        },
        {
            'name': 'Reilly Leisher',
            'role': 'Program Instructor',
            'description': 'Her favorite part of working at CBW is being able to form meaningful relationships with the kids of Allentown and seeing the impact of those relationships.',
            'image': 'images/team/keck-park/reilly-leisher.png',
            'has_more_info': True,
        },
        {
            'name': 'Omar Carpio',
            'role': 'Role',
            'description': 'Description',
            'image': 'images/logo.webp',
            'has_more_info': True,
        },
    ]

    team_members_easton = [
        {
            'name': 'Nella Panella',
            'role': 'Easton Program Manager',
            'description': 'Nella joined CBW in 2022 as a Program Instructor at our Easton location where she helped to expand programming, engage with community and help students become confident riders. She now manages programming in Easton. ',
            'image': 'images/team/easton/nella-panella.png',  
            'has_more_info': True,
        },
        {
            'name': 'Brean Shea',
            'role': 'Program Instructor',
            'description': 'He is a program instructor in Easton and absolutely LOVES sharing his bike life with the local community and youth, with a particular interest in getting kids to race.',
            'image': 'images/team/easton/brean-shea.png',
            'has_more_info': True,
        },
        {
            'name': 'Yotzael Cerezo',
            'role': 'Role',
            'description': 'Description',
            'image': 'images/logo.webp',
            'has_more_info': True,
        },
    ]

    # Select team members based on shopname
    if shopname == 'allentown-central':
        team_members = team_members_allentown_central
    elif shopname == 'allentown-east':
        team_members = team_members_allentown_east
    elif shopname == 'easton':
        team_members = team_members_easton
    else:
        raise Http404("Team not found")

    # Render the template with the corresponding team members
    return render(request, template, {
        'team_members': team_members
    })


def impact(request):
    return render(request, 'main/about/impact.html')

def people(request):
    return render(request, 'main/about/people.html')

def hiring(request):
    return render(request, 'main/about/hiring.html')