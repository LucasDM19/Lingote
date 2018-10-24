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
      
   def percorreModelo(self, n_reg, n_coef, moeda):
      b = Binary(n_reg, n_coef, moeda ) # Coleto os dados
      b.coletaDados()
      
      # Faz a regressao      
      rl = RegressaoLinear( b.getX(), b.getY() )
      rl.fazRegressaoLinear(indice_corte=0.5)
      
      a = Apostas(_fraction=0.05, _stake=1)
      a.calculaRetornoSimulado( rl.getX_Test(), rl.getY_Test(), rl.getCoeficients(), rl.getIntercept() )
      print( "Saldo=", a.getSaldo() )
      
if __name__ == "__main__":
   while True: # Sim
      h = Highlander()
      print("Highlander vive e funciona!")
      from random import randint
      n_reg = randint(1, 200)
      n_coef = randint(3, 20)
      import random
      moedas = ["frxUSDJPY", "frxGBPUSD", "frxAUDUSD", "frxUSDCAD", "frxEURJPY", "frxUSDCHF", "frxEURCHF", "frxEURGBP", "frxAUDJPY"]
      moeda=random.choice(moedas)
      print("Reg=", n_reg, ", coef=", n_coef, ", moeda=", moeda)
      h.percorreModelo(n_reg, n_coef, moeda)