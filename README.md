# Lingote
Em busca do Cisne Negro cavalgando um Unicórnio.

# Componentes
- LinearRegressionDiabetes.py
Uma Regressão Linear com a base de exemplo, para classificar diabetes.
- Sample.py
Se conecta na API da Binary, e obtém um fluxo infinito de variações da moeda.
- SampleLinearRegression2.py
Primeira tentativa de fazer uma Regressão Linear com o fluxo da API Binary. 
- SampleLinearRegression.py
Regressão Linear com o histórico de uma moeda, via API da Binary. 
- Highlander.py
Buscador de cenários e variações. Acha o melhor hiper parâmetro para a Regressão Linear. 
- RegressaoLinear.py
Faz Regressão Linear de conjuntos X e Y informados.
- Binary.py
Acessa a API da Binary, e retorna os dados em formatos X Y.
- Apostas.py
Simula apostas do mercado Binary, usando a Regressão Linear.
- VolDump.py
Simulador de Volatility Dump, ou o Shannon's Demon.

# Requisitos
websocket-client
Sklearn

O scipy precisa do Visual C++ Redistributable for Visual Studio 2015, caso rode no Windows.
 - https://stackoverflow.com/questions/33600302/installing-scipy-in-python-3-5-on-32-bit-windows-7-machine
 - https://www.microsoft.com/en-us/download/details.aspx?id=48145