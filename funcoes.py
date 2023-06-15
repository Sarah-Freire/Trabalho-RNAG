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

### Criando a função que computa a cesta de compras

def computa_cesta(individuo, alimentos, ordem_dos_alimentos):
    """ Computa o valor total e calorias total de uma cesta de compras
    Args:
        individuo:
            lista binária contendo informação de quais alimentos serão selecionados.
        objetos:
            Dicionário onde as chaves são os nomes dos alimentos e os valores são
            dicionários com a informação do peso e valor.
        ordem_dos_nomes:
            Lista contendo a ordem dos nomes dos objetos.
    Returns:
        calorias_total: calorias total dos itens da cesta.
        quantia_total: quantidade de alimentos dentro da cesta
    """
    
    calorias_total = 0
    densidade_total = 0
    
    for pegou_o_item_ou_nao, nome_do_alimento in zip(individuo,ordem_dos_nomes):
        
        if pegou_o_item_ou_nao == 1:
            
            densidade_nutri_alimento = alimentos[nome_do_alimento]["Densidade nutricional]
            calorias_do_alimento = alimentos[nome_do_alimento]["calorias"]
             
            densidade_total = densidade_total + densidade_nutri_alimento 
            calorias_total = calorias_total + calorias_do_alimento
     
     return densidade_total, calorias_total                                                              

