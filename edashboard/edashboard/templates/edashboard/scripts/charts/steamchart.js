//Code for charts
new Chart(document.getElementById("steam-chart"), {
    "type": "horizontalBar",
    "data": {
        "labels": [{% for data in list_steam %}
                      "{{ data|safe }}",
                      {% endfor %}],
        "datasets": [{
            "label": "Steam BTU",
            "data": [{% for data in usage_steam %}
                          {{ data|safe }},
                          {% endfor %}],
            "fill": false,
            "backgroundColor": ["#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a"],
            "borderColor": ["#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a","#ff6a6a"],
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
