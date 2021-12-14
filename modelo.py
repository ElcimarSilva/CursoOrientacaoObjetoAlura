# Criar um aplicação com controle de tv
class Filme: # Classe constrtora
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes(self): # Método utilizado para armazenar os likes
        return self.__likes

    def dar_likes(self): # Método utilizado para dar likes
        self.__likes += 1

    @property
    def nome(self): # Método utilizado para nomear
        return self.__nome

    @nome.setter
    def nome(self, nome_nome):
        self.__nome = nome_nome.title()


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome_nome):
        self.__nome = nome_nome.title()

vingadores = Filme('vingadores uhu', 2018, 160)
vingadores.dar_likes()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Temporadas: {vingadores.duracao}- Likes: {vingadores.likes}')

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')

