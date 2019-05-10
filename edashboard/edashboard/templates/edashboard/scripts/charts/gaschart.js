//Code for charts
new Chart(document.getElementById("gas-chart"), {
    "type": "horizontalBar",
    "data": {
        "labels": [{% for data in list_gas %}
                      "{{ data|safe }}",
                      {% endfor %}],
        "datasets": [{
            "label": "Gas Usage",
            "data": [{% for data in usage_gas %}
                          {{ data|safe }},
                          {% endfor %}],
            "fill": false,
            "backgroundColor": ["#000000","#000000","#000000","#000000","#000000","#000000"],
            "borderColor": ["#000000","#000000","#000000","#000000","#000000","#000000"],
            "borderWidth": 1
        }]
    },
    "options": {
        "scales": {
            "xAxes": [{
                "ticks": {
                    "beginAtZero": true
                }
            }]
        }
    }
});
