"""
Script para popular o banco com dados de exemplo
Execute: python manage.py shell < scripts/populate_sample_data.py
"""

import os
import django
from datetime import date, datetime

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from portfolio_app.models import Profile, Skill, Project, Experience

# Limpar dados existentes (opcional)
print("Limpando dados existentes...")
Profile.objects.all().delete()
Skill.objects.all().delete()
Project.objects.all().delete()
Experience.objects.all().delete()

# Criar perfil
print("Criando perfil...")
profile = Profile.objects.create(
    name="João Silva",
    title="Desenvolvedor Full Stack Python/Django",
    bio="""Desenvolvedor apaixonado por tecnologia com mais de 5 anos de experiência em desenvolvimento web. 
    Especializado em Python, Django, e tecnologias frontend modernas. Sempre em busca de novos desafios 
    e oportunidades para criar soluções inovadoras que impactem positivamente a vida das pessoas.""",
    email="joao.silva@email.com",
    phone="(11) 99999-9999",
    location="São Paulo, SP",
    github_url="https://github.com/joaosilva",
    linkedin_url="https://linkedin.com/in/joaosilva",
    twitter_url="https://twitter.com/joaosilva",
    website_url="https://joaosilva.dev"
)

# Criar habilidades
print("Criando habilidades...")
skills_data = [
    # Backend
    ("Python", "backend", 95, "fab fa-python"),
    ("Django", "backend", 90, "fab fa-django"),
    ("Django REST Framework", "backend", 85, "fas fa-code"),
    ("FastAPI", "backend", 75, "fas fa-rocket"),
    ("Flask", "backend", 70, "fas fa-flask"),
    
    # Frontend
    ("HTML5", "frontend", 90, "fab fa-html5"),
    ("CSS3", "frontend", 85, "fab fa-css3-alt"),
    ("JavaScript", "frontend", 80, "fab fa-js"),
    ("React", "frontend", 75, "fab fa-react"),
    ("Bootstrap", "frontend", 85, "fab fa-bootstrap"),
    
    # Database
    ("PostgreSQL", "database", 85, "fas fa-database"),
    ("MySQL", "database", 80, "fas fa-database"),
    ("SQLite", "database", 90, "fas fa-database"),
    ("MongoDB", "database", 70, "fas fa-leaf"),
    
    # Tools
    ("Git", "tools", 90, "fab fa-git-alt"),
    ("Docker", "tools", 75, "fab fa-docker"),
    ("Linux", "tools", 85, "fab fa-linux"),
    ("VS Code", "tools", 95, "fas fa-code"),
    
    # Other
    ("API REST", "other", 90, "fas fa-exchange-alt"),
    ("Testes Unitários", "other", 80, "fas fa-vial"),
]

for i, (name, category, proficiency, icon) in enumerate(skills_data):
    Skill.objects.create(
        name=name,
        category=category,
        proficiency=proficiency,
        icon=icon,
        order=i
    )

# Criar projetos
print("Criando projetos...")
projects_data = [
    {
        "title": "Sistema de E-commerce",
        "short_description": "Plataforma completa de e-commerce com Django e React",
        "description": """Sistema completo de e-commerce desenvolvido com Django no backend e React no frontend. 
        Inclui funcionalidades como carrinho de compras, sistema de pagamento, gestão de produtos, 
        painel administrativo e muito mais. Utiliza PostgreSQL como banco de dados e Redis para cache.""",
        "technologies": "Django, React, PostgreSQL, Redis, Stripe API, Docker",
        "demo_url": "https://ecommerce-demo.com",
        "github_url": "https://github.com/joaosilva/ecommerce",
        "featured": True,
        "start_date": date(2023, 1, 15),
        "end_date": date(2023, 6, 30),
        "order": 1
    },
    {
        "title": "API de Gestão de Tarefas",
        "short_description": "API RESTful para gerenciamento de tarefas e projetos",
        "description": """API RESTful desenvolvida com Django REST Framework para gerenciamento de tarefas e projetos. 
        Inclui autenticação JWT, CRUD completo, filtros avançados, paginação e documentação automática com Swagger. 
        Ideal para integração com aplicações frontend ou mobile.""",
        "technologies": "Django REST Framework, JWT, Swagger, PostgreSQL, Celery",
        "demo_url": "https://tasks-api-demo.com",
        "github_url": "https://github.com/joaosilva/tasks-api",
        "featured": True,
        "start_date": date(2023, 7, 1),
        "end_date": date(2023, 9, 15),
        "order": 2
    },
    {
        "title": "Dashboard Analytics",
        "short_description": "Dashboard interativo para análise de dados com gráficos dinâmicos",
        "description": """Dashboard web interativo para visualização e análise de dados. Desenvolvido com Django 
        e Chart.js, permite criar gráficos dinâmicos, relatórios personalizados e exportação de dados. 
        Integra com múltiplas fontes de dados e oferece interface intuitiva para usuários não técnicos.""",
        "technologies": "Django, Chart.js, Bootstrap, PostgreSQL, Pandas",
        "demo_url": "https://dashboard-demo.com",
        "github_url": "https://github.com/joaosilva/dashboard",
        "featured": True,
        "start_date": date(2023, 10, 1),
        "end_date": date(2024, 1, 30),
        "order": 3
    },
    {
        "title": "Blog Pessoal",
        "short_description": "Blog pessoal com sistema de comentários e tags",
        "description": """Blog pessoal desenvolvido com Django, incluindo sistema de posts, comentários, 
        tags, categorias e busca. Interface responsiva e otimizada para SEO. Painel administrativo 
        personalizado para gerenciamento de conteúdo.""",
        "technologies": "Django, Bootstrap, SQLite, TinyMCE",
        "demo_url": "https://joaosilva-blog.com",
        "github_url": "https://github.com/joaosilva/blog",
        "featured": False,
        "start_date": date(2022, 8, 1),
        "end_date": date(2022, 11, 30),
        "order": 4
    }
]

for project_data in projects_data:
    Project.objects.create(**project_data)

# Criar experiências
print("Criando experiências...")
experiences_data = [
    {
        "company": "TechCorp Solutions",
        "position": "Desenvolvedor Full Stack Sênior",
        "description": """Desenvolvimento de aplicações web complexas usando Django e React. 
        Liderança técnica de equipe de 4 desenvolvedores. Implementação de APIs RESTful, 
        otimização de performance e arquitetura de sistemas escaláveis.""",
        "start_date": date(2022, 3, 1),
        "end_date": None,
        "current": True,
        "company_url": "https://techcorp.com"
    },
    {
        "company": "StartupXYZ",
        "position": "Desenvolvedor Python",
        "description": """Desenvolvimento de MVP usando Django e PostgreSQL. Criação de APIs, 
        integração com serviços externos, implementação de testes automatizados e deploy 
        em ambiente de produção usando Docker e AWS.""",
        "start_date": date(2020, 6, 1),
        "end_date": date(2022, 2, 28),
        "current": False,
        "company_url": "https://startupxyz.com"
    },
    {
        "company": "WebDev Agency",
        "position": "Desenvolvedor Junior",
        "description": """Desenvolvimento de sites institucionais e sistemas web usando Django. 
        Manutenção de sistemas legados, criação de funcionalidades e correção de bugs. 
        Trabalho em equipe ágil com metodologia Scrum.""",
        "start_date": date(2019, 1, 15),
        "end_date": date(2020, 5, 30),
        "current": False,
        "company_url": "https://webdevagency.com"
    }
]

for exp_data in experiences_data:
    Experience.objects.create(**exp_data)

print("Dados de exemplo criados com sucesso!")
print("\nPara acessar o admin:")
print("URL: http://127.0.0.1:8000/admin/")
print("Usuário: admin")
print("Senha: admin123")
