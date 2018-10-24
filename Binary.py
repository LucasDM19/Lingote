"""
Define as coletas de dados da API da Binary.com
"""

import websocket   # pip install websocket-client
import json

class Binary():

   def __init__(self, _num_linhas=None, _num_coef=None, _moeda=None):
      if(_num_linhas is not None): self.setNumLinhas(_num_linhas)
      if(_num_coef is not None): self.setNumCoeficiente(_num_coef)
      if(_moeda is not None): self.setMoeda(_moeda)
   
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

   def coletaDados(self, silencioso=True):
      precos_X = []
      precos_Y = [] # 1 se tick 5 foi maior ou 0 se foi menor
      from Hush import APP_ID
      apiUrl = "wss://ws.binaryws.com/websockets/v3?app_id="+APP_ID
      for n in range(self.num_linhas):
         ws = websocket.create_connection(apiUrl)
         json_data = json.dumps({
           "ticks_history": self.moeda,
           "end": "latest",
           #"start": 1,
           "style": "ticks",
           "adjust_start_time": 1,
           "count": 5000 })
         ws.send(json_data)
         result = ws.recv()
         ws.close()   # Vamos economizar
         jasao = json.loads(result)
         #print(jasao['history']['prices'])
         #print("Ret=", len(jasao['history']['prices']) )
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
               p_tick5 = float(jasao['history']['prices'][-5])
               p_recente = float(jasao['history']['prices'][-1])
               if( p_tick5 > p_recente ):
                  tick5 = 1
               else:
                  tick5 = 0
               precos_Y.append( tick5 )
               precos_X.append( linhaX )
         if( n % 10 == 0 and not silencioso):
            print("N=", n, ", X=", len(precos_X[-1]), ", Y=", len(precos_Y), ", Ret=", len(jasao['history']['prices']))
      self.precos_X = precos_X
      self.precos_Y = precos_Y
      #return precos_X, precos_Y
      
if __name__ == "__main__":
   b = Binary()
   print("Binary Funciona!")