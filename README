# E-music Chatbot

Este projeto implementa um chatbot de atendimento a clientes para um e-commerce usando o Gemini da Google AI, Flask e Python.

## Configuração do Ambiente

1. **Crie um ambiente virtual:**

   ```bash
   python -m venv venv
   ```

2. **Ative o ambiente virtual:**

   * Windows:
     ```bash
     venv\Scripts\activate
     ```
   * Linux/macOS:
     ```bash
     source venv/bin/activate
     ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

## Variáveis de Ambiente

1. **Crie um arquivo `.env` na raiz do projeto:**

   Este arquivo armazenará a sua chave de API do Gemini.

2. **Adicione a chave de API ao arquivo `.env`:**

   ```
   GEMINI_API_KEY="SUA_CHAVE_DE_API_AQUI"
   ```
   **Substitua `SUA_CHAVE_DE_API_AQUI` pela sua chave de API real.**  Você pode obter uma chave de API no Google Cloud Console.

   O arquivo `.env` fornecido como exemplo contém uma chave de API de demonstração que não funcionará.  **Certifique-se de usar sua própria chave.**

3. **Carregue as variáveis de ambiente:**

   O arquivo `app.py` carrega automaticamente as variáveis de ambiente do arquivo `.env` usando a biblioteca `python-dotenv`.

## Executando a Aplicação

1. **Certifique-se de que o ambiente virtual esteja ativado.**

2. **Execute o aplicativo Flask:**

   ```bash
   python app.py
   ```

3. **Acesse o chatbot:**

   Abra um navegador web e acesse `http://127.0.0.1:5000/`.


## Arquivos Importantes

* **app.py:** Contém o código principal da aplicação Flask, incluindo a lógica do chatbot e as rotas.
* **requirements.txt:** Lista as dependências do projeto.
* **.env:** Armazena as variáveis de ambiente, como a chave de API do Gemini.
* **dados/emusic.txt:** Contém o contexto para o chatbot (dados do e-commerce).
* **helper.py:** Contém funções auxiliares para carregar e salvar dados.
* **selecionar_persona.py:** Contém a lógica para selecionar a persona do chatbot.


## Informações Adicionais

* O chatbot usa o modelo `gemini-1.5-flash`.
* A temperatura do modelo é definida como 0.1 para gerar respostas mais determinísticas.
* O número máximo de tokens de saída é definido como 8192.
* O chatbot tenta gerar uma resposta até um número máximo de vezes, com um tempo de espera entre as tentativas, para lidar com possíveis erros temporários.
