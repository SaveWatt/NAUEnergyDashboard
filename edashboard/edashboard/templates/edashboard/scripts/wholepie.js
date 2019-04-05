{% load staticfiles %}

new Chart(document.getElementById("pie-chart"), {
    type: 'pie',
    data: {
      labels: ["Electricity","Steam", "Dom Water", "Reclaimed Water"],
      datasets: [{
        label: "BTU/Hour",
        backgroundColor: ["#e3e3e3","#003467","#ffcc01","f31363"],
        //Need to display 10,30,60 <- All need to add up to 100% not actual data value
        // Need python function to call and return today's electricity, cooling, heating, and total from DB in array.
        data: [{{elecToBTU|safe}},{{steamToBTU|safe}},{{domToBTU|safe}},{{reclaimedToBTU|safe}}]
      }]
    },
    options: {
      legend: {
        display: false,
            }
          }
        });
