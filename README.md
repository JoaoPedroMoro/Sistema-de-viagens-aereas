# 🛬 **Sistema de viagens aéreas**

Neste repositório se encontra o projeto de armazenamento e manipulação de dados para um sistema de viagens aéreas. Tal projeto foi desenvolvido durante a disciplina `1001304 - Processamento Massivo de Dados`, ministrada pela **Profa. Dra. Sahudy M. González** na **Universidade Federal de São Carlos - Campus Sorocaba**.

Alunos envolvidos no projeto:
- João Pedro Moro Bolognini - RA: 792185 - [GitHub](https://github.com/JoaoPedroMoro)
- Renan Aparecido de Almeida - RA: 795239 - [GitHub](https://github.com/littleluwu)

## 📂 **Conjunto de dados**

O conjunto de dados escolhido é um arquivo de passagens aéreas que foram compradas no site de viagens norte-americana Expedia entre as datas de 16/04/2022 e 05/10/2022, no conjunto de dados as datas estão no formato YYYY-MM-DD, partindo e chegando nos aeroportos das cidades de Atlanta (ATL), Dallas (DFW), Denver (DEN), Orlando (ORD), Los Angeles (LAX), Charlotte (CLT), Miami (MIA), Nova Iorque (JFK), Newark (EWR), São Francisco (SFO), Detroit (DTW), Boston (BOS), Filadélfia (PHL), Nova Iorque (LGA), Washington (IAD) e Oklahoma City (OAK).

Essa base de dados possui 31.09 GB e se encontra publicada no [Kaggle](https://www.kaggle.com/), pelo usuário Dillon Wong. Ela conta com aproximadamente 82.1 milhões de registros em sua totalidade, onde esses registros referem-se a 6 milhões de voos catalogados. Para mais informações, a base pode ser acessada em [Flight Prices](https://www.kaggle.com/datasets/dilwong/flightprices)

## ⚙️ **Dependências**

Para o funcionamento adequado do projeto, faz-se necessário a instalação de alguns componentes no ambiente de execução. As seguintes dependências, ou outras versões compatíveis, devem estar disponíveis no ambiente em que o projeto sera executado:

- Python 3.8+
    - py4j
    
    - PySpark

- Java Development Kit 8

- Apache Spark 3.4.3

O esquema de armazenamento dos dados escolhido foi a utilização do sistema NoSQL MongoDB. Portanto, o Apache Spark necessita também das componentes que gerenciam a conexão entre ele e o MongoDB.

- [MongoDB Driver Sync](https://mvnrepository.com/artifact/org.mongodb/mongodb-driver-sync)
- [MongoDB Driver Core](https://mvnrepository.com/artifact/org.mongodb/mongodb-driver-core)
- [MongoDB Bson](https://mvnrepository.com/artifact/org.mongodb/bson)
- [MongoDB Bson Record Codec](https://mvnrepository.com/artifact/org.mongodb/bson-record-codec)