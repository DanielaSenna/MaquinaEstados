from estados_transicoes import Estados_Transicoes

class Maquina:

    def __init__(self):

        #A máquina será criada já com todos os estados e transições possíveis.
        estados_transacoes = Estados_Transicoes()
        
        self.estadosMaquina = estados_transacoes.estadosPossiveis
        self.transicoesMaquina = estados_transacoes.transicoesPossiveis
        
        # O estado inicial da máquina é "DORMINDO"
        self.estadoAtual = self.estadosMaquina[0]


    def getEstadoAtual(self):
        return f'Estado Atual: {self.estadoAtual.estado}'

    '''
    A função recebe como parâmetro um estado e
    retorna as possíveis transições para o estado em questão.
    '''
    def enviarEstado(self, estado):
        n_estado = estado.upper()

        achou = -1
        posicao = -1
        for index in range(len(self.estadosMaquina)):
            if self.estadosMaquina[index].estado == n_estado:
                achou = 1
                posicao = index
                break
        
        if achou == 1:
            for transicoes in self.estadosMaquina[index].transicoes:
                print(transicoes.transicao, transicoes.proximoEstado.estado)
        else:
            print("Este estado não existe")

        

    '''
    A função recebe como parâmetro a transição para um novo estado.
    O estado atual da máquina é alterado, retornando o novo estado
    que a máquina se encontra.
    '''
    def enviarTransicao(self, transicao):
        n_transicao = transicao
        n_atual = self.estadoAtual.estado

        achou = -1
        achouEstado = None

        for transicao in self.transicoesMaquina:
            if n_transicao == transicao.transicao:
                achou = 1
                achouEstado = transicao.proximoEstado
                break
        
        if achou == 1:
            self.estadoAtual = achouEstado
            print(f"{n_atual} => {self.estadoAtual.estado} >>> Novo Estado Atual: {self.estadoAtual.estado}")
        else:
            print("Não existe essa transição de estado")


      