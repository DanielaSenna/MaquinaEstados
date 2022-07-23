from maquina import Maquina
from estados import Estado

if __name__ == "__main__":
    #app.run(debug=True)

    # Instancia a máquina
    maquinaEstados = Maquina()

    # Verifica o estado atual
    print(maquinaEstados.getEstadoAtual())

    # Altera o estado atual
    print("\nAlterando o Estado")
    maquinaEstados.enviarTransicao("08:00")

    # Verifica TODAS as transições para um estado
    print("\nVerificando TODAS as transições para um estado")
    maquinaEstados.enviarEstado("trabalhando")

    # Altera o estado atual
    print("\nAlterando o Estado")
    maquinaEstados.enviarTransicao("12:00")

    # Verifica TODAS as transições para o estado
    print("\nVerificando TODAS as transições para um estado")
    maquinaEstados.enviarEstado("descansando")
    
   