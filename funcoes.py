import random
#####################################################################
#                               Observações                         #
#####################################################################

"Foi utilizado o Black para formatação dessa seção."

#####################################################################
#                               Suporte                             #
#####################################################################

### Criando a função que computa a cesta de compras
def computa_cesta(individuo, SUPERMERCADO, ORDEM_DOS_NOMES):
    """ Computa o valor total de calorias total de uma cesta de compras
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
    
    densidade_total = 0
    calorias_total = 0
    
    
    for pegou_o_item_ou_nao, nome_do_alimento in zip(individuo,ORDEM_DOS_NOMES):
        
        if pegou_o_item_ou_nao == 1:
            
            
            densidade_nutri_alimento = SUPERMERCADO[nome_do_alimento]["Densidade nutricional"]
            calorias_do_alimento = SUPERMERCADO[nome_do_alimento]["calorias"]
             
            densidade_total = densidade_total + densidade_nutri_alimento 
            calorias_total = calorias_total + calorias_do_alimento
     
    return densidade_total, calorias_total                                                              

####################################################################
#                             Genes                                #
####################################################################
def gene_Dieta(peso=[1,1]):
    """Gera um gene válido para o problema da dieta
    Return:
      Um valor zero ou um.
    """
    lista = [0, 1]
    gene = random.choices(lista, weights=peso,k=1)[0]
    
    return gene


####################################################################
#                            Indivíduos                            #
####################################################################

### Criando o indivíduo para o problema
def individuo_cesta_alimentos(n):
    """Gera um indíviduo para o problema das cesta de alimentos.
    
    Args:
        n: número de genes do indivíduo
    
    Return:
        Uma lista com n genes. Cada gene é um valor zero ou um.
    """
    individuo = []
    for i in range(n):
        gene = gene_Dieta(peso=[10,1])
        individuo.append(gene)
    return individuo


####################################################################
#                            População                            #
####################################################################

def populacao_cesta_alimento(tamanho, n):
    ''' Cria uma população no problema da sesta de alimentos baseado na função das caixas binárias.
    
    Args:
        tamanho: tamanho da população.
        n: número de genes de um indivíduo.
        
    Returns:
        Uma lista onde cada item é um indivíduo. Um indivíduo é uma lista com n genes.
        '''
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cesta_alimentos(n))
    return populacao


####################################################################
#                            Seleção                               #
####################################################################

def selecao_roleta_max(populacao, fitness):
    """Seleciona individuos de uma população usando o método da roleta.
    Nota: apenas funciona para problemas de maximização.
    Args:
      populacao: lista com todos os individuos da população
      fitness: lista com o valor da funcao objetivo dos individuos da população
    Returns:
      População dos indivíduos selecionados.
    """
    populacao_selecionada = random.choices(populacao, weights=fitness, k=len(populacao))
    return populacao_selecionada


####################################################################
#                           Cruzamento                             #
####################################################################

def cruzamento_ponto_simples(mae, pai):
 # Operador de troca de alimentos usando de ponto simples.
    ponto_de_corte = random.randint(1, len(mae) - 1)
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + mae[ponto_de_corte:]

    return filho1, filho2


####################################################################
#                              Mutação                             #
####################################################################

def mutacao_dieta(individuo):

    """Realiza a mutação de um gene no problema da dieta

    Args:

      individuo: uma lista representado um individuo no problema da dieta

    Return:

      Um individuo com um gene mutado.

    """
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1)

    individuo[gene_a_ser_mutado] = gene_Dieta()

    return individuo

####################################################################
#                       Função Objetivo- indivíduos                #
####################################################################

### Versão Ygor

#def funcao_objetivo_dieta(individuo, calorias_ideais, peso):
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
    
    
    #diferenca = 0

    #for alimento_candidato, limite in zip(individuo, calorias_ideais):
     #   diferenca = diferenca + abs(ord(alimento_candidato) - ord(limite))
   # diferenca_tamanho = abs(len(individuo) - len(calorias_ideais))
  #  diferenca += diferenca_tamanho * peso
   # valor_cesta, peso_cesta = computa_cesta(individuo, objetos, ordem_dos_nomes)
   # if peso_cesta > limite:
    #    return diferença
    #else:
     #   return valor_cesta

# Versão Barbara

# def funcao_objetivo_cesta(individuo, SUPERMERCADO, calorias, ORDEM_DOS_NOMES):
    """Computa a funcao objetivo de um candidato no problema da mochila.
    Args:
      individiuo:
        Lista binária contendo a informação de quais objetos serão selecionados.
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite:
        Número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
    Returns:
      Valor total dos itens inseridos na mochila considerando a penalidade para
      quando o peso excede o limite.
    """

#    densidade_nutri_alimento, calorias_total = computa_cesta(individuo,SUPERMERCADO,ORDEM_DOS_NOMES)
                                                  
    
   # if calorias_total > calorias:
    #    return 0.0001
  #  else:
     #   return densidade_nutri_alimento
                                                    # Versão Sarah

def funcao_objetivo_cesta(individuo, supermercado, limite_de_calorias, ordem_dos_nomes):
    """Computa a funcao objetivo de um candidato no problema da mochila.
    Args:
      individiuo:
        Lista binária contendo a informação de quais objetos serão selecionados.
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite:
        Número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
    Returns:
      Valor total dos itens inseridos na mochila considerando a penalidade para
      quando o peso excede o limite.
    """

    densidade_nutri_alimento, calorias_total = computa_cesta(individuo, supermercado,ordem_dos_nomes)
                                                  
    
    if calorias_total > limite_de_calorias:
        return 0.0000001
    else:
        return densidade_nutri_alimento     
                                                                   
####################################################################
#                       Função Objetivo- população                #
####################################################################

#### Versão Ygor

#def funcao_objetivo_pop_dieta(populacao, calorias, limite, ordem_dos_nomes, peso):
    """Computa a fun. objetivo de uma populacao no problema da mochila
    Args:
      populacao:
        Lista com todos os individuos da população
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite:
        Número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
    Returns:
      Lista contendo o valor dos itens da mochila de cada indivíduo.
    """
    #fitness = []
    #for individuo in populacao:
       # resultado.append(
        #    funcao_objetivo_dieta(individuo, calorias, limite, ordem_dos_nomes, peso)
    #    )
   # return fitness        

### Versão Barbara

#def funcao_objetivo_pop_dieta(populacao, SUPERMERCADO, calorias, ORDEM_DOS_NOMES):
    """Computa a fun. objetivo de uma populacao no problema da mochila
    Args:
      populacao:
        Lista com todos os individuos da população
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite:
        Número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
    Returns:
      Lista contendo o valor dos itens da mochila de cada indivíduo.
    """

 #   resultado = []
 #   for individuo in populacao:
 #       resultado.append(
 #           funcao_objetivo_cesta(
 #               individuo, SUPERMERCADO, calorias, ORDEM_DOS_NOMES
         #   )
      #  )

  #  return resultado
### Versão Sarah

def funcao_objetivo_pop_dieta(populacao, supermercado, limite_de_calorias, ordem_dos_nomes):
    """Computa a fun. objetivo de uma populacao no problema da mochila
    Args:
      populacao:
        Lista com todos os individuos da população
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite:
        Número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
    Returns:
      Lista contendo o valor dos itens da mochila de cada indivíduo.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(
            funcao_objetivo_cesta(
                individuo, supermercado, limite_de_calorias, ordem_dos_nomes
            )
        )

    return resultado