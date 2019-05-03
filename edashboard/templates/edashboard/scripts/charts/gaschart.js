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
            "backgroundColor": ["#000000", "#478868", "#619a87", "#6fa597", "#7baea9"],
            "borderColor": ["#000000", "#478868", "#619a87", "#6fa597", "#7baea9"],
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
