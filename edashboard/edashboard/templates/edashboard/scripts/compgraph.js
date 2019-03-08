{% load staticfiles %}

  new Chart(document.getElementById("line-chart"), {
  type: 'line',
  data: {
  labels: [{% for data in db_id %}
                {{ data }},
              {% endfor %}],
  fillOpacity: .3,
  datasets: [{
      data: [{% for data in db_data %}
                    {{ data }},
                  {% endfor %}],
      label: "B13 ELEC",
      borderColor: "#1f61a8",
      fill: origin,
      backgroundColor: "rgba(31,97,168,.3)",
    },
    {
      data: [27,3,28,9,38,1,6],
      label: "B13A GAS",
      borderColor: "#ffcc01",
      fill: origin,
      backgroundColor: "rgba(255,204,1,.3)",
    }]
  },
  options: {
  responsive: false,
  title: {
    display: true,
    text: "SAS Building Electricity usage",
  },
  scales: {
  xAxes: [{
    scaleLabel: {
      display: true,
      labelString: 'Time'
    }
  }],
  yAxes: [{
    scaleLabel: {
      display: true,
      labelString: 'Electricity (kWh)'
    }}]}
  }});
