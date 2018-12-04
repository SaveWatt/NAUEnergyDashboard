<div id="div-container">
<canvas id="line-chart"></canvas>
</div>

<script>
new Chart(document.getElementById("line-chart"), {
type: 'line',
data: {
labels: ["00:00","01:00","02:00","03:00","04:00","05:00","06:00","07:00","08:00","09:00","10:00"],
fillOpacity: .3,
datasets: [{
    data: [15203.04,15284.88,13507.83,14654.75,16106.85,15894.85,15989.33,14696.22,16431.25,13622,12053],
    label: "Week 1",
    borderColor: "#1f61a8",
    fill: origin,
    backgroundColor: "rgba(31,97,168,.3)",
  },
  {
      data: [16509.04,15890.88,16288.83,16805.75,16082.85,16510.85,14714.33,15047.22,15737.25,16564,17394],
      label: "Week 2",
      borderColor: "#ffcc01",
      fill: origin,
      backgroundColor: "rgba(255,204,1,.3)",
    }
]
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
  }
}]
}
}
});
</script>
