"""
Classe que simula apostas.
"""

class Apostas():

   def __init__(self, _fraction=None, _stake=None ):
      if( _fraction is not None ): self.setFraction(_fraction)
      if( _stake is not None ): self.setStake(_stake)

   # fracao da banca
   def setFraction(self, _fraction):
      #if _fraction is None: _fraction = 0.05
      self.s_fraction = _fraction

   # Quanto sera apostado
   def setStake(self, _stake=1):
      self.stake = _stake
      
   def getSaldo(self):
      return self.saldo
   
   def getRetMedio(self):
      return self.ret_medio

   def calculaRetornoSimulado(self, p_X, p_Y, coefs, inter):
      saldo = 1000
      ret_medio = 0
      for n in range(len(p_Y)):
         y_calc = inter + sum([x*k for x in p_X[n] for k in coefs])
         #print("N=", n, ", X=", p_X[n], ", Y=", p_Y[n], ", calc=", y_calc)
         self.stake = self.s_fraction * saldo
         #if( round(y_calc) == p_Y[n] ):
         if( ((y_calc > 0.65) and  p_Y[n]==1) or ((y_calc < 0.35) and  p_Y[n]==0) ):
            #txt = ", acertou, mizeravi!"
            saldo += 1.8*self.stake
            ret_medio += 1.8   # Ver retorno unitario
         else:
            #txt = ", e nao foi dessa vez..."
            saldo -= self.stake
            ret_medio -= 1   # Ver retorno unitario
         #print("N=", n, ", Y=", p_Y[n], ", calc=", y_calc, txt)
      self.ret_medio = 1.0*ret_medio/len(p_Y)
      self.saldo = saldo
      
if __name__ == "__main__":
   a = Apostas()
   print("Aposta Funciona!")