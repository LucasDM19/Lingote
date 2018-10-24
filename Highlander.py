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
      
   def percorreModelos(self):
      n_reg=100
      n_coef=10
      moeda="frxAUDJPY"
      b = Binary(n_reg, n_coef, moeda ) # Coleto os dados
      b.coletaDados()
      
      # Faz a regressao      
      rl = RegressaoLinear( b.getX(), b.getY() )
      rl.fazRegressaoLinear(indice_corte=0.5)
      
      a = Apostas()
      a.calculaRetornoSimulado( rl.getX_Test(), rl.getY_Test(), rl.getCoeficients(), rl.getIntercept() )
      print( "Saldo=", a.getSaldo() )
      
if __name__ == "__main__":
   h = Highlander()
   print("Highlander vive e funciona!")
   h.percorreModelos()