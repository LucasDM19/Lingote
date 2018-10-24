"""
Classe que faz a regressao linear dos dados informados. 
A intencao e atuar como uma substituta do Weka.
"""

from sklearn import linear_model   # pip install sklearn
from sklearn.metrics import mean_squared_error, r2_score

class RegressaoLinear:

   # So na hora de instanciar que tenta importar
   def __init__(self, _X=None, _Y=None):
      if( _X is not None ): self.setX(_X)
      if( _Y is not None ): self.setY(_Y)
   
   # Define valores X, ordenada
   def setX(self, X):
      self.X = X
      
   # Define valores Y, absissa
   def setY(self, Y):
      self.Y = Y
   
   def getX_Train(self):
      return self.X_train
   
   def getX_Test(self):
      return self.X_test
      
   def getY_Train(self):
      return self.Y_train
   
   def getY_Test(self):
      return self.Y_test
      
   def getY_Pred(self):
      return self.Y_pred
      
   def getCoeficients(self):
      return self.regr.coef_
      
   def getIntercept(self):
      return self.regr.intercept_
   
   #Separa entre dados para modelo e para testes
   def separaDados(self):
      self.corte = int(len(self.X)*self.indice_corte)
      
      # Split the data into training/testing sets
      self.X_train = self.X[:-1*self.corte]
      self.X_test = self.X[-1*self.corte:]
      
      # Split the targets into training/testing sets
      self.Y_train = self.Y[:-1*self.corte]
      self.Y_test = self.Y[-1*self.corte:]
      
   def fazRegressaoLinear(self, indice_corte=0.5):
      #Regressao
      self.indice_corte = indice_corte
      self.separaDados() # Split the data
      
      # Create linear regression object
      self.regr = linear_model.LinearRegression()
      
      # Train the model using the training sets
      self.regr.fit(self.X_train, self.Y_train)
      
      # Make predictions using the testing set
      self.Y_pred = self.regr.predict(self.X_test)
      
if __name__ == "__main__":
   rl = RegressaoLinear()
   print("Regressao Linear Funciona!")