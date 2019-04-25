{% load staticfiles %}
var input2 = document.getElementById("sensorsearchexpcompsearch");
var input3 = "None"
var input4 = "None"
var input5 = "None"

function checkSensorValues(){
  if(document.getElementById('extrasdiv2') != null){
    input3 = document.getElementById('extrasdiv2').getElementsByTagName('input')[0];
  }
  else{
    input3 = "None"
  }
  if(document.getElementById('extrasdiv2') != null){
    input4 = document.getElementById('extrasdiv2').getElementsByTagName('input')[0];
  }
  else{
    input4 = "None"
  }
  if(document.getElementById('extrasdiv2') != null){
    input5 = document.getElementById('extrasdiv2').getElementsByTagName('input')[0];
  }
  else{
    input5 = "None"
  }
}
var buildings = {{ buildlist|safe }} ;
var results;

// functions
function autocompletee(val) {
  var build_return = [];
  for (i = 0; i < buildings.length; i++) {
    if(buildings[i].includes(val)){
      build_return.push(buildings[i]);
    }}
  return build_return;
}
// events
input2.onkeyup = function(e){
  input_val = this.value; // updates the variable on each ocurrence
  if (input_val.length > 0) {
    var build_to_show = [];
    autocomplete_results = document.getElementById("autocomplete-results3");
    autocomplete_results.innerHTML = '';
    build_to_show = autocompletee(input_val);
    if(build_to_show.length != 0){
      for (i = 0; i < build_to_show.length; i++) {
        autocomplete_results.innerHTML += '<li class=\'searchsug\'id="list9'+i+'" onclick="FillInput2(\'list9'+i+'\')">' + build_to_show[i] + '</li>';
      }
      autocomplete_results.style.display = 'block';
      autocomplete_results.style.backgroundColor = '#e3e3e3';
    }
    else{
      build_to_show = [];
      autocomplete_results.innerHTML = '';
      autocomplete_results.style.backgroundColor = 'white';
    }
  }

  else {
    build_to_show = [];
    autocomplete_results.innerHTML = '';
    autocomplete_results.style.backgroundColor = 'white';
  }
}
function FillInput2(listid){
  listName = document.getElementById(listid).innerHTML;
  document.getElementById("sensorsearchexpcompsearch").value = listName;
  document.getElementById("autocomplete-results3").innerHTML = ''
  document.getElementById("autocomplete-results3").style.backgroundColor = 'white';
  return 0;
}

// functions
function autocompletee(val) {
  var build_return = [];
  for (i = 0; i < buildings.length; i++) {
    if(buildings[i].includes(val)){
      build_return.push(buildings[i]);
    }}
  return build_return;
}
// events
input3.onkeyup = function(e){
  input_val = this.value; // updates the variable on each ocurrence
  if (input_val.length > 0) {
    var build_to_show = [];
    autocomplete_results = document.getElementById("autocomplete-results3");
    autocomplete_results.innerHTML = '';
    build_to_show = autocompletee(input_val);
    if(build_to_show.length != 0){
      for (i = 0; i < build_to_show.length; i++) {
        autocomplete_results.innerHTML += '<li class=\'searchsug\'id="list9'+i+'" onclick="FillInput3(\'list9'+i+'\')">' + build_to_show[i] + '</li>';
      }
      autocomplete_results.style.display = 'block';
      autocomplete_results.style.backgroundColor = '#e3e3e3';
    }
    else{
      build_to_show = [];
      autocomplete_results.innerHTML = '';
      autocomplete_results.style.backgroundColor = 'white';
    }
  }

  else {
    build_to_show = [];
    autocomplete_results.innerHTML = '';
    autocomplete_results.style.backgroundColor = 'white';
  }
}
function FillInput3(listid){
  listName = document.getElementById(listid).innerHTML;
  document.getElementById("sensorsearchexpcompsearch").value = listName;
  document.getElementById("autocomplete-results3").innerHTML = ''
  document.getElementById("autocomplete-results3").style.backgroundColor = 'white';
  return 0;
}

// functions
function autocompletee(val) {
  var build_return = [];
  for (i = 0; i < buildings.length; i++) {
    if(buildings[i].includes(val)){
      build_return.push(buildings[i]);
    }}
  return build_return;
}
// events
input4.onkeyup = function(e){
  input_val = this.value; // updates the variable on each ocurrence
  if (input_val.length > 0) {
    var build_to_show = [];
    autocomplete_results = document.getElementById("autocomplete-results3");
    autocomplete_results.innerHTML = '';
    build_to_show = autocompletee(input_val);
    if(build_to_show.length != 0){
      for (i = 0; i < build_to_show.length; i++) {
        autocomplete_results.innerHTML += '<li class=\'searchsug\'id="list9'+i+'" onclick="FillInput4(\'list9'+i+'\')">' + build_to_show[i] + '</li>';
      }
      autocomplete_results.style.display = 'block';
      autocomplete_results.style.backgroundColor = '#e3e3e3';
    }
    else{
      build_to_show = [];
      autocomplete_results.innerHTML = '';
      autocomplete_results.style.backgroundColor = 'white';
    }
  }

  else {
    build_to_show = [];
    autocomplete_results.innerHTML = '';
    autocomplete_results.style.backgroundColor = 'white';
  }
}
function FillInput4(listid){
  listName = document.getElementById(listid).innerHTML;
  document.getElementById("sensorsearchexpcompsearch").value = listName;
  document.getElementById("autocomplete-results3").innerHTML = ''
  document.getElementById("autocomplete-results3").style.backgroundColor = 'white';
  return 0;
}

// functions
function autocompletee(val) {
  var build_return = [];
  for (i = 0; i < buildings.length; i++) {
    if(buildings[i].includes(val)){
      build_return.push(buildings[i]);
    }}
  return build_return;
}
// events
input5.onkeyup = function(e){
  input_val = this.value; // updates the variable on each ocurrence
  if (input_val.length > 0) {
    var build_to_show = [];
    autocomplete_results = document.getElementById("autocomplete-results3");
    autocomplete_results.innerHTML = '';
    build_to_show = autocompletee(input_val);
    if(build_to_show.length != 0){
      for (i = 0; i < build_to_show.length; i++) {
        autocomplete_results.innerHTML += '<li class=\'searchsug\'id="list9'+i+'" onclick="FillInput5(\'list9'+i+'\')">' + build_to_show[i] + '</li>';
      }
      autocomplete_results.style.display = 'block';
      autocomplete_results.style.backgroundColor = '#e3e3e3';
    }
    else{
      build_to_show = [];
      autocomplete_results.innerHTML = '';
      autocomplete_results.style.backgroundColor = 'white';
    }
  }

  else {
    build_to_show = [];
    autocomplete_results.innerHTML = '';
    autocomplete_results.style.backgroundColor = 'white';
  }
}
function FillInput5(listid){
  listName = document.getElementById(listid).innerHTML;
  document.getElementById("sensorsearchexpcompsearch").value = listName;
  document.getElementById("autocomplete-results3").innerHTML = ''
  document.getElementById("autocomplete-results3").style.backgroundColor = 'white';
  return 0;
}
