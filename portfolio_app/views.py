from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile, Skill, Project, Experience, Contact
from .forms import ContactForm


def home(request):
    """View principal do portfólio"""
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    
    # Projetos em destaque
    featured_projects = Project.objects.filter(featured=True)[:3]
    
    # Habilidades por categoria
    skills_by_category = {}
    for skill in Skill.objects.all():
        if skill.category not in skills_by_category:
            skills_by_category[skill.category] = []
        skills_by_category[skill.category].append(skill)
    
    # Experiências recentes
    experiences = Experience.objects.all()[:3]
    
    context = {
        'profile': profile,
        'featured_projects': featured_projects,
        'skills_by_category': skills_by_category,
        'experiences': experiences,
    }
    
    return render(request, 'portfolio_app/home.html', context)


def projects(request):
    """View para listar todos os projetos"""
    projects_list = Project.objects.all()
    
    context = {
        'projects': projects_list,
    }
    
    return render(request, 'portfolio_app/projects.html', context)


def project_detail(request, project_id):
    """View para detalhes de um projeto específico"""
    project = get_object_or_404(Project, id=project_id)
    
    context = {
        'project': project,
    }
    
    return render(request, 'portfolio_app/project_detail.html', context)


def about(request):
    """View para página sobre"""
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    
    experiences = Experience.objects.all()
    skills = Skill.objects.all()
    
    context = {
        'profile': profile,
        'experiences': experiences,
        'skills': skills,
    }
    
    return render(request, 'portfolio_app/about.html', context)


def contact(request):
    """View para página de contato"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Salvar mensagem no banco
            contact_message = form.save()
            
            # Enviar email (opcional)
            try:
                send_mail(
                    subject=f"Novo contato: {contact_message.subject}",
                    message=f"Nome: {contact_message.name}\nEmail: {contact_message.email}\n\nMensagem:\n{contact_message.message}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.DEFAULT_FROM_EMAIL],
                    fail_silently=True,
                )
            except:
                pass  # Se não conseguir enviar email, continua normalmente
            
            messages.success(request, 'Mensagem enviada com sucesso! Entrarei em contato em breve.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    
    context = {
        'form': form,
        'profile': profile,
    }
    
    return render(request, 'portfolio_app/contact.html', context)
