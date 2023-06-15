import random
###############################################################################
#                                 Observações                                 #
##############################################################################+

"Foi utilizado o Black para formatação dessa seção."

###############################################################################
#                                   Suporte                                   #
##############################################################################+

def funcao_objetivo_dieta(individuo, calorias_ideais, peso):
    """Computa a funcao objetivo de um individuo no problema da dieta com limite de peso
    Args:
      individiuo: lista contendo os alimentos
      calorias_ideais: O valor retornado, dado a busca pelos ínvidos, junto de quem compõem a mochila
    Returns:
      A "distância" entre o alimento que passou do limite e o peso máximo de calorias da dieta. Essa distância
      é medida alimento por alimento. Quanto mais distante uma dieta for da que
      o limite diz que deveria ser, maior sendo essa distância, maior será a penalização.
      Peso: representa a penalidade de quão longe está o limite  da tentativa realizada
    """

 

    diferenca = 0

 

    for alimento_candidato, limite in zip(individuo, calorias_ideais):
        diferenca = diferenca + abs(ord(alimento_candidato) - ord(limite))
    diferenca_tamanho = abs(len(individuo) - len(calorias_ideais))
    diferenca += diferenca_tamanho * peso

 

    return diferenca

