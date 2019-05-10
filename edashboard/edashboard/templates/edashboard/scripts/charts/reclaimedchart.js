//Code for charts
new Chart(document.getElementById("reclaimed-chart"), {
    "type": "horizontalBar",
    "data": {
        "labels": [{% for data in list_reclaimed %}
                      "{{ data|safe }}",
                      {% endfor %}],
        "datasets": [{
            "label": "Reclaimed Water Gallons",
            "data": [{% for data in usage_reclaimed %}
                          {{ data|safe }},
                          {% endfor %}],
            "fill": false,
            "backgroundColor": ["#387f55", "#387f55"],
            "borderColor": ["#387f55", "#387f55"],
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
