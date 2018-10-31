"""
Classe que busca um modelo que pode ser lucrativo.
Um tipo de cola, que utiliza as outras classes.
"""

from RegressaoLinear import RegressaoLinear
from Apostas import Apostas
from Binary import Binary
from Apostas import * # Funcoes

class Highlander():

   def __init__(self):
      pass
      
   def getApostas(self):
      return self.a
      
   def getRegLin(self):
      return self.rl
   
   def percorreModelo(self, n_reg, n_coef, moeda):
      self.b = Binary(n_reg, n_coef, moeda ) # Coleto os dados
      self.b.coletaDados(silencioso=False, funcaoAvalia=avaliaRetornoUp)
      
      # Faz a regressao      
      self.rl = RegressaoLinear( self.b.getX(), self.b.getY() )
      self.rl.fazRegressaoLinear(indice_corte=0.1) # Testo apenas nos ultimos 10%
      
      self.a = Apostas(_fraction=0.05, _stake=1)
      self.a.calculaRetornoSimulado( self.rl.getX_Test(), self.rl.getY_Test(), self.rl.getCoeficients(), self.rl.getIntercept(), funcaoRetorno=calculaRetornoUp )
         
      if( (self.getApostas().getSaldo()) > 1000 and (self.getApostas().qtd_apostas > 3000) and (sum([c for c in self.rl.getCoeficients()]) > 0) ):
         print("Modelagem: Reg=", n_reg, ", coef=", n_coef, ", moeda=", moeda, ", saldo=", self.getApostas().getSaldo(), " ret_medio=", self.getApostas().getRetMedio(), ", qtd=", self.getApostas().qtd_apostas, "eq=", self.getRegLin().getCoeficients(), "+", self.getRegLin().getIntercept() )
         return True
      return False
   
   def apostaBinary(self, n_reg, n_coef, moeda, rl=None):
      n_reg2 = int(n_reg/2) # Modelo apenas metade
      self.b = Binary(n_reg2, n_coef, moeda ) # Coleto os dados
      #self.b.coletaDados(silencioso=True, funcaoAvalia=avaliaRetornoUp) # Sem coleta
      
      # Faz a regressao, se necessario
      if( rl is None ):
         self.rl = RegressaoLinear( self.b.getX(), self.b.getY() )
         self.rl.fazRegressaoLinear(indice_corte=-1) # Com -1, nao faz Test
      else:
         self.rl = rl
      
      # Avaliando os dados atuais
      p_X, y, t = self.b.coletaDado(n_coef, funcaoAvalia=avaliaRetornoUp)
      y_calc = self.getRegLin().getIntercept() + sum([x*k for x in p_X for k in self.getRegLin().getCoeficients()])
      if( y_calc > 0.65 ): 
         tipo="CALL"
      else:
         #tipo="PUT"
         return 0
         
      n_tick = int(n_coef/2)+1
      self.b.fazAposta(2, self.b.getMoeda(), tipo, n_tick ) # Atencao!
      
      #print("Apostando: Reg=", n_reg2, ", coef=", n_coef, ", moeda=", moeda, "eq=", self.getRegLin().getCoeficients(), "+", self.getRegLin().getIntercept() )
      print("Apostando...")
      return 1
      
if __name__ == "__main__":
   totApostas = 0
   for i in range(1):
      h = Highlander()
      print("Highlander vive e funciona!")
      from random import randint
      #n_reg = randint(99849, 15)
      n_reg = 99849*2
      n_coef = randint(10, 20)
      import random
      moedas = ["frxUSDJPY", "frxGBPUSD", "frxAUDUSD", "frxUSDCAD", "frxEURJPY", "frxUSDCHF", "frxEURCHF", "frxEURGBP", "frxAUDJPY"]
      moeda=random.choice(moedas)
      
      valeAPena = h.percorreModelo(n_reg, n_coef, moeda)
      #valeAPena = False
      if( valeAPena ):
         for v in range(5):
            totApostas += h.apostaBinary(int(n_reg), n_coef, moeda, h.getRegLin() )   # Apenas uma parte
            
   print("Total de apostas efetuadas:", totApostas)