import random

class AcaoAleatoria():
   def __init__(self, _nome, _deveOscilar):
      self.nome = _nome
      self.deveOscilar = _deveOscilar
      
   def atualizaAcao(self):
      if( self.deveOscilar ):
         if( random.random() >= 0.5 ): # Sobe!
            self.saldo = 2*self.saldo
            self.info = " "+self.nome+" dobrou"
         else:
            self.saldo = self.saldo/2
            self.info = " "+self.nome+" encolheu"
         else:
            self.info = " "+self.nome+" constante"

def simulaUmaAcao():
   saldo = 100
   acao1 = 0   # Tenho 0 nessa acao1
   acao2 = 0   # Dinheiro
   for n in range(10):   # 100 periodos
      info = ""
      # Distribuo
      acao1 = saldo/2
      acao2 = saldo/2
      if( random.random() >= 0.5 ): # Sobe!
         acao1 = 2*acao1
         info = " A1 dobrou"
      else:
         acao1 = acao1/2
         info = " A1 encolheu"
      info += " A2 constante"
      saldo = acao1 + acao2
      print( "A1=", acao1, ", A2=", acao2, ", T=", saldo, info)

def simulaDuasAcoes():
   saldo = 100
   acao1 = 0   # Tenho 0 nessa acao1
   acao2 = 0   # Tenho 0 nessa acao2
   for n in range(10):   # 100 periodos
      info = ""
      # Distribuo
      acao1 = saldo/2
      acao2 = saldo/2
      if( random.random() >= 0.5 ): # Sobe!
         acao1 = 2*acao1
         info = " A1 dobrou"
      else:
         acao1 = acao1/2
         info = " A1 encolheu"
      if( random.random() >= 0.5 ): # Sobe!
         acao2 = 2*acao2
         info += " A2 dobrou"
      else:
         acao2 = acao2/2
         info += " A2 encolheu"
      saldo = acao1 + acao2
      print( "A1=", acao1, ", A2=", acao2, ", T=", saldo, info)

if __name__ == "__main__":
   simulaUmaAcao()