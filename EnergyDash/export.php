<html>
  <head>
    <link rel="stylesheet" type="text/css" href="stylesheet.css">
    <script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>
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
        <div class="rightcont">
          <button id="export">Export</button>
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
</script>
