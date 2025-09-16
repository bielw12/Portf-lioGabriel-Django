from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Profile(models.Model):
    """Modelo para informações do perfil do desenvolvedor"""
    name = models.CharField(max_length=100, verbose_name="Nome")
    title = models.CharField(max_length=200, verbose_name="Título/Cargo")
    bio = models.TextField(verbose_name="Biografia")
    email = models.EmailField(verbose_name="E-mail")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Telefone")
    location = models.CharField(max_length=100, blank=True, verbose_name="Localização")
    profile_image = models.ImageField(upload_to='profile/', blank=True, verbose_name="Foto do Perfil")
    
    # Links sociais
    github_url = models.URLField(blank=True, verbose_name="GitHub")
    linkedin_url = models.URLField(blank=True, verbose_name="LinkedIn")
    twitter_url = models.URLField(blank=True, verbose_name="Twitter")
    website_url = models.URLField(blank=True, verbose_name="Website Pessoal")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"
    
    def __str__(self):
        return self.name


class Skill(models.Model):
    """Modelo para habilidades técnicas"""
    SKILL_CATEGORIES = [
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('database', 'Banco de Dados'),
        ('tools', 'Ferramentas'),
        ('other', 'Outros'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Nome da Habilidade")
    category = models.CharField(max_length=20, choices=SKILL_CATEGORIES, verbose_name="Categoria")
    proficiency = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        verbose_name="Nível de Proficiência (%)"
    )
    icon = models.CharField(max_length=50, blank=True, verbose_name="Ícone (classe CSS)")
    order = models.IntegerField(default=0, verbose_name="Ordem de Exibição")
    
    class Meta:
        verbose_name = "Habilidade"
        verbose_name_plural = "Habilidades"
        ordering = ['category', 'order', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"


class Project(models.Model):
    """Modelo para projetos do portfólio"""
    STATUS_CHOICES = [
        ('completed', 'Concluído'),
        ('in_progress', 'Em Andamento'),
        ('planned', 'Planejado'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Título do Projeto")
    description = models.TextField(verbose_name="Descrição")
    short_description = models.CharField(max_length=300, verbose_name="Descrição Curta")
    image = models.ImageField(upload_to='projects/', verbose_name="Imagem do Projeto")
    
    # URLs do projeto
    demo_url = models.URLField(blank=True, verbose_name="URL da Demo")
    github_url = models.URLField(blank=True, verbose_name="URL do GitHub")
    
    # Tecnologias utilizadas
    technologies = models.CharField(max_length=500, verbose_name="Tecnologias (separadas por vírgula)")
    
    # Status e datas
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='completed', verbose_name="Status")
    start_date = models.DateField(verbose_name="Data de Início")
    end_date = models.DateField(blank=True, null=True, verbose_name="Data de Conclusão")
    
    # Controle de exibição
    featured = models.BooleanField(default=False, verbose_name="Projeto em Destaque")
    order = models.IntegerField(default=0, verbose_name="Ordem de Exibição")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        ordering = ['-featured', 'order', '-start_date']
    
    def __str__(self):
        return self.title
    
    def get_technologies_list(self):
        """Retorna lista de tecnologias"""
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]


class Experience(models.Model):
    """Modelo para experiência profissional"""
    company = models.CharField(max_length=200, verbose_name="Empresa")
    position = models.CharField(max_length=200, verbose_name="Cargo")
    description = models.TextField(verbose_name="Descrição das Atividades")
    start_date = models.DateField(verbose_name="Data de Início")
    end_date = models.DateField(blank=True, null=True, verbose_name="Data de Término")
    current = models.BooleanField(default=False, verbose_name="Trabalho Atual")
    company_url = models.URLField(blank=True, verbose_name="Site da Empresa")
    
    class Meta:
        verbose_name = "Experiência"
        verbose_name_plural = "Experiências"
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.position} - {self.company}"


class Contact(models.Model):
    """Modelo para mensagens de contato"""
    name = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField(verbose_name="E-mail")
    subject = models.CharField(max_length=200, verbose_name="Assunto")
    message = models.TextField(verbose_name="Mensagem")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Envio")
    read = models.BooleanField(default=False, verbose_name="Lida")
    
    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
