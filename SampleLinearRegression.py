import websocket   # pip install websocket-client
import json

from sklearn import linear_model   # pip install sklearn
from sklearn.metrics import mean_squared_error, r2_score

def coletaDados(num_linhas, num_coef):
   precos_X = []
   precos_Y = [] # 1 se tick 5 foi maior ou 0 se foi menor
   from Hush import APP_ID
   apiUrl = "wss://ws.binaryws.com/websockets/v3?app_id="+APP_ID
   for n in range(num_linhas):
      ws = websocket.create_connection(apiUrl)
      json_data = json.dumps({
        "ticks_history": "frxAUDJPY",
        "end": "latest",
        #"start": 1,
        "style": "ticks",
        "adjust_start_time": 1,
        "count": 5000 })
      ws.send(json_data)
      result = ws.recv()
      ws.close()   # Vamos economizar
      jasao = json.loads(result)
      #print(jasao['history']['prices'])
      #print("Ret=", len(jasao['history']['prices']) )
      for y in range(len(jasao['history']['prices'])-10):   # Vou de 10 em 10
         linhaX = []
         for i in range(y+1,y+10):   # Para cada grupo de 10 itens
            p_atual = float(jasao['history']['prices'][-1*i])
            p_anterior = float(jasao['history']['prices'][-1*i-1])
            v = (p_atual - p_anterior)/(p_anterior)
            #print(i, p_atual, p_anterior, v)
            linhaX.append(v)
         p_tick5 = float(jasao['history']['prices'][-5])
         p_recente = float(jasao['history']['prices'][-1])
         if( p_tick5 > p_recente ):
            tick5 = 1
         else:
            tick5 = 0
         precos_Y.append( tick5 )
         precos_X.append( linhaX )
      if( n % 10 == 0):
         print("N=", n, ", X=", len(precos_X[-1]), ", Y=", len(precos_Y), ", Ret=", len(jasao['history']['prices']))
   #print("N=", n, ", X=", len(precos_X), ", Y=", len(precos_Y) )
   return precos_X, precos_Y

def fazRegressaoLinear(p_X, p_Y):
   #Regressao
   corte = int(len(p_X)/2)
   # Split the data into training/testing sets
   p_X_train = p_X[:-1*corte]
   p_X_test = p_X[-1*corte:]
   
   # Split the targets into training/testing sets
   p_Y_train = p_Y[:-1*corte]
   p_Y_test = p_Y[-1*corte:]
   
   # Create linear regression object
   regr = linear_model.LinearRegression()
   
   # Train the model using the training sets
   regr.fit(p_X_train, p_Y_train)
   
   # Make predictions using the testing set
   p_Y_pred = regr.predict(p_X_test)
   
   return p_X_train, p_X_test, p_Y_train, p_Y_test, p_Y_pred, regr
 
def calculaRetornoSimulado(p_X, p_Y, coefs, inter):
   saldo = 1000
   stake = 1
   s_fraction = 0.05   # Fracao da banca
   ret_medio = 0
   for n in range(len(p_Y)):
      y_calc = inter + sum([x*k for x in p_X[n] for k in coefs])
      #print("N=", n, ", X=", p_X[n], ", Y=", p_Y[n], ", calc=", y_calc)
      stake = 0.05 * saldo
      #if( round(y_calc) == p_Y[n] ):
      if( ((y_calc > 0.65) and  p_Y[n]==1) or ((y_calc < 0.35) and  p_Y[n]==0) ):
         #txt = ", acertou, mizeravi!"
         saldo += 1.8*stake
         ret_medio += 1.8   # Ver retorno unitario
      else:
         #txt = ", e nao foi dessa vez..."
         saldo -= stake
         ret_medio -= 1   # Ver retorno unitario
      #print("N=", n, ", Y=", p_Y[n], ", calc=", y_calc, txt)
   print("saldo=", saldo, ", Ret Md=", 1.0*ret_medio/len(p_Y) )
 
if __name__ == "__main__":
   n_reg=100
   n_coef=10
   p_X, p_Y = coletaDados(n_reg, n_coef)
   #print("X=", p_X, ", Y=", p_Y )
   
   p_X_train, p_X_test, p_Y_train, p_Y_test, p_Y_pred, regr = fazRegressaoLinear(p_X, p_Y)
   
   print("Train=", len(p_X_train), ", test=", len(p_X_test) )
   
   # The coefficients
   print('Coefficients: \n', regr.coef_, ", intercept=", regr.intercept_)
   # The mean squared error
   print("Mean squared error: %.2f" % mean_squared_error(p_Y_test, p_Y_pred))
   # Explained variance score: 1 is perfect prediction
   print('Variance score: %.2f' % r2_score(p_Y_test, p_Y_pred))
   
   calculaRetornoSimulado(p_X_test, p_Y_test, regr.coef_, regr.intercept_ )