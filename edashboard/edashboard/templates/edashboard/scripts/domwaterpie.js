{% load staticfiles %}

new Chart(document.getElementById("pie-chart-domwater"), {
    type: 'pie',
    data: {
      labels: ["B46","B62","B50A","B95 Pump House","B60","B86","B14 Main","B14 Bypass"],
      datasets: [{
        label: "BTU/Hour",
        backgroundColor: ["#e3e3e3","#003467","#ffcc01","#cfe0e8","#b7d7e8","#87bdd8","#daebe8","#5b9aa0"],
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
