//Code for charts
new Chart(document.getElementById("reclaimed-chart"), {
    "type": "horizontalBar",
    "data": {
        "labels": ["B60","B86"],
        "datasets": [{
            "label": "Reclaimed Water Gallons",
            "data": [{% for data in usage_reclaimed %}
                          {{ data|safe }},
                          {% endfor %}],
            "fill": false,
            "backgroundColor": ["#387f55", "#478868", "#619a87", "#6fa597", "#7baea9"],
            "borderColor": ["#387f55", "#478868", "#619a87", "#6fa597", "#7baea9"],
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
