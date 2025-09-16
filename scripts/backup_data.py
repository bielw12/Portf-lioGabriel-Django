"""
Script para fazer backup dos dados do portfólio
Execute: python manage.py shell < scripts/backup_data.py
"""

import os
import json
import django
from datetime import datetime

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from portfolio_app.models import Profile, Skill, Project, Experience, Contact

def backup_data():
    """Cria backup de todos os dados em formato JSON"""
    
    backup_data = {
        'backup_date': datetime.now().isoformat(),
        'profile': [],
        'skills': [],
        'projects': [],
        'experiences': [],
        'contacts': []
    }
    
    # Backup do perfil
    for profile in Profile.objects.all():
        backup_data['profile'].append({
            'name': profile.name,
            'title': profile.title,
            'bio': profile.bio,
            'email': profile.email,
            'phone': profile.phone,
            'location': profile.location,
            'github_url': profile.github_url,
            'linkedin_url': profile.linkedin_url,
            'twitter_url': profile.twitter_url,
            'website_url': profile.website_url,
        })
    
    # Backup das habilidades
    for skill in Skill.objects.all():
        backup_data['skills'].append({
            'name': skill.name,
            'category': skill.category,
            'proficiency': skill.proficiency,
            'icon': skill.icon,
            'order': skill.order,
        })
    
    # Backup dos projetos
    for project in Project.objects.all():
        backup_data['projects'].append({
            'title': project.title,
            'description': project.description,
            'short_description': project.short_description,
            'technologies': project.technologies,
            'demo_url': project.demo_url,
            'github_url': project.github_url,
            'status': project.status,
            'start_date': project.start_date.isoformat() if project.start_date else None,
            'end_date': project.end_date.isoformat() if project.end_date else None,
            'featured': project.featured,
            'order': project.order,
        })
    
    # Backup das experiências
    for experience in Experience.objects.all():
        backup_data['experiences'].append({
            'company': experience.company,
            'position': experience.position,
            'description': experience.description,
            'start_date': experience.start_date.isoformat() if experience.start_date else None,
            'end_date': experience.end_date.isoformat() if experience.end_date else None,
            'current': experience.current,
            'company_url': experience.company_url,
        })
    
    # Backup dos contatos (apenas dados não sensíveis)
    for contact in Contact.objects.all():
        backup_data['contacts'].append({
            'name': contact.name,
            'subject': contact.subject,
            'created_at': contact.created_at.isoformat(),
            'read': contact.read,
        })
    
    # Salvar backup
    backup_filename = f"backup_portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    with open(backup_filename, 'w', encoding='utf-8') as f:
        json.dump(backup_data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Backup criado: {backup_filename}")
    print(f"📊 Dados salvos:")
    print(f"   - Perfis: {len(backup_data['profile'])}")
    print(f"   - Habilidades: {len(backup_data['skills'])}")
    print(f"   - Projetos: {len(backup_data['projects'])}")
    print(f"   - Experiências: {len(backup_data['experiences'])}")
    print(f"   - Contatos: {len(backup_data['contacts'])}")

if __name__ == "__main__":
    backup_data()
