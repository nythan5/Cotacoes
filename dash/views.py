from django.shortcuts import render
import requests
from django.http import JsonResponse
from datetime import datetime, timezone

def dashboard_view(request):
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,BTC-BRL"
    response = requests.get(url=url)
    data = response.json()

    cotacoes = {

        "dollar":{
            "compra": float(data['USDBRL']['bid']),
            "venda": float(data['USDBRL']['ask']),
            "data": data['USDBRL']['create_date']
        },

        "bitcoin":{
            "compra": float(data['BTCBRL']['bid']),
            "venda": float(data['BTCBRL']['ask']),
            "data": data['BTCBRL']['create_date']
        }
    }

    return render(request, 'dashboard.html', {'cotacoes':cotacoes})



def get_historical_data(request, moeda):
    # Buscar dados históricos para o Chart.js
    url = f"https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/30"
    response = requests.get(url)

    
    data = response.json()

    # item["create_date"]: A data e hora de cada cotação no formato "2024-12-01 12:15:00".
    # [:10]: Pega apenas os primeiros 10 caracteres para obter a data ("2024-12-01").
    # data[::-1]: Inverte a ordem dos dados (pois a API retorna os mais recentes primeiro), para que o mais antigo seja exibido primeiro no gráfico.


    # Processar os dados
    historico = {
        "dates": [],
        "values": []
    }

    for item in data:
        timestamp = int(item["timestamp"])  # Usa timestamp
        date = datetime.fromtimestamp(timestamp, tz=timezone.utc).strftime('%d-%m-%Y')

        # Pega a cotação 'bid'
        historico["dates"].append(date)
        historico["values"].append(float(item["bid"]))

    return JsonResponse(historico)