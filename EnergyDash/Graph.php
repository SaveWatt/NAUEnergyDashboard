    <div id="div-container">
    <canvas id="line-chart"></canvas>
    </div>

<script>
new Chart(document.getElementById("line-chart"), {
  type: 'line',
  data: {
    labels: [
      <?php
          $conn = mysqli_connect("10.18.106.255", "testUser", "passpass", "testDB");

          $query = 'SELECT Time_Of_Sample FROM tblTrendlog_0000601_0000000000 WHERE Sequence BETWEEN 1 AND 500';
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
            $conn = mysqli_connect("10.18.106.255", "testUser", "passpass", "testDB");

            $query = 'SELECT Sample_Value FROM tblTrendlog_0000601_0000000000 WHERE Sequence BETWEEN 1 AND 500';
            $result = mysqli_query($conn, $query);
            while( $row = mysqli_fetch_array($result) ) {
            	echo $row['Sample_Value'] . ',';
            }
            mysqli_close($conn);
          ?>],
        label: "Week 1",
        borderColor: "#1f61a8",
        fill: origin,
        backgroundColor: "rgba(31,97,168,.3)",
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
