"""
Classe que busca um modelo que pode ser lucrativo.
Um tipo de cola, que utiliza as outras classes.
"""

from RegressaoLinear import RegressaoLinear
from Apostas import Apostas
from Binary import Binary

class Highlander():

   def __init__(self):
      pass
      
   def getApostas(self):
      return self.a
      
   def getRegLin(self):
      return self.rl
   
   def percorreModelo(self, n_reg, n_coef, moeda):
      self.b = Binary(n_reg, n_coef, moeda ) # Coleto os dados
      self.b.coletaDados(silencioso=True)
      
      # Faz a regressao      
      self.rl = RegressaoLinear( self.b.getX(), self.b.getY() )
      self.rl.fazRegressaoLinear(indice_corte=0.5)
      
      self.a = Apostas(_fraction=0.05, _stake=1)
      self.a.calculaRetornoSimulado( self.rl.getX_Test(), self.rl.getY_Test(), self.rl.getCoeficients(), self.rl.getIntercept() )
      
      print("Reg=", n_reg, ", coef=", n_coef, ", moeda=", moeda, ", saldo=", h.getApostas().getSaldo(), " ret_medio=", h.getApostas().getRetMedio(), "eq=", h.getRegLin().getCoeficients(), "+", h.getRegLin().getIntercept() )
   
   def apostaBinary(self, n_reg, n_coef, moeda):
      n_reg2 = int(n_reg/2) # Modelo apenas metade
      self.b = Binary(n_reg2, n_coef, moeda ) # Coleto os dados
      self.b.coletaDados(silencioso=True)
      
      # Faz a regressao      
      self.rl = RegressaoLinear( self.b.getX(), self.b.getY() )
      self.rl.fazRegressaoLinear(indice_corte=-1) # Com -1, nao faz Test
      
      if( h.getRegLin().getIntercept() == 1 ):
         tipo="CALL"
      else:
         tipo="PUT"
      n_tick = int(n_coef/2)
      self.b.fazAposta(2.1, self.b.getMoeda(), tipo, n_tick ) # Atencao!
      
      print("Reg=", n_reg2, ", coef=", n_coef, ", moeda=", moeda, "eq=", h.getRegLin().getCoeficients(), "+", h.getRegLin().getIntercept() )
   
if __name__ == "__main__":
   for i in range(50):
      h = Highlander()
      print("Highlander vive e funciona!")
      from random import randint
      n_reg = randint(3, 9000)
      n_coef = randint(10, 20)
      import random
      #moedas = ["frxUSDJPY", "frxGBPUSD", "frxAUDUSD", "frxUSDCAD", "frxEURJPY", "frxUSDCHF", "frxEURCHF", "frxEURGBP", "frxAUDJPY"]
      #moedas = ["frxUSDJPY", "frxGBPUSD", "frxAUDUSD", "frxEURJPY", "frxUSDCHF", "frxEURCHF", "frxEURGBP", "frxAUDJPY"]
      moedas = ["frxAUDJPY"]
      moeda=random.choice(moedas)
      #h.percorreModelo(n_reg, n_coef, moeda)
      h.apostaBinary(n_reg, n_coef, moeda)      