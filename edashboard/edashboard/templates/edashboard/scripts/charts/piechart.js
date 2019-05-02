//Code for charts
new Chart(document.getElementById("pie-chart"), {
    type: 'pie',
    data: {
      labels: ["Electricity","Steam","Dom Water","Reclaimed Water","Chilled Water"],
      datasets: [{
        label: "BTU/Hour",
        backgroundColor: ["#ffcc01","#ff6a6a","#003467","#007867","#aed7f4"],
        //Need to display 10,30,60 <- All need to add up to 100% not actual data value
        // Need python function to call and return today's electricity, cooling, heating, and total from DB in array.
        data: [{{ elecDollar|safe }},{{ steamDollar|safe }},{{ domDollar|safe }},{{ reclaimedDollar|safe }},{{ chilledDollar|safe }}]
      }]
    },
    options: {
      legend: {
        display: false,
            }
          }
        });
