//Code for charts
new Chart(document.getElementById("chilled-chart"), {
    "type": "horizontalBar",
    "data": {
        "labels": [{% for data in list_chilled %}
                      "{{ data|safe }}",
                      {% endfor %}],
        "datasets": [{
            "label": "Chilled Water Gallons",
            "data": [{% for data in usage_chilled %}
                          {{ data|safe }},
                          {% endfor %}],
            "fill": false,
            "backgroundColor": ["#7bb5e5","#7bb5e5","#7bb5e5"],
            "borderColor": ["#7bb5e5","#7bb5e5","#7bb5e5"],
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
