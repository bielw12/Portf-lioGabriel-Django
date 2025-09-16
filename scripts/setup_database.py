"""
Script para configurar o banco de dados e criar superusuário
Execute: python manage.py shell < scripts/setup_database.py
"""

import os
import django
from django.contrib.auth.models import User
from django.core.management import execute_from_command_line

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

# Executar migrações
print("Executando migrações...")
execute_from_command_line(['manage.py', 'makemigrations'])
execute_from_command_line(['manage.py', 'migrate'])

# Criar superusuário se não existir
if not User.objects.filter(username='admin').exists():
    print("Criando superusuário...")
    User.objects.create_superuser(
        username='admin',
        email='admin@portfolio.com',
        password='admin123'
    )
    print("Superusuário criado: admin / admin123")
else:
    print("Superusuário já existe")

print("Configuração do banco de dados concluída!")
