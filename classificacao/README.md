# Desafio: Prever os usuários com alta chance de deixar seu Streaming
Desafio feito como desafio do curso da [Escola DNC](https://www.escoladnc.com.br) (Cientista de Dados)

### Situação
- Você trabalha em uma plataforma de streaming e a diretoria está preocupada com o alto índice de usuários cancelando as suas assinaturas. Eles acreditam que é possível prever se um usuário tem mais chance de deixar a plataforma antes que isso aconteça, e com base nessa informação tomar ações para reduzir o churn.

### Tarefa
- Criar um modelo de classificação capaz de prever se um usuário tem mais chance de cancelar a sua assinatura na plataforma ou não. Para isso, a empresa forneceu uma base de dados em csv contendo dados sobre as contas dos clientes.

### Ação
- Foi utilizado as bibliotecas Pandas, Sklearn, Matplotlib,  para realizar o projeto, Pandas para fazer a limpeza e manipulação dos dados, Sklearn para gerar e treinar os modelos e Matplotlib para gerar gráficos e gerar insights visuais.
- Os modelos utilizados foram de *Regressão Logística* e *Random Forest*.
- Extensões da biblioteca Sklearn foram utilizadas para realizar calculo de métricas, normalizar os dados numéricos, transformar as variáveis categóricas em numéricas e para achar os melhores hiperparâmetros com o GridSearchCV.

### Resultado
- Depois de uma busca dos melhores hiperparâmetros dos modelos, foi obtido uma média de 80% de acurácia, assim, ajudando a empresa a saber que tipo de padrão se repete para usuários Churn ou não Churn e assim conseguir elaborar um plano de marketing mais sólido e diminuir o número de Churn.
