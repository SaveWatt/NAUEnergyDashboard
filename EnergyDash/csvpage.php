<?php

$host = '192.168.0.9';
$user = 'testUser';
$password = 'passpass';
$database = 'testDB';

$con = new mysqli($host, $user, $password, $database);

$query = "SELECT Sample_Value, Time_Of_Sample FROM 601sam100";
if (!$result = mysqli_query($con, $query)) {
    exit(mysqli_error($con));
}

if (mysqli_num_rows($result) > 0) {
    $number = 1;
    $users = '<table class="table table-bordered">
        <tr>
            <th>No.</th>
            <th>Sample Value</th>
            <th>Time Of Sample</th>
        </tr>
    ';
    while ($row = mysqli_fetch_assoc($result)) {
        $users .= '<tr>
            <td>'.$number.'</td>
            <td>'.$row['Sample_Value'].'</td>
            <td>'.$row['Time_Of_Sample'].'</td>
        </tr>';
        $number++;
    }
    $users .= '</table>';
}

?>

<html>
  <head>
    <link rel="stylesheet" type="text/css" href="stylesheet.css">
    <script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>
    <meta charset="UTF-8">
    <title>Export Data from MySQL to CSV Tutorial | iTech Empires</title>
    <link rel="stylesheet" type="text/css" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"/>
  </head>
  <body>
    <div class="container" style="clear:both;">
      <div id='leftdiv' style="float: left; height: 100%; width:fit-content;">
        <div class='sideheader' id='sideheader' style="z-index: 2;">
          <div class="imgborder">
            <img id="logo" src="logo.png" style="margin:1%;">
          </div>
        </div>
        <?php include 'Sidebar.php'; ?>
      </div>
      <div id='rightdiv' style="float: left; width:-webkit-fill-available;">
        <?php include 'Header.php'; ?>
        <div class="container">
            <div class="form-group">
                <?php echo $users ?>
            </div>
            <div class="form-group">
                <button onclick="Export()" class="btn btn-primary">Export to CSV File</button>
            </div>
        </div>
      </div>
    </div>
  </body>
</html>

<script>
function fixdivs() {
    var divw = document.getElementById('sidebar').offsetWidth;
    document.getElementById('sideheader').style.width = divw + 'px';
    var divh = document.getElementById('Topnav').offsetHeight;
    document.getElementById('sideheader').style.height = divh + 'px';
}
  fixdivs();

  function Export()
  {
      window.open("tocsv.php", '_blank');
  }
</script>
