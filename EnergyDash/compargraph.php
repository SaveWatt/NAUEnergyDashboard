<div id="div-container">
<canvas id="line-chart"></canvas>
</div>

<script>
new Chart(document.getElementById("line-chart"), {
type: 'line',
data: {
labels: [
  <?php
      $conn = mysqli_connect("192.168.0.9", "testUser", "passpass", "testDB");

      $query = 'SELECT Time_Of_Sample FROM tblTrendlog_0000210_0000000049 WHERE Sequence BETWEEN 4 AND 53';
      $result = mysqli_query($conn, $query);

      while( $row = mysqli_fetch_array($result) ) {
        echo '"'.$row['Time_Of_Sample'].'",';
      }
      mysqli_close($conn);
    ?>
],
fillOpacity: .3,
datasets: [{
    data: [
      <?php
            $conn = mysqli_connect("192.168.0.9", "testUser", "passpass", "testDB");

            $query = 'SELECT Sample_Value FROM tblTrendlog_0000210_0000000049 WHERE Sequence BETWEEN 4 AND 53';
            $result = mysqli_query($conn, $query);

            while( $row = mysqli_fetch_array($result) ) {
              echo $row['Sample_Value'].',';
            }
            mysqli_close($conn);
          ?>
    ],
    label: "B13 GAS",
    borderColor: "#1f61a8",
    fill: origin,
    backgroundColor: "rgba(31,97,168,.3)",
  },
  {
      data: [
        <?php
            $conn = mysqli_connect("192.168.0.9", "testUser", "passpass", "testDB");

            $query = 'SELECT Sample_Value FROM tblTrendlog_0000210_0000000028 WHERE Sequence BETWEEN 8 AND 57';
            $result = mysqli_query($conn, $query);

            while( $row = mysqli_fetch_array($result) ) {
              echo $row['Sample_Value'].',';
            }
            mysqli_close($conn);
          ?>
      ],
      label: "B13A GAS",
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
