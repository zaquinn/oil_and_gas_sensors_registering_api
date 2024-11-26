# Documentação da API 

## Tabela de Conteúdos
  - [1. Visão Geral](#1-visão-geral)
  - [2. Endpoints](#2-endpoints)

---
## 1. Visão Geral

O projeto consiste em uma aplicação Backend que visa ser responsável pelo registro e leitura de sensores de equipamentos de estações de óleo e gás.

Através desta API é possível registrar os valores de sensores no seguinte formato:

```json
{
    "equipmentId": "EQ-12495",
    "timestamp": "2023-02-15T01:30:00.000-05:00",
    "value": 78.42
}
```

Também é possível realizar os registros através de um arquivo CSV, seguindo o formato:
equipmentId | timestamp | value 
--- | --- | --- 
EQ-12495 | 2023-02-12T01:30:00.000-05:00 | 78.8
EQ-12499 | 2023-02-11T01:30:00.000-04:00 | 65.33

Para visitar o repositório do projeto Front End que consome esta API, clique <a href="" target="_blank">aqui</a>.

Tecnologias utilizadas:
- [Python](https://www.python.org/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLModel](https://sqlmodel.tiangolo.com/)
- [Pandas](https://pandas.pydata.org/docs/)
- [PostgreSQL](https://www.postgresql.org/docs/)
- [Docker](https://docs.docker.com/)

Url base da aplicação:

---
## 2. Endpoints

Esta seção inclui as rotas da aplicação.

[ Voltar para o topo ](#tabela-de-conteúdos)

- [Sensors](#1-sensors)
    - [POST - /sensors](#11-registro-dos-dados-de-um-sensor)
    
## 1. Sensors
Estas são as rotas relacionadas registro e leitura dos dados dos sensores.



### 1.1. Registro dos dados de um sensor
### `/sensors/`

### Exemplo de Request:
```
POST /sensors/
Host: 
Content-type: application/json
```

### Corpo da Requisição:
```json
{
    "equipmentId": "EQ-12499",
    "timestamp": "2023-02-16T01:30:00.000-05:00",
    "value": 73.81
}
```
### Exemplo de Resposta:
```
200 Success
```

```json
{
	"id": 1,
	"equipmentId": "EQ-12499",
	"timestamp": "2023-02-16T03:30:00",
	"value": "73.81"
}
```
[ Voltar para Endpoints ](#2-endpoints)

### 1.2. Registro dos dados de um sensor a partir de um arquivo CSV
### `/sensors/from-csv/`

### Exemplo de Request:
```
POST /sensors/from-csv/
Host: 
Content-type: multipart/form-data
```

### Exemplo de arquivo CSV:
equipmentId | timestamp | value 
--- | --- | --- 
EQ-12495 | 2023-02-12T01:30:00.000-05:00 | 78.8
EQ-12499 | 2023-02-11T01:30:00.000-04:00 | 65.33
### Exemplo de Resposta:
```
200 Success
```

```json
[  
    {
        "id": 1,
        "equipmentId": "EQ-12495",
        "timestamp": "2023-02-12T01:30:00.000-05:00",
        "value": "78.8"
    },
    {
        "id": 2,
        "equipmentId": "EQ-124999",
        "timestamp": "2023-02-11T01:30:00.000-04:00",
        "value": "65.33"
    }
]
```
[ Voltar para Endpoints ](#2-endpoints)

---