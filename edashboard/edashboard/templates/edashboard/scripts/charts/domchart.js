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
            "backgroundColor": ["#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9"],
            "borderColor": ["#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9","#0c64c9"],
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
