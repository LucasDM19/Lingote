"""
Define as coletas de dados da API da Binary.com
"""

import websocket   # pip install websocket-client
import json
from Hush import API_TOKEN, APP_ID

class Binary():

   def __init__(self, _num_linhas=None, _num_coef=None, _moeda=None):
      if(_num_linhas is not None): self.setNumLinhas(_num_linhas)
      if(_num_coef is not None): self.setNumCoeficiente(_num_coef)
      if(_moeda is not None): self.setMoeda(_moeda)
      self.token = API_TOKEN # Para autorizar antes da aposta
   
   def setNumLinhas(self, _num_linhas):
      self.num_linhas = _num_linhas
      
   def setNumCoeficiente(self, _num_coef):
      self.num_coef = _num_coef
      
   def setMoeda(self, _moeda):
      self.moeda = _moeda
   
   def getX(self):
      return self.precos_X
   
   def getY(self):
      return self.precos_Y
      
   def getMoeda(self):
      return self.moeda

   def chamaURL(self, json_data, keepAlive=False, ws=None):
      apiUrl = "wss://ws.binaryws.com/websockets/v3?app_id="+APP_ID
      if( ws is None ):
         ws = websocket.create_connection(apiUrl)
      ws.send(json_data)
      result = ws.recv()
      jasao = json.loads(result)
      if( 'error' in jasao ):   # Erro na chamada
         print("Erro na chamada!", jasao['error']['message'])
      if( not keepAlive ):
         ws.close()   # Vamos economizar
         return jasao
      return jasao, ws   # Retorna conexao
   
   def obtemSaldo(self):
      json_data = json.dumps({
         "balance": 1,
         "subscribe": 1 })
      jasao = self.chamaURL(json_data)
      print( jasao['balance']['balance'] )
      return jasao['balance']['balance']
   
   def obtemUltimoPreco(self):
      json_data = json.dumps({
        "ticks_history": self.moeda,
        "end": "latest",
        "style": "ticks",
        "adjust_start_time": 1,
        "count": 1 })
      jasao = self.chamaURL(json_data)
      return float(jasao['history']['prices'][0])
   
   def fazAposta(self, quantidade, simbolo, tipo="CALL", n_tick=5):
      #Autorizando
      json_data = json.dumps({
         "authorize": self.token
      })
      jasao, ws = self.chamaURL(json_data, keepAlive=True, ws=None)
      #print( jasao )
      
      #Criando contrato
      json_data = json.dumps({
        "proposal": 1,
        "amount": str(quantidade),
        "basis": "payout",
        "contract_type": tipo, # "CALL" para acima "PUT" para Abaixo
        "currency": "USD",
        "duration": str(n_tick),
        "duration_unit": "t",
        "symbol": simbolo })
      jasao, ws = self.chamaURL(json_data, keepAlive=True, ws=ws)
      #print( jasao ) # jasao['error']['message']
      if( 'error' in jasao ): return
      id_contrato = str(jasao['proposal']['id'])
      
      #Enviando contrato
      ultimo_preco = round(self.obtemUltimoPreco(),2)
      ultimo_preco = 100  # Preco maximo
      json_data = json.dumps({
         "buy": id_contrato, #"5951bc87-4967-5eb5-5c73-f1de191ac903",
         "price": ultimo_preco })
      jasao = self.chamaURL(json_data, keepAlive=False, ws=ws)
      return jasao
   
   def coletaDado(self, qtd_registros, funcaoAvalia):
      json_data = json.dumps({
        "ticks_history": self.moeda,
        "end": "latest",
        #"start": 1,
        "style": "ticks",
        "adjust_start_time": 1,
        "count": qtd_registros })
      jasao = self.chamaURL(json_data)
      #print(jasao['history']['prices'][0:2])
      #print("Ret=", len(jasao['history']['prices']) )
      precos_X = []
      precos_Y = [] # 1 se tick 5 foi maior ou 0 se foi menor
      if('history' not in jasao):
         print("JSon estranho!", jasao['error']['code'], " - ", jasao['error']['message'])
      else: # Tudo blz com o Json
         for y in range(len(jasao['history']['prices'])-self.num_coef):   # Vou de 10 em 10
            linhaX = []
            for i in range(y+1,y+self.num_coef):   # Para cada grupo de 10 itens
               p_atual = float(jasao['history']['prices'][-1*i])
               p_anterior = float(jasao['history']['prices'][-1*i-1])
               v = (p_atual - p_anterior)/(p_anterior)
               #print(i, p_atual, p_anterior, v)
               linhaX.append(v)
               #linhaX.append(p_atual - p_anterior)
            tick_meio = int(self.num_coef/2)
            p_tick5 = float(jasao['history']['prices'][-1*tick_meio])
            p_recente = float(jasao['history']['prices'][-1])
            tick5 = funcaoAvalia(p_tick5, p_recente)
            precos_Y.append( tick5 )
            precos_X.append( linhaX )
      return precos_X, precos_Y, len(jasao['history']['prices'])
               
   def coletaDados(self, silencioso, funcaoAvalia):
      precos_X = []
      precos_Y = [] # 1 se tick 5 foi maior ou 0 se foi menor
      self.MAX_REQ = 5000
      quantidade_inteira = int(self.num_linhas / self.MAX_REQ)
      quantidade_fracao = self.num_linhas % self.MAX_REQ
      for n in range(quantidade_inteira):
         X1, Y1, tot_prices = self.coletaDado(self.MAX_REQ, funcaoAvalia)
         precos_X += X1
         precos_Y += Y1
         if( n % 10 == 0 and not silencioso):
            print("N=", n, ", X=", len(precos_X[-1]), ", Y=", len(precos_Y), ", Ret=", tot_prices)
      X2, Y2, tot_prices = self.coletaDado(quantidade_fracao, funcaoAvalia)
      precos_X += X2
      precos_Y += Y2
      if( not silencioso and len(precos_X) > 1 ):
         try:
            print("X=", len(precos_X[-1]), ", Y=", len(precos_Y), ", Ret=", tot_prices)
         except IndexError:
            print(self.num_linhas, quantidade_fracao, X2, precos_X)
      self.precos_X = precos_X
      self.precos_Y = precos_Y
      
if __name__ == "__main__":
   b = Binary()
   print("Binary Funciona!")