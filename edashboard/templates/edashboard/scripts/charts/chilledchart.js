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
            "backgroundColor": ["#76a6fa", "#7bb5e5", "#aed7f4", "#c5e1f5", "#d3ebf0"],
            "borderColor": ["#76a6fa", "#7bb5e5", "#aed7f4", "#c5e1f5", "#d3ebf0"],
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
