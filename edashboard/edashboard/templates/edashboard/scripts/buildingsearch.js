{% load staticfiles %}
var input2 = document.getElementById('buildingadder').getElementsByTagName('input')[0];
console.log(input2);
var input3 = "None"
var input4 = "None"
var input5 = "None"
var buildings = {{ buildlist|safe }} ;
var results;

function checkBuildingValues(){
  if(document.getElementById('extrabdiv0') != null){
    input3 = document.getElementById('extrabdiv0').getElementsByTagName('input')[0];
  }
  else{
    input3 = "None"
  }
  if(document.getElementById('extrabdiv1') != null){
    input4 = document.getElementById('extrabdiv1').getElementsByTagName('input')[0];
  }
  else{
    input4 = "None"
  }
  if(document.getElementById('extrabdiv2') != null){
    input5 = document.getElementById('extrabdiv2').getElementsByTagName('input')[0];
  }
  else{
    input5 = "None"
  }
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
input2.onkeyup = function(e){
  input_val = this.value; // updates the variable on each ocurrence
  if (input_val.length > 0) {
    var build_to_show = [];
    autocomplete_results = document.getElementById("autocomplete-results10");
    autocomplete_results.innerHTML = '';
    build_to_show = autocompletee(input_val);
    if(build_to_show.length != 0){

      for (i = 0; i < build_to_show.length; i++) {
        autocomplete_results.innerHTML += '<li class=\'searchsug\'id="list'+i+'" onclick="FillInput(\'list'+i+'\')">' + build_to_show[i] + '</li>';
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
function FillInput(listid){
  listName = document.getElementById(listid).innerHTML;
  document.getElementById("buildingsearchexpcompsearch").value = listName;
  document.getElementById("autocomplete-results10").innerHTML = ''
  document.getElementById("autocomplete-results10").style.backgroundColor = 'white';
  return 0;
}

// functions
// events
input3.onkeyup = function(e){
  input_val = this.value; // updates the variable on each ocurrence
  if (input_val.length > 0) {
    var build_to_show = [];
    autocomplete_results = document.getElementById("autocomplete-results0");
    autocomplete_results.innerHTML = '';
    build_to_show = autocompletee(input_val);
    if(build_to_show.length != 0){

      for (i = 0; i < build_to_show.length; i++) {
        autocomplete_results.innerHTML += '<li class=\'searchsug\'id="list'+i+'" onclick="FillInput0(\'list'+i+'\')">' + build_to_show[i] + '</li>';
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
function FillInput0(listid){
  listName = document.getElementById(listid).innerHTML;
  document.getElementById("buildingsearchexpcompsearch").value = listName;
  document.getElementById("autocomplete-results0").innerHTML = ''
  document.getElementById("autocomplete-results0").style.backgroundColor = 'white';
  return 0;
}

// functions
// events
input4.onkeyup = function(e){
  input_val = this.value; // updates the variable on each ocurrence
  if (input_val.length > 0) {
    var build_to_show = [];
    autocomplete_results = document.getElementById("autocomplete-results1");
    autocomplete_results.innerHTML = '';
    build_to_show = autocompletee(input_val);
    if(build_to_show.length != 0){

      for (i = 0; i < build_to_show.length; i++) {
        autocomplete_results.innerHTML += '<li class=\'searchsug\'id="list'+i+'" onclick="FillInput7(\'list'+i+'\')">' + build_to_show[i] + '</li>';
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
function FillInput7(listid){
  listName = document.getElementById(listid).innerHTML;
  document.getElementById("buildingsearchexpcompsearch").value = listName;
  document.getElementById("autocomplete-results1").innerHTML = ''
  document.getElementById("autocomplete-results1").style.backgroundColor = 'white';
  return 0;
}

// functions
// events
input5.onkeyup = function(e){
  input_val = this.value; // updates the variable on each ocurrence
  if (input_val.length > 0) {
    var build_to_show = [];
    autocomplete_results = document.getElementById("autocomplete-results2");
    autocomplete_results.innerHTML = '';
    build_to_show = autocompletee(input_val);
    if(build_to_show.length != 0){

      for (i = 0; i < build_to_show.length; i++) {
        autocomplete_results.innerHTML += '<li class=\'searchsug\'id="list'+i+'" onclick="FillInput8(\'list'+i+'\')">' + build_to_show[i] + '</li>';
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
function FillInput(listid){
  listName = document.getElementById(listid).innerHTML;
  document.getElementById("buildingsearchexpcompsearch").value = listName;
  document.getElementById("autocomplete-results2").innerHTML = ''
  document.getElementById("autocomplete-results2").style.backgroundColor = 'white';
  return 0;
}
