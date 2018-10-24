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
   
   def percorreModelo(self, n_reg, n_coef, moeda):
      self.b = Binary(n_reg, n_coef, moeda ) # Coleto os dados
      self.b.coletaDados(silencioso=False)
      
      # Faz a regressao      
      self.rl = RegressaoLinear( self.b.getX(), self.b.getY() )
      self.rl.fazRegressaoLinear(indice_corte=0.5)
      
      self.a = Apostas(_fraction=0.05, _stake=1)
      self.a.calculaRetornoSimulado( self.rl.getX_Test(), self.rl.getY_Test(), self.rl.getCoeficients(), self.rl.getIntercept() )
      
if __name__ == "__main__":
   while True: # Sim
      h = Highlander()
      print("Highlander vive e funciona!")
      from random import randint
      n_reg = randint(3, 2000)
      n_coef = randint(3, 20)
      import random
      moedas = ["frxUSDJPY", "frxGBPUSD", "frxAUDUSD", "frxUSDCAD", "frxEURJPY", "frxUSDCHF", "frxEURCHF", "frxEURGBP", "frxAUDJPY"]
      moeda=random.choice(moedas)
      h.percorreModelo(n_reg, n_coef, moeda)
      print("Reg=", n_reg, ", coef=", n_coef, ", moeda=", moeda, ", saldo=", h.getApostas().getSaldo(), " ret_medio=", h.getApostas().getRetMedio() )