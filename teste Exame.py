import unittest

from exame import Prova


class ProvaTest(unittest.TestCase):
    def setUp(self):
        self.questao = "O que aprendem os alunos da Ctrl+Play"
        self.resposta = "Programaçao, Robotica e muito mais"
        self.p = Prova()
        self.p.armazenar_Questao_resposta(self.questao, self.resposta)
    def test_armazenaQuestao(self):
       self.assertIn("O que aprendem os alunos da Ctrl+Play", self.p.questoes)

    def test_armazenaResposta(self):
        self.assertIn("Programaçao, Robotica e muito mais", self.p.respostas)

unittest.main(argv=[''],exit=False)