# Web Scraping 

## Índice:

### 1.Notebook de fundamentos: BeautifulSoup e Requests
Este notebook é um exemplo de como desenvolver funções simples e utilitárias para facilitar a extração de dados e a análise de conteúdo de páginas web. Com **Requests**, fazemos requisições HTTP para obter o HTML de páginas web, e com **BeautifulSoup**, navegamos pela estrutura HTML para extrair informações relevantes.

#### Funcionalidades Principais

- **busca_google()**: Realiza buscas no Google utilizando palavras-chave fornecidas como parâmetros.
- **seleciona_atr()**: Extrai valores de atributos específicos ou textos de elementos HTML, permitindo personalizar o seletor HTML e o atributo desejado.
- **remove_stopwords()**: Filtra palavras irrelevantes (stopwords) do texto, utilizando a biblioteca NLTK, para uma análise de conteúdo mais eficiente.
- **extrair_texto_limpo()**: Ela identifica e remove tags como `<script>`, `<style>`, `<header>`, `<footer>`, `<nav>`, e `<aside>`, que geralmente não contêm o texto principal.
- **verifica_texto_legivel()**: Avalia se o texto extraído de um documento ou página web é "legível" e significativo, se a maior parte do texto consiste em caracteres alfanuméricos.

#### Aplicação
1. Identificação de Tópicos Relevantes: Analisar essas palavras permite identificar os temas mais discutidos e relevantes, ajudando a refinar futuras buscas e a entender o que está em alta.
2. Treinamento de Modelos de Linguagem (LLM): Os textos extraídos podem ser usados para treinar modelos de linguagem, melhorando sua capacidade de gerar respostas precisas e relevantes, baseadas em dados atualizados.
____


