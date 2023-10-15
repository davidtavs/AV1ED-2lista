import requests

API_KEY = "ca57e6cf06dc3d4c05b6d20dff24f9ef"
cidade = input("Bem vindo ao app do tempo, digite a cidade para saber sua descrição e temperatura: \n->")
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

#[se der print (req)]link funcionando = 200 / nao encontrou = 404 / server indisponivel = 500
req = requests.get(link)

if req.status_code == 200:
    req_dic = req.json()
    descricao = req_dic['weather'][0]['description'] # [0] é pra pegar um item da lista "weather"
    temperatura =req_dic['main']['temp'] - 273.15 #diminuir para transfomar em celsius
    print(f"a cidade de {cidade} está com o tempo: {descricao} e sua temperatura é de: {temperatura:.2f}°C")
else:
    print("Cidade inexistente")
