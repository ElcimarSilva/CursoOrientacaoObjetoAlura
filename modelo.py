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

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes}'
    

class Filme(Programa): # Classe constrtora
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao}- {self._likes}'
    

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas



class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas

    def tamanho(self):
        return len(self.programas)

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas}- {self._likes}'

vingadores = Filme('vingadores uhu', 2018, 160)
vingadores.dar_likes()

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    print(programa)