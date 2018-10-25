import random

class AcaoAleatoria():
   def __init__(self, _nome, _deveOscilar, _saldo=0):
      self.nome = _nome
      self.deveOscilar = _deveOscilar
      self.saldo = _saldo
      self.info = ""
   
   def setSaldo(self, novoSaldo):
      self.saldo = novoSaldo
      
   def getSaldo(self):
      return self.saldo
      
   def getInfo(self):
      return self.info
   
   def atualizaAcao(self):
      if( self.deveOscilar == False ):
         self.info = " "+self.nome+" constante"
         return
         
      if( random.random() >= 0.5 ): # Sobe!
         self.saldo = 2*self.saldo
         self.info = " "+self.nome+" dobrou"
      else:
         self.saldo = self.saldo/2
         self.info = " "+self.nome+" encolheu"
         

def simulaUmaAcao():
   saldo = 100
   acao1 = AcaoAleatoria("A1", True, 0)   # Tenho 0 nessa acao1
   acao2 = AcaoAleatoria("$$", False, 0)   # Dinheiro
   for n in range(10):   # 100 periodos
      info = ""
      # Distribuo
      acao1.setSaldo(saldo/2)
      acao2.setSaldo(saldo/2)
      acao1.atualizaAcao()
      acao2.atualizaAcao()
      saldo = acao1.getSaldo() + acao2.getSaldo()
      print( "A1=", acao1.getSaldo(), ", A2=", acao2.getSaldo(), ", T=", saldo, acao1.getInfo(), acao2.getInfo() )

def simulaDuasAcoes():
   saldo = 100
   acao1 = AcaoAleatoria("A1", True, 0)   # Tenho 0 nessa acao1
   acao2 = AcaoAleatoria("A2", True, 0)   # Acao tambem
   for n in range(10):   # 100 periodos
      info = ""
      # Distribuo
      acao1.setSaldo(saldo/2)
      acao2.setSaldo(saldo/2)
      acao1.atualizaAcao()
      acao2.atualizaAcao()
      saldo = acao1.getSaldo() + acao2.getSaldo()
      print( "A1=", acao1.getSaldo(), ", A2=", acao2.getSaldo(), ", T=", saldo, acao1.getInfo(), acao2.getInfo() )

if __name__ == "__main__":
   simulaDuasAcoes()