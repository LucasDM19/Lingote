import websocket   # pip install websocket-client
import json

def on_open(ws):
   json_data = json.dumps({'ticks':'frxAUDJPY'})   # R_100 - Volatility 100 Index
   ws.send(json_data)

def on_message(ws, message):
   #print('ticks update: %s' % message)   # ticks update: {"echo_req":{"ticks":"R_100"},"msg_type":"tick","tick":{"ask":"6877.80","bid":"6875.80","epoch":"1539885954","id":"28fc0dd3-c04c-588f-cd6c-17bbda459c8d","quote":"6876.80","symbol":"R_100"}}
   jasao = json.loads(message)
   print('Mudou. Bid=', jasao['tick']['bid'] )   # Tem Bid ou Ask. Spread = Ask-Bid
   p = float(jasao['tick']['bid'])
   novoPreco(p)

def novoPreco(p):
   if( preco_anterior > -1  ):
      v = (1.0*p - preco_anterior)/(preco_anterior)
      print(p - preco_anterior)
      linha_var_X.append(v)
   print("V=", linha_var_X)
   preco_anterior = p
   
if __name__ == "__main__":
   precos_X = []
   linha_var_X = []   # Controla as ultimas nove variacoes de precos
   preco_anterior = -999.0
   from Hush import APP_ID
   apiUrl = "wss://ws.binaryws.com/websockets/v3?app_id="+APP_ID
   ws = websocket.WebSocketApp(apiUrl, on_message = on_message, on_open = on_open)
   ws.run_forever()