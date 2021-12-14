# Criar um aplicação com controle de tv
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0


    def likes(self): # Método utilizado para armazenar os likes
        return self._likes

    def dar_likes(self): # Método utilizado para dar likes
        self._likes += 1

    @property
    def nome(self): # Método utilizado para nomear
        return self._nome

    @nome.setter
    def nome(self, nome_nome):
        self._nome = nome_nome.title()

class Filme(Programa): # Classe constrtora
    def __init__(self, nome, ano, duracao):
        self._nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self._likes = 0


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        self._nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self._likes = 0


vingadores = Filme('vingadores uhu', 2018, 160)
vingadores.dar_likes()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Temporadas: {vingadores.duracao}- Likes: {vingadores.likes()}')

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes()}')

