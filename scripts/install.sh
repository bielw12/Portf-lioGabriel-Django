#!/bin/bash

# Script de instalação automática do Portfólio Django
# Execute: bash scripts/install.sh

echo "🚀 Instalando Portfólio Django..."
echo "=================================="

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado. Por favor, instale Python 3.8 ou superior."
    exit 1
fi

echo "✅ Python encontrado: $(python3 --version)"

# Criar ambiente virtual
echo "📦 Criando ambiente virtual..."
python3 -m venv venv

# Ativar ambiente virtual
echo "🔧 Ativando ambiente virtual..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

# Instalar dependências
echo "📚 Instalando dependências..."
pip install --upgrade pip
pip install -r requirements.txt

# Configurar banco de dados
echo "🗄️ Configurando banco de dados..."
python manage.py makemigrations
python manage.py migrate

# Criar superusuário
echo "👤 Criando superusuário..."
echo "Por favor, forneça as informações para o administrador:"
python manage.py createsuperuser

# Perguntar se deseja dados de exemplo
echo ""
read -p "🎯 Deseja popular com dados de exemplo? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "📝 Populando com dados de exemplo..."
    python manage.py shell < scripts/populate_sample_data.py
fi

# Coletar arquivos estáticos
echo "🎨 Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo ""
echo "🎉 Instalação concluída com sucesso!"
echo "=================================="
echo ""
echo "Para iniciar o servidor:"
echo "1. Ative o ambiente virtual:"
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "   venv\\Scripts\\activate"
else
    echo "   source venv/bin/activate"
fi
echo "2. Execute o servidor:"
echo "   python manage.py runserver"
echo ""
echo "Acesse:"
echo "🌐 Site: http://127.0.0.1:8000/"
echo "⚙️  Admin: http://127.0.0.1:8000/admin/"
echo ""
echo "Usuário admin criado com as credenciais fornecidas."
