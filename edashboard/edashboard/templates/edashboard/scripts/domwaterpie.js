{% load staticfiles %}

new Chart(document.getElementById("pie-chart-domwater"), {
    type: 'pie',
    data: {
      labels: [{% for data in list_dom %}
              "{{ data|safe }}",
            {% endfor %}],
      datasets: [{
        label: "BTU/Hour",
        backgroundColor: ["#e3e3e3","#003467","#ffcc01","#722132"],
        //Need to display 10,30,60 <- All need to add up to 100% not actual data value
        // Need python function to call and return today's electricity, cooling, heating, and total from DB in array.
        data: [{% for data in usage_dom %}
                {{ data|safe }},
              {% endfor %}]
      }]
    },
    options: {
      legend: {
        display: false,
            }
          }
        });