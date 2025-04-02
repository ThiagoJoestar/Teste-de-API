# Teste de API

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![Vue.js](https://img.shields.io/badge/Vue.js-2.x-brightgreen)
![Postman](https://img.shields.io/badge/Postman-Collection-orange)

## Descrição
Este projeto consiste no desenvolvimento de uma interface web utilizando **Vue.js** para interagir com um servidor em **Python** (Flask). A aplicação permite realizar buscas textuais na lista de cadastros de operadoras, retornando os registros mais relevantes.

## Tecnologias Utilizadas
- **Python 3.9+**
- **Flask**
- **Pandas**
- **Vue.js 2.x**
- **Axios**
- **Postman** (para testes da API)

## Estrutura do Projeto
```
/
├── frontend/               # Interface web Vue.js
│   ├── src/
│   │   ├── components/    # Componentes Vue.js (se aplicável)
│   │   ├── App.vue        # Componente principal
│   │   ├── main.js        # Arquivo principal Vue.js
│   ├── package.json       # Dependências do frontend
│   ├── public/            # Diretório público
├── backend/                # API Flask
│   ├── app.py             # Servidor Flask
│   ├── requirements.txt   # Dependências do backend
│   ├── data/              # Diretório para armazenamento de CSV
├── postman_collection.json # Coleção de testes no Postman
├── README.md               # Documentação do projeto
```

## Instalação e Execução

### Backend (Flask)
1. Clone o repositório:
   ```sh
   git clone https://github.com/seuusuario/nome-do-repositorio.git
   cd nome-do-repositorio/backend
   ```
2. Crie um ambiente virtual e instale as dependências:
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Execute a API:
   ```sh
   python app.py
   ```
   O servidor estará rodando em `http://localhost:5000`

### Frontend (Vue.js)
1. Acesse a pasta do frontend:
   ```sh
   cd ../frontend
   ```
2. Instale as dependências:
   ```sh
   npm install
   ```
3. Inicie o servidor Vue:
   ```sh
   npm run serve
   ```
   O frontend estará rodando em `http://localhost:8080`

## Uso da API

### Endpoint: Buscar Operadora
- **URL:** `/search`
- **Método:** `GET`
- **Parâmetro:** `query` (texto a ser buscado)
- **Exemplo de requisição:**
  ```sh
  curl "http://localhost:5000/search?query=OperadoraX"
  ```
- **Resposta (JSON):**
  ```json
  [
    {
      "id_operadora": 123,
      "nome": "OperadoraX"
    }
  ]
  ```

## Testes com Postman
Uma coleção de testes foi preparada no Postman para facilitar a verificação dos endpoints. Basta importar o arquivo `postman_collection.json` e executar os testes.

## Contato
- **Thiago Piassi** - [LinkedIn](https://www.linkedin.com/in/thiagopiassi/)

