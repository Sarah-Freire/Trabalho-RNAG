![Logo do GitHub](https://github.com/Sarah-Freire/Trabalho-RNAG/raw/main/A2.png)

![LICENSE](https://img.shields.io/badge/LICENSE-GNU%20General%20Public%20License%20v3.0-red)

<h1 align="center"> Nutrella: O Algoritmo Genético que faz a sua dieta! </h1>

O Nutrella é um algoritmo genético baseado no problema da mochila com restrição. O nosso algoritmo utiliza uma base de dados brasileira de alimentos para montar uma dieta otimizada para o seu bem-estar. O algoritmo é de otimização visando maximizar a nutrição do consumidor, por entregar os alimentos mais nutritivos, sempre respeitando o limite calórico que ele deve consumir.

Não caia na rotina, use Nutrella.

Com Nutrella, toda vez que rodar o código você receberá uma nova dieta.

## Bem-vindo!

Este repositório de GitHub é dedicado para a disciplina de Redes Neurais e Algoritmos Genéticos do 3° semestre do Bacharelado em Ciência e Tecnologia da Ilum Escola de Ciência, faculdade parte do Centro Nacional de Pesquisa em Energia e Materiais (CNPEM), ministrada pelo Profº [Cassar. Daniel](https://github.com/drcassar). O projeto é um trabalho realizado para o atividade final da disciplina. Desse modo, abaixo temos uma explicação do trabalho e os responsaveis: 

 - [Barbara Perez](https://github.com/barbaraperez) - 220040
 - [Sarah Freire](https://github.com/Sarah-Freire) - 220043
 - [Vitor Barelli](https://github.com/Leprechas) - 220072
 - [Ygor Ruas](https://github.com/YgorRuas) - 220066

<details>
    
__<summary>O que é o Nutrella e o motivo da sua criação :orange:</summary>__
    
<p align="justify"> Nutrella é o nome dado a este código, o qual procura uma dieta razoável para o usuário. Desse modo, usando Algoritmos Genéticos para gerar a dieta e, para que seja possível, tem-se um dataframe contendo uma lista de vários alimentos comuns na alimentação brasileira. Pensando nisso, o diferencial em relação aos demais concorrentes é que aqui, toda vez que após interagir com o código uma dieta nova será retornada, de moto a evitar alimentações repetitivas, mantendo a qualidade nas escolhas, estas que são dadas pelos melhores indivíduos (alimentos) encontrados na busca usado pelo algoritmo.  

Além disso, sua criação se deu pelo objetivo de cientificamente poder proporcionar uma dieta com alimentos acessíveis para a população, dado o objetivo de cada usuário.
</p>
</details>

<details>

__<summary>Como foi feito 🥗</summary>__
    
<p align="justify">O código foi feito fazendo uma adaptação no algoritmo genético para o problema clássico da mochila. Portanto, o funcionamento do código é semelhante e baseia-se em encontrar a melhor resposta possível dadas as opções, que nesse caso é uma dieta que aproxima-se do numero de calorias "ideal" que foi retornado pelas perguntas anteriores.

Desse modo, como grande mudança temos a função obevtivo, já que além de buscar uma dieta com bons valores de calorias ela busca os melhores índices possíveis para o valor nutricional, dado as restrições. E para compreender melhor como é a estrutura de um algoritmo genético e o que cada termo usado durante as etapas do código temos o glossario abaixo:

- __*Indivíduos*:__ Em algoritmos genéticos, os indivíduos são soluções potenciais para um problema. Cada indivíduo é representado por um cromossomo, que contém genes que codificam características ou traços específicos.

- __*População*:__ Uma população é uma coleção de indivíduos que são avaliados e evoluídos ao longo do tempo. A população representa a geração atual de soluções potenciais.

- __*Gene*:__ Um gene é uma seção específica de um cromossomo que codifica um traço ou característica particular. Por exemplo, em um algoritmo genético para otimizar o design de uma asa de avião, um gene pode representar o ângulo no qual a asa está inclinada.

- __*Cromossomos*:__ Um cromossomo é uma sequência de genes que representa uma solução individual para o problema em questão. Em algoritmos genéticos codificados em binário, os cromossomos são geralmente representados como sequências de 0s e 1s.

- __*Geração*:__ Uma geração refere-se a uma iteração do algoritmo genético. Durante cada geração, a função de aptidão é aplicada para avaliar os indivíduos da população, e novos indivíduos são criados por meio de seleção, cruzamento e mutação.

- __*Função de objetivo*:__ A função de aptidão é usada para avaliar o quão bem cada indivíduo da população resolve o problema em questão. Ela atribui uma pontuação de aptidão a cada indivíduo com base em quão próximo sua solução está de ser ótima.

- __*Seleção*:__ A seleção é o processo pelo qual os indivíduos com pontuações de aptidão mais altas têm maior probabilidade de serem escolhidos para reprodução (ou seja, passar seus genes adiante) do que aqueles com pontuações de aptidão mais baixas.

- __*Cruzamento*:__ O cruzamento envolve a combinação de dois cromossomos parentais para criar um ou mais cromossomos filhos. Esse processo pode ajudar a criar novas combinações de genes que podem levar a melhores soluções.

- __*Mutação*:__ A mutação envolve a alteração aleatória de um ou mais genes no cromossomo de um indivíduo. Esse processo pode ajudar a introduzir novos traços na população que podem levar a melhores soluções.

</p>
</details>

## Principais arquivos

<p align="justify"> Guia para navegar no Git da Nutrella; </p>

Desse modo, as seguintes pastas compõem esse repositório:
- [Alimentos - Calorias.xlsx](https://github.com/Sarah-Freire/Trabalho-RNAG/blob/main/Alimentos%20-%20Calorias.xlsx): É uma tabela excel que possibilita encontrar os alimentos e seus dados de calorias e densidade nutricional
- [Alimentos.xlsx](https://github.com/Sarah-Freire/Trabalho-RNAG/blob/main/Alimentos.xlsx): É uma tabela excel, onde podemos encontrar os alimentos e seus dados de calorias, proteínas, lipídios, carboidratos e fibra alimentar
- [Tratando dados.ipynb](https://github.com/Sarah-Freire/Trabalho-RNAG/blob/main/Tratando%20dados.ipynb): Notebook o qual utiliza o arquivo excel "Alimentos.xlsx" e altera os seus dados para produzir os dados de densidade nutricional e gerar o arquivo excel "Alimentos - Calorias.xlsx".
- [LICENSE](https://github.com/Sarah-Freire/Trabalho-RNAG/blob/main/LICENSE): Apresenta a licença usada no repositório
- [README.md](https://github.com/YgorRuas/Redes_Neuro_Anais/blob/main/README.md): Guia para o repositório
- [funcoes.py](https://github.com/Sarah-Freire/Trabalho-RNAG/blob/main/funcoes.py): Arquivo python a qual armazenam todas as funções utilizadas no decorrer do trabalho.
- [trabalho_rnag.ipynb](https://github.com/Sarah-Freire/Trabalho-RNAG/blob/main/trabalho_rnag.ipynb): É o notebook onde o trabalho foi desenvolvido.


![Logo do GitHub](https://github.com/Sarah-Freire/Trabalho-RNAG/raw/main/A1.png)
