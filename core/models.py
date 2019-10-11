from django.db import models
from django.conf import settings


# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)

    def __str__(self):
        return self.sobrenome.upper() + ', ' + self.nome

    class Meta:
        verbose_name_plural = "Autores"


class Aluno(models.Model):
    matricula = models.CharField(max_length=12, unique=True)
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField("Data de nascimento")
    email = models.EmailField('e-mail')

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField("Título", max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    ano_publicacao = models.DateField("Ano de publicação")

    def __str__(self):
        return "%s, (%s)" % (self.titulo, self.ano_publicacao)


class Emprestimo(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data_retirado = models.DateField("Data do emprestimo")
    data_devolucao = models.DateField("Data da devolução")
    livro = models.ManyToManyField(Livro)
    devolvido = models.BooleanField()
