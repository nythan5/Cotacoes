// Função para buscar dados históricos e renderizar gráficos
async function renderChart(moeda, chartId) {
    const response = await fetch(`/historical/${moeda}/`);
    const data = await response.json();

    const ctx = document.getElementById(chartId).getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.dates,
            datasets: [{
                label: `Histórico de ${moeda.toUpperCase()} (Compra)`,
                data: data.values,
                borderColor: 'rgb(12, 231, 231)',
                borderWidth: 1,
                fill: false,
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    title: { display: true, text: 'Datas' },
                    ticks:{color:'white'},
                    grid: {
                        color: 'rgba(255, 255, 255, 0.1)'  // Cor branca com transparência para o grid
                    }
                },
                y: {
                    title: { display: true, text: 'Cotação (BRL)' },
                    ticks:{color:'white'},
                    grid: {
                        color: 'rgba(255, 255, 255, 0.1)'  // Cor branca com transparência para o grid
                    }
                }
            }
        }
    });
}

// Renderizar gráficos
renderChart('usd', 'chartDollar');
renderChart('btc', 'chartBitcoin');
