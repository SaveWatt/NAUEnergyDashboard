//Code for charts
new Chart(document.getElementById("dom-chart"), {
    "type": "horizontalBar",
    "data": {
        "labels": [{% for data in list_dom %}
                      "{{ data|safe }}",
                      {% endfor %}],
        "datasets": [{
            "label": "Dom Water Gallons",
            "data": [{% for data in usage_dom %}
                          {{ data|safe }},
                          {% endfor %}],
            "fill": false,
            "backgroundColor": ["#0c64c9", "#1b75c8", "#2b8cbe", "#3ca0c8", "#4eb3d3", "#71c2dc"],
            "borderColor": ["#0c64c9", "#1b75c8", "#2b8cbe", "#3ca0c8", "#4eb3d3", "#71c2dc"],
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
