{% load staticfiles %}
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
