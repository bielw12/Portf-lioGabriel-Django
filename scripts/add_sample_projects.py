#!/usr/bin/env python
"""
Script para adicionar projetos de exemplo ao portfólio
Execute: python manage.py shell < scripts/add_sample_projects.py
"""

import os
import sys
import django
from datetime import date, timedelta

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from portfolio_app.models import Project

def create_sample_projects():
    """Cria projetos de exemplo para o portfólio"""
    
    # Limpar projetos existentes (opcional)
    Project.objects.all().delete()
    print("Projetos existentes removidos.")
    
    projects_data = [
        {
            'title': 'E-commerce Django',
            'short_description': 'Plataforma completa de e-commerce com carrinho, pagamentos e painel administrativo.',
            'description': '''Sistema completo de e-commerce desenvolvido em Django com funcionalidades avançadas:
            
• Sistema de autenticação e perfis de usuário
• Catálogo de produtos com categorias e filtros
• Carrinho de compras e sistema de checkout
• Integração com gateway de pagamento
• Painel administrativo para gestão de produtos
• Sistema de avaliações e comentários
• Relatórios de vendas e analytics
• Design responsivo e otimizado para SEO''',
            'technologies': 'Django, Python, PostgreSQL, Bootstrap, JavaScript, Stripe API, Redis',
            'demo_url': 'https://demo-ecommerce.herokuapp.com',
            'github_url': 'https://github.com/usuario/ecommerce-django',
            'status': 'completed',
            'featured': True,
            'start_date': date.today() - timedelta(days=120),
            'end_date': date.today() - timedelta(days=30),
            'order': 1
        },
        {
            'title': 'API REST Blog',
            'short_description': 'API RESTful para blog com autenticação JWT e documentação Swagger.',
            'description': '''API REST completa para sistema de blog desenvolvida com Django REST Framework:
            
• Autenticação JWT com refresh tokens
• CRUD completo para posts, categorias e comentários
• Sistema de permissões granular
• Paginação e filtros avançados
• Upload de imagens com redimensionamento
• Documentação automática com Swagger
• Testes unitários e de integração
• Deploy automatizado com Docker''',
            'technologies': 'Django REST Framework, JWT, PostgreSQL, Docker, Swagger, Celery',
            'demo_url': 'https://api-blog-demo.herokuapp.com/docs/',
            'github_url': 'https://github.com/usuario/blog-api-django',
            'status': 'completed',
            'featured': True,
            'start_date': date.today() - timedelta(days=90),
            'end_date': date.today() - timedelta(days=15),
            'order': 2
        },
        {
            'title': 'Sistema de Gestão Escolar',
            'short_description': 'Plataforma web para gestão de escola com módulos para alunos, professores e administração.',
            'description': '''Sistema completo de gestão escolar desenvolvido em Django:
            
• Módulo de matrículas e cadastro de alunos
• Sistema de notas e frequência
• Calendário acadêmico e horários
• Portal do aluno e do professor
• Relatórios e boletins em PDF
• Sistema de mensagens internas
• Controle financeiro e mensalidades
• Dashboard com métricas e gráficos''',
            'technologies': 'Django, Python, MySQL, Chart.js, Bootstrap, ReportLab, AJAX',
            'demo_url': 'https://gestao-escolar-demo.com',
            'github_url': 'https://github.com/usuario/gestao-escolar',
            'status': 'completed',
            'featured': False,
            'start_date': date.today() - timedelta(days=180),
            'end_date': date.today() - timedelta(days=60),
            'order': 3
        },
        {
            'title': 'Dashboard Analytics',
            'short_description': 'Dashboard interativo para visualização de dados com gráficos em tempo real.',
            'description': '''Dashboard de analytics desenvolvido com Django e tecnologias modernas:
            
• Visualização de dados em tempo real
• Gráficos interativos com Chart.js e D3.js
• Filtros dinâmicos por período e categoria
• Exportação de relatórios em PDF/Excel
• API para integração com outras aplicações
• Sistema de alertas e notificações
• Interface responsiva e intuitiva
• Otimização de performance com cache Redis''',
            'technologies': 'Django, Chart.js, D3.js, Redis, Pandas, PostgreSQL, WebSockets',
            'demo_url': 'https://dashboard-analytics.herokuapp.com',
            'github_url': 'https://github.com/usuario/dashboard-analytics',
            'status': 'completed',
            'featured': False,
            'start_date': date.today() - timedelta(days=75),
            'end_date': date.today() - timedelta(days=10),
            'order': 4
        },
        {
            'title': 'Chat em Tempo Real',
            'short_description': 'Aplicação de chat com WebSockets, salas privadas e compartilhamento de arquivos.',
            'description': '''Sistema de chat em tempo real desenvolvido com Django Channels:
            
• Mensagens instantâneas com WebSockets
• Salas de chat públicas e privadas
• Compartilhamento de arquivos e imagens
• Sistema de notificações push
• Histórico de conversas
• Status online/offline dos usuários
• Emojis e formatação de texto
• Moderação e controle de spam''',
            'technologies': 'Django Channels, WebSockets, Redis, JavaScript, HTML5, CSS3',
            'demo_url': 'https://chat-realtime.herokuapp.com',
            'github_url': 'https://github.com/usuario/chat-django',
            'status': 'in_progress',
            'featured': False,
            'start_date': date.today() - timedelta(days=45),
            'end_date': None,
            'order': 5
        },
        {
            'title': 'Portfólio Pessoal',
            'short_description': 'Site portfólio responsivo com área administrativa para gerenciar projetos e conteúdo.',
            'description': '''Portfólio pessoal desenvolvido em Django com design moderno:
            
• Design responsivo e otimizado para SEO
• Área administrativa para gerenciar conteúdo
• Galeria de projetos com filtros
• Formulário de contato funcional
• Blog integrado para artigos
• Otimização de imagens automática
• Integração com Google Analytics
• Deploy automatizado no Heroku''',
            'technologies': 'Django, HTML5, CSS3, JavaScript, Bootstrap, Pillow, Heroku',
            'demo_url': 'https://meu-portfolio.herokuapp.com',
            'github_url': 'https://github.com/usuario/portfolio-django',
            'status': 'completed',
            'featured': True,
            'start_date': date.today() - timedelta(days=30),
            'end_date': date.today() - timedelta(days=5),
            'order': 6
        }
    ]
    
    # Criar projetos
    for project_data in projects_data:
        project = Project.objects.create(**project_data)
        print(f"✓ Projeto criado: {project.title}")
    
    print(f"\n🎉 {len(projects_data)} projetos de exemplo foram adicionados com sucesso!")
    print("\nProjetos em destaque:")
    featured_projects = Project.objects.filter(featured=True)
    for project in featured_projects:
        print(f"  • {project.title}")

if __name__ == "__main__":
    create_sample_projects()
