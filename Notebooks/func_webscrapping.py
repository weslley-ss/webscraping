from bs4 import BeautifulSoup
import requests
import nltk
from nltk.corpus import stopwords # É um dos conjuntos de dados inclusos em corpus incluindo diferentes idiomas.
from nltk.tokenize import word_tokenize # Contém funções para dividir o texto em unidades menores, como palavras ou frases.

#nltk.download('stopwords') # Garante que as listas de stopwords dos idiomas estejam disponíveis localmente no ambiente de desenvolvimento
#nltk.download('punkt') # A word_tokenize() para dividir uma string de texto em palavras, o NLTK utiliza o modelo punkt para identificar corretamente os limites das palavras
#nltk.download('punkt_tab')

def busca_google(termos = None):
    soup = None
    # Garante que o retorno do request terá o mesmo conteúdo do navegador
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}

    if termos is None:
        termos = input("Pesquisar no google:")
    else:
        termos = termos.replace(" ", "+")
    
    url = 'https://www.google.com/search?q='+termos
    pagina = requests.get(url, headers = headers)

    if pagina.status_code == 200:
        #print("Website found successfully :)")
        print("Search: ", url) ## Exibindo a url para poder acompanhar os links e tags da página também no navegador
        html = pagina.text
        soup = BeautifulSoup(html, features='html.parser')
        return soup
    else: 
        print("Something went wrong :(")
        return None


def seleciona_atr(soup, selecao = 'a', atr = 'href'):    
    retorno = []
    items = soup.select(selecao)
    for item in items:
        if atr == "text":
            texto = item.get_text()
            retorno.append(item.get_text())

        elif item.has_attr(atr): 
            valor = item.get(atr) # Caso o atributo não existisse o retorno da função seria None
            retorno.append(valor)
        else:
            retorno.append(None)
    return retorno

def cria_soup(url = None):
    soup = None
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}

    try:
        pagina = requests.get(url, headers=headers)
        if pagina.status_code == 200:
            html = pagina.text
            soup = BeautifulSoup(html, features='html.parser')
            return soup
        else:
            return None
    except Exception as e:
        #print(f"An error occurred: {e}")
        return None

def extrair_texto_limpo(soup):
    # Remove elementos desnecessários
    for script in soup(["script", "style", "header", "footer", "nav", "aside"]):
        script.extract()
    
    # Extrair o texto
    texto = soup.get_text(separator=" ")

    # Limpar o texto, removendo múltiplas quebras de linha e espaços extras
    texto_limpo = ' '.join(texto.split())
    
    return texto_limpo

def remove_stopwords(texto, idioma = "portuguese"):
    # Obter a lista de stopwords para o idioma especificado
    stop_words = set(stopwords.words(idioma))

    # Tokenizar o texto
    palavras = word_tokenize(texto)
    
    # Filtrar as palavras que não são stopwords e nem pontuações
    palavras_filtradas = []
    for palavra in palavras:
        if palavra.lower() not in stop_words and palavra.isalpha():
            palavras_filtradas.append(palavra.lower())
    
    # Juntar as palavras filtradas de volta em uma string
    texto_limpo = ' '.join(palavras_filtradas)
    
    return texto_limpo

def verificar_texto_legivel(texto):
    # Conta o número de caracteres "legíveis", ou seja, letras, números e espaços
    caracteres_legiveis = sum(c.isalnum() or c.isspace() for c in texto)
    
    # Calcula a proporção de caracteres legíveis em relação ao comprimento total do texto
    proporcao_legivel = caracteres_legiveis / len(texto)
    
    # Se mais de 70% do texto é legível, consideramos que é texto válido
    return proporcao_legivel > 0.7
