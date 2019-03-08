{% load staticfiles %}
var fieldId=0;
var building=[null,null,null];

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
      innerdiv.setAttribute("id", "extradiv"+insert_at);
      innerdiv.setAttribute("style","display:inline-flex;width: -webkit-fill-available;");
      var innerinput = document.createElement('input');
      innerinput.setAttribute("class", "search");
      innerinput.setAttribute("id", "extrabuild");
      innerinput.setAttribute("placeholder", "Search For Building...");
      innerinput.setAttribute("style","height: fit-content;");
      var removebutt = document.createElement('img');
      removebutt.setAttribute("src", "{% static 'edashboard/images/delete.png' %}");
      removebutt.setAttribute("id", "removebutton");
      removebutt.setAttribute("onClick", "removeBuilding("+insert_at+")");
      removebutt.setAttribute("style", "height: 30px;margin: 5% 0;padding-left: 3%;");
      innerdiv.appendChild(innerinput);
      innerdiv.appendChild(removebutt);
      (document.getElementById("buildingadder")).appendChild(innerdiv);
      fieldId++; // increment fileId to get a unique ID for the new element
      building[insert_at] = 1;
    }
    else{
      alert("You can only add up to 4 buildings!");
    }
}
function removeBuilding(num){
  innerdiv=document.getElementById("extradiv"+num);
  innerdiv.parentNode.removeChild(innerdiv);
  building[num]=null;
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


	function checkFields(){
    var buildingname = document.getElementById('search').value.length;
    var valarr = document.getElementsByClassName('select-selected').innerHTML;
    var buildingsensor = document.getElementById('select-selected-sens').innerHTML;
    var buildingutil = document.getElementById('select-selected-util').innerHTML;
    //If Name not entered
		if(buildingname == 0){
			var flag = 0;
			//checks if in missing array
			for(i=0;i<missing.length;i++){
				if(missing[i] == 'Building Name'){
					flag = 1
					break;
				}
			}
			//if not in array
			if(flag == 0){
				missing[missing.length] = 'Building Name';
			}
			// If there is an Error box, UPDATE <p>
			if(document.getElementById('required-field-error')){
				var str = arrToString(missing);
				var para = document.getElementById('reqfielderror');
				para.textContent = str;
			}
			// If there isn't an error box
			else{
				//Create div
				errcount++;
				var innerdiv = document.createElement('div');
				innerdiv.setAttribute("id", "required-field-error");
				var str = arrToString(missing);
    		innerdiv.innerHTML = "<p id=reqfielderror>" + str + "</p>";
     		(document.getElementById("error-display")).appendChild(innerdiv);
			}
		}
    //Name entered
    else {
      for(i=0;i<missing.length;i++){
				if(missing[i] == 'Building Name'){
					missing[i] = null;
  				var str = arrToString(missing);
  				var para = document.getElementById('reqfielderror');
  				para.textContent = str;
				}
			}
    }
    if(buildingutil == "Select"){
			var flag = 0;
			//checks if in missing array
			for(i=0;i<missing.length;i++){
				if(missing[i] == 'Building Utility'){
					flag = 1
					break;
				}
			}
			//if not in array
			if(flag == 0){
				missing[missing.length] = 'Building Utility';
			}
			// If there is an Error box, UPDATE <p>
			if(document.getElementById('required-field-error')){
				var str = arrToString(missing);
				var para = document.getElementById('reqfielderror');
				para.textContent = str;
			}
			// If there isn't an error box
			else{
				//Create div
				errcount++;
				var innerdiv = document.createElement('div');
				innerdiv.setAttribute("id", "required-field-error");
				var str = arrToString(missing);
    		innerdiv.innerHTML = "<p id=reqfielderror>" + str + "</p>";
     		(document.getElementById("error-display")).appendChild(innerdiv);
			}
		}
    else {
      for(i=0;i<missing.length;i++){
				if(missing[i] == 'Building Utility'){
					missing[i] = null;
  				var str = arrToString(missing);
  				var para = document.getElementById('reqfielderror');
  				para.textContent = str;
				}
			}
    }
    if(buildingsensor == "Select"){
			var flag = 0;
			//checks if in missing array
			for(i=0;i<missing.length;i++){
				if(missing[i] == 'Building Sensor'){
					flag = 1
					break;
				}
			}
			//if not in array
			if(flag == 0){
				missing[missing.length] = 'Building Sensor';
			}
			// If there is an Error box, UPDATE <p>
			if(document.getElementById('required-field-error')){
				var str = arrToString(missing);
				var para = document.getElementById('reqfielderror');
				para.textContent = str;
			}
			// If there isn't an error box
			else{
				//Create div
				errcount++;
				var innerdiv = document.createElement('div');
				innerdiv.setAttribute("id", "required-field-error");
				var str = arrToString(missing);
    		innerdiv.innerHTML = "<p id=reqfielderror>" + str + "</p>";
     		(document.getElementById("error-display")).appendChild(innerdiv);
			}
		}
		// If there is a entered value, remove the value or box
    else {
      for(i=0;i<missing.length;i++){
				if(missing[i] == 'Building Sensor'){
					missing[i] = null;
  				var str = arrToString(missing);
  				var para = document.getElementById('reqfielderror');
  				para.textContent = str;
				}
			}
    }
    //Checks for no errors
    var flag2 = 0
    for(i=0;i<missing.length;i++){
      if(missing[i]!=null){
        flag2=1
      }
    }
    //Removes error box if none
    if(flag2==0){
      var innerdiv = document.getElementById('required-field-error');
				if(innerdiv){
					innerdiv.parentNode.removeChild(innerdiv);
				}
        //ADD CODE HERE TO GENERATE GRAPH
    }
	}
	function arrToString(array){
		var str = "ERROR: You must enter in a value for: ";
		var count = 0;
		var found = 0;
		for(i=0;i<missing.length;i++){
			if(array[i] != null){
				count++;
			}
		}
		for(i = 0; i<missing.length; i++){
			if(array[i] == null){
				continue;
			}
			else if(found==count-2){
				str+= array[i] + " & ";
				found++;
			}
			else if(found==count-1){
				str+= array[i]+".";
				found++;
			}
			else{
			str+= array[i] + ", ";
			found++;
			}
		}
		return str;
	}
