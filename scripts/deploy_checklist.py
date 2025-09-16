"""
Script para verificar se o projeto está pronto para deploy
Execute: python manage.py shell < scripts/deploy_checklist.py
"""

import os
import django
from django.conf import settings
from django.core.management import call_command
from django.core.exceptions import ImproperlyConfigured

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

def check_deploy_readiness():
    """Verifica se o projeto está pronto para deploy em produção"""
    
    print("🔍 Verificando prontidão para deploy...")
    print("=" * 50)
    
    issues = []
    warnings = []
    
    # 1. Verificar DEBUG
    if settings.DEBUG:
        issues.append("❌ DEBUG está habilitado (deve ser False em produção)")
    else:
        print("✅ DEBUG desabilitado")
    
    # 2. Verificar SECRET_KEY
    if settings.SECRET_KEY == 'django-insecure-your-secret-key-here-change-in-production':
        issues.append("❌ SECRET_KEY padrão detectada (altere para produção)")
    else:
        print("✅ SECRET_KEY personalizada")
    
    # 3. Verificar ALLOWED_HOSTS
    if not settings.ALLOWED_HOSTS or settings.ALLOWED_HOSTS == ['localhost', '127.0.0.1']:
        warnings.append("⚠️  ALLOWED_HOSTS contém apenas hosts locais")
    else:
        print("✅ ALLOWED_HOSTS configurado")
    
    # 4. Verificar banco de dados
    db_engine = settings.DATABASES['default']['ENGINE']
    if 'sqlite3' in db_engine:
        warnings.append("⚠️  Usando SQLite (considere PostgreSQL para produção)")
    else:
        print("✅ Banco de dados de produção configurado")
    
    # 5. Verificar arquivos estáticos
    if not settings.STATIC_ROOT:
        issues.append("❌ STATIC_ROOT não configurado")
    else:
        print("✅ STATIC_ROOT configurado")
    
    # 6. Verificar MEDIA_ROOT
    if not settings.MEDIA_ROOT:
        warnings.append("⚠️  MEDIA_ROOT pode precisar de configuração para produção")
    else:
        print("✅ MEDIA_ROOT configurado")
    
    # 7. Verificar se existem migrações pendentes
    try:
        call_command('showmigrations', '--plan', verbosity=0)
        print("✅ Migrações verificadas")
    except:
        warnings.append("⚠️  Não foi possível verificar migrações")
    
    # 8. Verificar se collectstatic foi executado
    static_files_exist = os.path.exists(os.path.join(settings.STATIC_ROOT or '', 'css', 'style.css'))
    if not static_files_exist:
        warnings.append("⚠️  Execute 'python manage.py collectstatic' antes do deploy")
    else:
        print("✅ Arquivos estáticos coletados")
    
    # 9. Verificar variáveis de ambiente recomendadas
    env_vars = ['SECRET_KEY', 'DATABASE_URL', 'ALLOWED_HOSTS']
    for var in env_vars:
        if var not in os.environ:
            warnings.append(f"⚠️  Variável de ambiente {var} não encontrada")
    
    # Resumo
    print("\n" + "=" * 50)
    print("📋 RESUMO DA VERIFICAÇÃO")
    print("=" * 50)
    
    if not issues and not warnings:
        print("🎉 Projeto pronto para deploy!")
    else:
        if issues:
            print(f"❌ {len(issues)} problema(s) crítico(s) encontrado(s):")
            for issue in issues:
                print(f"   {issue}")
        
        if warnings:
            print(f"\n⚠️  {len(warnings)} aviso(s):")
            for warning in warnings:
                print(f"   {warning}")
    
    print("\n📚 Checklist adicional:")
    print("   □ Configurar servidor web (Nginx/Apache)")
    print("   □ Configurar HTTPS/SSL")
    print("   □ Configurar backup automático")
    print("   □ Configurar monitoramento")
    print("   □ Testar formulário de contato")
    print("   □ Verificar SEO e meta tags")
    print("   □ Testar responsividade")
    print("   □ Configurar domínio personalizado")

if __name__ == "__main__":
    check_deploy_readiness()
