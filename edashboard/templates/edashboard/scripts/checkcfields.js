{% load staticfiles %}
var fieldId=0;
var building=[null,null,null];
var sensor=[null,null,null];

function addBuilding(){
    var insert_at=0;
    var flag =0;
    var i;
    // Look for available spots
    for(i=0;i<3;i++){
      // if we have an open spot
      if(building[i]==null){
        insert_at=i;
        break;
      }
      //if we get to the end and dont have room
      else if(i==2){
        flag=1;
      }
    }
    if(flag==0){
      var innerdiv = document.createElement('div');
      innerdiv.setAttribute("class", "extrabuildings");
      innerdiv.setAttribute("id", "extrabdiv"+insert_at);
      innerdiv.setAttribute("style","display:block;width: -webkit-fill-available;");
      var stackdiv = document.createElement('div');
      stackdiv.setAttribute("class", "searchremovestack");
      stackdiv.setAttribute("style","display:inline-flex;width: -webkit-fill-available;");
      var innerinput = document.createElement('input');
      innerinput.setAttribute("class", "search");
      innerinput.setAttribute("id", "extrabuild");
      innerinput.setAttribute("placeholder", "Search For Building...");
      innerinput.setAttribute("style","height: fit-content;");
      innerinput.setAttribute("id", "extrabuild");
      var searchresults = document.createElement('ul');
      var idval = "autocomplete-results" + insert_at;
      searchresults.setAttribute("id","autocomplete-results" + insert_at);
      searchresults.setAttribute("class","sidemenu");
      var removebutt = document.createElement('img');
      removebutt.setAttribute("src", "{% static 'edashboard/images/delete.png' %}");
      removebutt.setAttribute("id", "removebutton");
      removebutt.setAttribute("onClick", "removeBuilding("+insert_at+")");
      removebutt.setAttribute("style", "height: 30px;margin: 5% 0;padding-left: 3%;");
      stackdiv.appendChild(innerinput);
      stackdiv.appendChild(removebutt);
      innerdiv.appendChild(stackdiv);
      innerdiv.appendChild(searchresults);
      (document.getElementById("buildingadder")).appendChild(innerdiv);
      fieldId++; // increment fileId to get a unique ID for the new element
      building[insert_at] = 1;
    }
    else{
      alert("You can only graph up to 4 buildings!");
    }
    checkBuildingValues()
}
function addSensor(){
    var insert_at=0;
    var flag =0;
    var i;
    // Look for available spots
    for(i=0;i<3;i++){
      // if we have an open spot
      if(sensor[i]==null){
        insert_at=i;
        break;
      }
      //if we get to the end and dont have room
      else if(i==2){
        flag=1;
      }
    }
    if(flag==0){
      var innerdiv = document.createElement('div');
      innerdiv.setAttribute("class", "extrasensors");
      innerdiv.setAttribute("id", "extrasdiv"+insert_at);
      innerdiv.setAttribute("style","display:inline-flex;width: -webkit-fill-available;");
      var innerinput = document.createElement('input');
      innerinput.setAttribute("class", "search");
      innerinput.setAttribute("id", "extrasens");
      innerinput.setAttribute("placeholder", "Search For Sensor...");
      innerinput.setAttribute("style","height: fit-content;");
      var removebutt = document.createElement('img');
      removebutt.setAttribute("src", "{% static 'edashboard/images/delete.png' %}");
      removebutt.setAttribute("id", "removebutton");
      removebutt.setAttribute("onClick", "removeSensor("+insert_at+")");
      removebutt.setAttribute("style", "height: 30px;margin: 5% 0;padding-left: 3%;");
      innerdiv.appendChild(innerinput);
      innerdiv.appendChild(removebutt);
      (document.getElementById("sensoradder")).appendChild(innerdiv);
      fieldId++; // increment fileId to get a unique ID for the new element
      sensor[insert_at] = 1;
    }
    else{
      alert("You can only graph up to 4 Sensors!");
    }
    //checkSensorValues()
}
function removeBuilding(num){
  innerdiv=document.getElementById("extrabdiv"+num);
  innerdiv.parentNode.removeChild(innerdiv);
  building[num]=null;
  checkBuildingValues()
}
function removeSensor(num){
  innerdiv=document.getElementById("extrasdiv"+num);
  innerdiv.parentNode.removeChild(innerdiv);
  sensor[num]=null;
  //checkSensorValues()
}
//TIME RANGE CODE
$(function() {
    var start = moment().subtract(29, 'days');
    var end = moment();
    function cb(start, end) {
        $('#reportrange span').html(start.format('MMMM D, YYYY') + ' - ' + end.format('MMMM D, YYYY'));
    }
    $('#reportrange').daterangepicker({
        startDate: start,
        endDate: end,
        timePicker: true,
        ranges: {
           'Today': [moment(), moment()],
           'Yesterday': [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
           'Last 7 Days': [moment().subtract(6, 'days'), moment()],
           'Last 30 Days': [moment().subtract(29, 'days'), moment()],
           'This Month': [moment().startOf('month'), moment().endOf('month')],
           'Last Month': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
        }
    }, cb);
    cb(start, end);
});
	var missing = [];
	var clicked = [];
	var errcount = 0;
