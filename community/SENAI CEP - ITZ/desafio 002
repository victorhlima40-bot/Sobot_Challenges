import time

# Definição dos Estados da Missão
ESTADO_COLETA = 1
ESTADO_SEGUIR_LINHA = 2
ESTADO_DEPOSITO = 3
ESTADO_RETORNO = 4
ESTADO_FIM = 5

class SoBotAdvancedFSM:
    def __init__(self):
        print(">> Inicializando SoBot com Máquina de Estados...")
        self.estado_atual = ESTADO_COLETA
        self.rodando = True

    def ler_sensores_três_pontos(self):
        """
        Simula um array de 3 sensores (Esquerdo, Centro, Direito).
        Retorna um dicionário com os valores (0 = branco/pista, 1 = linha preta).
        """
        # Exemplo simulado: altere conforme a leitura digital/analógica real das portas do SoBot
        return {
            "esq": 0,
            "centro": 1,  # Centro na linha
            "dir": 0
        }

    def verificar_sensor_fim_pista(self):
        """Verifica se encontrou a fita transversal no final da linha."""
        return False  # Mude para True quando o sensor de chegada for acionado

    # --- Comportamentos dos Atuadores ---
    def acionar_motores(self, vel_esq, vel_dir):
        print(f"[Motores] Esquerdo: {vel_esq}% | Direito: {vel_dir}%")

    def empilhadeira(self, acao):
        if acao == "subir":
            print("[Empilhadeira] Subindo garfo com o palete...")
            time.sleep(2.0)
        elif acao == "descer":
            print("[Empilhadeira] Descendo garfo...")
            time.sleep(2.0)
        print("[Empilhadeira] Posição alcançada.")

    # --- Execução da Máquina de Estados ---
    def executar_ciclo(self):
        while self.rodando:
            
            if self.estado_atual == ESTADO_COLETA:
                print("\n--- [ESTADO] Coletando Palete ---")
                self.empilhadeira("descer")
                self.acionar_motores(30, 30)  # Avança devagar para encaixar
                time.sleep(1.2)
                self.acionar_motores(0, 0)
                self.empilhadeira("subir")
                
                # Transição para o próximo estado
                self.estado_atual = ESTADO_SEGUIR_LINHA

            elif self.estado_atual == ESTADO_SEGUIR_LINHA:
                print("\n--- [ESTADO] Seguindo Linha até o Destino ---")
                
                while True:
                    s = self.ler_sensores_três_pontos()
                    
                    # Verificação de chegada ao fim da pista
                    if self.verificar_sensor_fim_pista():
                        self.acionar_motores(0, 0)
                        self.estado_atual = ESTADO_DEPOSITO
                        break

                    # Lógica de controle com 3 sensores (Seguidor de linha proporcional básico)
                    if s["centro"] == 1:
                        # Linha no centro: segue em frente em velocidade máxima
                        self.acionar_motores(40, 40)
                    elif s["esq"] == 1:
                        # Desviau para a direita, corrige virando para a esquerda
                        self.acionar_motores(15, 45)
                    elif s["dir"] == 1:
                        # Desviau para a esquerda, corrige virando para a direita
                        self.acionar_motores(45, 15)
                    else:
                        # Perdeu a linha momentaneamente, avança lento procurando
                        self.acionar_motores(25, 25)
                    
                    time.sleep(0.02) # Frequência de atualização rápida

            elif self.estado_atual == ESTADO_DEPOSITO:
                print("\n--- [ESTADO] Depositando o Palete ---")
                self.empilhadeira("descer")
                self.acionar_motores(-30, -30)  # Dá ré para sair debaixo do palete
                time.sleep(1.0)
                self.acionar_motores(0, 0)
                
                # Transição para o retorno ou fim
                self.estado_atual = ESTADO_FIM

            elif self.estado_atual == ESTADO_FIM:
                print("\n--- [ESTADO] Missão Concluída com Sucesso! ---")
                self.rodando = False

# Execução
if __name__ == "__main__":
    missao = SoBotAdvancedFSM()
    missao.executar_ciclo()
