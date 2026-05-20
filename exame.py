class Prova():
    def __init__(self):
        self.questoes = []
        self.respostas = []

    def mostra_Questoes(self):
        print(self.questoes)


    def mostrar_respostas(self):
        print(self.respostas)

    def armazenar_Questao_resposta(self, novaQuestao, novaResposta):
        self.questoes.append(novaQuestao)
        self.respostas.append(novaResposta)