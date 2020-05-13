import tweepy

chave_consumidor = ''
segredo_consumidor = ''
token_acesso = ''
token_acesso_segredo = ''

menssagem = input('Sobre qual tema você gostaria de pesquisar no Twitter ?')

autenticacao = tweepy.OAuthHandler(chave_consumidor, segredo_consumidor)
autenticacao.set_access_token(token_acesso, token_acesso_segredo)

twitter = tweepy.API(autenticacao)

resultados = twitter.search(q = '{menssagem}')
for tweet in resultados:
     print(f'Tweet: {tweet.text}')
