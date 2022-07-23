from estados import Estado
from transicoes import Transicao

class Estados_Transicoes:

    def __init__(self):

        '''
        O programa já possui uma lista de possíveis estados e transições para as máquinas.
        '''
        
        self.estadosPossiveis = [
                                    Estado("DORMINDO"), 
                                    Estado("ACORDADO"), 
                                    Estado("TRABALHANDO"),
                                    Estado("DESCANSANDO")]

        self.transicoesPossiveis = [
                                    Transicao("08:00"),
                                    Transicao("12:00"),
                                    Transicao("13:00"),
                                    Transicao("18:00"),
                                    Transicao("22:00")
                                    ]

        self.Relacionamentos()

    def Relacionamentos(self):
        self.transicoesPossiveis[0].proximoEstado = self.estadosPossiveis[2]
        self.transicoesPossiveis[1].proximoEstado = self.estadosPossiveis[3]
        self.transicoesPossiveis[2].proximoEstado = self.estadosPossiveis[2]
        self.transicoesPossiveis[3].proximoEstado = self.estadosPossiveis[1]
        self.transicoesPossiveis[4].proximoEstado = self.estadosPossiveis[0]


        self.estadosPossiveis[0].transicoes.append(self.transicoesPossiveis[0])
        self.estadosPossiveis[1].transicoes.append(self.transicoesPossiveis[4])
        self.estadosPossiveis[2].transicoes.append(self.transicoesPossiveis[1])
        self.estadosPossiveis[2].transicoes.append(self.transicoesPossiveis[3])
        self.estadosPossiveis[3].transicoes.append(self.transicoesPossiveis[2])

