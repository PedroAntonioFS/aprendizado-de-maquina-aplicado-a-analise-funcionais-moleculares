# Aprendizado de máquina aplicado a Análises Funcionais Moleculares

### Esse repositório foi o resultado do meu projeto de TCC intitulado [Estudo e implementação de algoritmos de aprendizagem de máquina supervisionado aplicados a avaliações comportamentais no contexto clínico](https://drive.google.com/file/d/1Vsja8qt6qJNm2Fdh5Nq0QP_xMe4zMVyv/view?usp=sharing)

## Resumo
Este trabalho propõe o uso de um algoritmo de aprendizado de máquina supervisionado aplicados em análises funcionais moleculares contidas
em avaliações comportamentais realizadas no contexto clínico por psicoterapeutas. O modelo desenvolvido por este trabalho é um sistema de
classificação de textos que rotula contingências (antecedentes, respostas, consequentes e efeitos) entre possíveis processos: reforço positivo, reforço negativo, punição positiva, punição negativa ou extinção. Entretanto, pelas informações serem textuais, foram aplicadas técnicas e métodos de processamento de linguagem natural durante a desenvolvimento. O classificador obtido demonstrou, em seu melhor resultado, 81.37% de acurácia média em uma validação cruzada.

## Metodologia
A metodologia aplicada foi baseada em uma Fayyad, Piatetsky-Shapiro e Smith (1996) e outra Vajjala et. al. (2020), melhor explicada nesse [artigo](https://drive.google.com/file/d/1Vsja8qt6qJNm2Fdh5Nq0QP_xMe4zMVyv/view?usp=sharing). 

Há quatro etapas: Seleção, Pré-processamento, Transformação e Avaliação.

### Seleção
Os dados selecionados manualmente estão no arquivo [BD_analises_funcionais.xlsx](https://github.com/PedroAntonioFS/aprendizado-de-maquina-aplicado-a-analises-funcionais-moleculares/blob/dev/BD_analises_funcionais.xlsx).

### Pré-processamento
As rotinas aplicadas estão no arquivo [pre-processing.ipynb](https://github.com/PedroAntonioFS/aprendizado-de-maquina-aplicado-a-analises-funcionais-moleculares/blob/dev/pre-processing.ipynb). Os procedimentos aplicados gerou as bases de dados [preprocessed_lemmatization.xlsx](https://github.com/PedroAntonioFS/aprendizado-de-maquina-aplicado-a-analises-funcionais-moleculares/blob/dev/preprocessed_lemmatization.xlsx) e [preprocessed_stemming.xlsx](https://github.com/PedroAntonioFS/aprendizado-de-maquina-aplicado-a-analises-funcionais-moleculares/blob/dev/preprocessed_stemming.xlsx).

### Transformação e Mineração
As rotinas aplicadas estão no arquivo [transformation_and_data_mining.ipynb](https://github.com/PedroAntonioFS/aprendizado-de-maquina-aplicado-a-analises-funcionais-moleculares/blob/dev/transformation_and_data_mining.ipynb). 

### Avaliação
As rotinas aplicadas também estão no arquivo [transformation_and_data_mining.ipynb](https://github.com/PedroAntonioFS/aprendizado-de-maquina-aplicado-a-analises-funcionais-moleculares/blob/dev/transformation_and_data_mining.ipynb). Os resultados detalhados e comentados podem encontram-se no [artigo](https://drive.google.com/file/d/1Vsja8qt6qJNm2Fdh5Nq0QP_xMe4zMVyv/view?usp=sharing).

## Referências
FAYYAD, U. M.; PIATETSKY-SHAPIRO, G.; SMYTH, P. (1996). From data mining to knowledge in databases. AI Magazine, [Menlo Park], v.17, n.3, mar, 1996.  Disponível em: < https://www.aaai.org/ojs/index.php/aimagazine/article/view/1230 >. Acesso em: 09 de abr. 2022.

VAJJALA, S.; et. al. Pratical natural language processing: a comprehensive guide to build real-world nlp systems. 1st ed. Sebastapool: O’Reilly Media, 2020.
