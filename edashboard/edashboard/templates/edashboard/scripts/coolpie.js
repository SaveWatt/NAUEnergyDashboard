{% load staticfiles %}

new Chart(document.getElementById("pie-chart-cool"), {
    type: 'pie',
    data: {
      labels: ["Electricity","Cooling", "Heating"],
      datasets: [{
        label: "BTU/Hour",
        backgroundColor: ["#e3e3e3","#003467","#ffcc01"],
        //Need to display 10,30,60 <- All need to add up to 100% not actual data value
        // Need python function to call and return today's electricity, cooling, heating, and total from DB in array.
        data: [{% for data in usage_cool %}
                {{ data|safe }},
              {% endfor %}]
      }]
    },
    options: {
      maintainAspectRatio: false,
      legend: {
        display: false,
            }
          }
        });
