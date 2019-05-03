//Code for charts
new Chart(document.getElementById("elec-chart"), {
    "type": "horizontalBar",
    "data": {
        "labels": [{% for data in list_elec %}
                      "{{ data|safe }}",
                      {% endfor %}],
        "datasets": [{
            "label": "Elec kWh",
            "data": [{% for data in usage_elec %}
                          {{ data|safe }},
                          {% endfor %}],
            "fill": false,
            "backgroundColor": ["#ffcc01"],
            "borderColor": ["#ffcc01"],
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
