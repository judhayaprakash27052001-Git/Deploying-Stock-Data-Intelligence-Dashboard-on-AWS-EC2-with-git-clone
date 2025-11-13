// Fetch companies and populate sidebar
fetch("/companies")
  .then(res => res.json())
  .then(data => {
    let div = document.getElementById('companies');
    data.companies.forEach(symbol => {
      let btn = document.createElement('button');
      btn.innerText = symbol;
      btn.onclick = () => showChart(symbol);
      div.appendChild(btn);
    });
  });

function showChart(symbol) {
  fetch(`/data/${symbol}`)
    .then(res => res.json())
    .then(data => {
      let dates = data.map(row => row.Date);
      let close = data.map(row => row.Close);
      let trace = { x: dates, y: close, type: 'scatter', name: symbol };
      Plotly.newPlot('chart', [trace], { title: `${symbol} Closing Prices (Last 30 Days)` });
    });
}
