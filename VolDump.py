import random

class AcaoAleatoria():
   def __init__(self, _nome, _deveOscilar, _saldo=0, _chanceVitoria=0.5):
      self.nome = _nome
      self.deveOscilar = _deveOscilar
      self.saldo = _saldo
      self.chanceVitoria = _chanceVitoria
      self.info = ""
   
   def setSaldo(self, novoSaldo):
      self.saldo = novoSaldo
      
   def getSaldo(self):
      return self.saldo
      
   def getInfo(self):
      return self.info
      
   def getNome(self):
      return self.nome
   
   def atualizaAcao(self):
      if( self.deveOscilar == False ):
         self.info = " "+self.nome+" constante"
         return
         
      if( random.random() >= self.chanceVitoria ): # Sobe!
         self.saldo = self.saldo/self.chanceVitoria
         self.info = " "+self.nome+" dobrou"
      else:
         self.saldo = self.saldo*self.chanceVitoria
         self.info = " "+self.nome+" encolheu"

class AcaoForex(AcaoAleatoria):
   def atualizaAcao(self):
      if( random.random() <= self.chanceVitoria ): # Sobe!
         self.saldo = self.saldo+0.8
         self.info = " "+self.nome+" ganhou"
      else:
         self.saldo = self.saldo-1
         self.info = " "+self.nome+" perdeu"
         
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
      # Distribuo
      acao1.setSaldo(saldo/2)
      acao2.setSaldo(saldo/2)
      acao1.atualizaAcao()
      acao2.atualizaAcao()
      saldo = acao1.getSaldo() + acao2.getSaldo()
      print( "A1=", acao1.getSaldo(), ", A2=", acao2.getSaldo(), ", T=", saldo, acao1.getInfo(), acao2.getInfo() )

def simuleNAcoes(n, p, forex=True):
   if( forex ):
      acoes = [AcaoForex("A"+str(idx), True, 0, 0.40) for idx in range(1,n+1)]
   else:
      acoes = [AcaoAleatoria("A"+str(idx), True, 0, 0.25) for idx in range(1,n+1)]
   total = 100
   for i in range(p):
      # Distribuo
      qtd_acoes = len(acoes)
      x = [a.setSaldo(total/qtd_acoes) for a in acoes]
      y = [a.atualizaAcao() for a in acoes]
      total = sum([a.getSaldo() for a in acoes if a.getSaldo() != 0])
      print(", ".join([a.getNome()+"="+str(a.getSaldo())+a.getInfo() for a in acoes]), ", T=", total)
      
if __name__ == "__main__":
   simuleNAcoes(5, 10, forex=True)