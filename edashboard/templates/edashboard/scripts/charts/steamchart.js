//Code for charts
new Chart(document.getElementById("steam-chart"), {
    "type": "horizontalBar",
    "data": {
        "labels": ["B88","B36","B60","B60"],
        "datasets": [{
            "label": "Steam BTU",
            "data": [{% for data in usage_steam %}
                          {{ data|safe }},
                          {% endfor %}],
            "fill": false,
            "backgroundColor": ["#ff6a6a", "#ff8667", "#ffba69", "#ffcf85", "#fff6b7"],
            "borderColor": ["#ff6a6a", "#ff8667", "#ffba69", "#ffcf85", "#fff6b7"],
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
