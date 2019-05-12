{% load staticfiles %}
var input2 = document.getElementById('buildingadder').getElementsByTagName('input')[0];
var input3 = "None"
var input4 = "None"
var input5 = "None"
var buildings = {{ buildlist|safe }} ;
var results;

function checkBuildingValues(){
  if(document.getElementById('extrabdiv0') != null){
    input3 = document.getElementById('extrabdiv0').getElementsByTagName('input')[0];
    input3.setAttribute("onkeyup", "input3KeyUp(event)");
  }
  else{
    input3 = "None"
  }
  if(document.getElementById('extrabdiv1') != null){
    input4 = document.getElementById('extrabdiv1').getElementsByTagName('input')[0];
    input4.setAttribute("onkeyup", "input4KeyUp(event)");
  }
  else{
    input4 = "None"
  }
  if(document.getElementById('extrabdiv2') != null){
    input5 = document.getElementById('extrabdiv2').getElementsByTagName('input')[0];
    input5.setAttribute("onkeyup", "input5KeyUp(event)");
  }
  else{
    input5 = "None"
  }
  if(input3 == "None" && input4 == "None" && input5 == "None"){
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
        autocomplete_results.innerHTML += '<li class=\'searchsug\'id="list2'+i+'" onclick="FillInput(\'list2'+i+'\')">' + build_to_show[i] + '</li>';
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
  var listName = document.getElementById(listid).innerHTML;
  document.getElementById('buildingadder').getElementsByTagName('input')[0].value = listName;
  document.getElementById("autocomplete-results10").innerHTML = ''
  document.getElementById("autocomplete-results10").style.backgroundColor = 'white';
  return 0;
}

// functions
// events
$('#buildyourform').on('keyup', '#field_2', function(){
    $('#target2').html($(this).val());
});
function input3KeyUp(e){
  input_val = input3.value; // updates the variable on each ocurrence
  if (input_val.length > 0) {
    var build_to_show = [];
    autocomplete_results = document.getElementById("autocomplete-results0");
    autocomplete_results.innerHTML = '';
    build_to_show = autocompletee(input_val);
    if(build_to_show.length != 0){

      for (i = 0; i < build_to_show.length; i++) {
        autocomplete_results.innerHTML += '<li class=\'searchsug\'id="list3'+i+'" onclick="FillInput0(\'list3'+i+'\')">' + build_to_show[i] + '</li>';
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
  document.getElementById('extrabdiv0').getElementsByTagName('input')[0].value = listName;
  document.getElementById("autocomplete-results0").innerHTML = ''
  document.getElementById("autocomplete-results0").style.backgroundColor = 'white';
  return 0;
}

// functions
// events
function input4KeyUp(e){
  input_val = input4.value; // updates the variable on each ocurrence
  if (input_val.length > 0) {
    var build_to_show = [];
    autocomplete_results = document.getElementById("autocomplete-results1");
    autocomplete_results.innerHTML = '';
    build_to_show = autocompletee(input_val);
    if(build_to_show.length != 0){

      for (i = 0; i < build_to_show.length; i++) {
        autocomplete_results.innerHTML += '<li class=\'searchsug\'id="list4'+i+'" onclick="FillInput7(\'list4'+i+'\')">' + build_to_show[i] + '</li>';
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
  document.getElementById('extrabdiv1').getElementsByTagName('input')[0].value = listName;
  document.getElementById("autocomplete-results1").innerHTML = ''
  document.getElementById("autocomplete-results1").style.backgroundColor = 'white';
  return 0;
}

// functions
// events
function input5KeyUp(e){
  input_val = input5.value; // updates the variable on each ocurrence
  if (input_val.length > 0) {
    var build_to_show = [];
    autocomplete_results = document.getElementById("autocomplete-results2");
    autocomplete_results.innerHTML = '';
    build_to_show = autocompletee(input_val);
    if(build_to_show.length != 0){

      for (i = 0; i < build_to_show.length; i++) {
        autocomplete_results.innerHTML += '<li class=\'searchsug\'id="list5'+i+'" onclick="FillInput8(\'list5'+i+'\')">' + build_to_show[i] + '</li>';
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
function FillInput8(listid){
  listName = document.getElementById(listid).innerHTML;
  document.getElementById('extrabdiv2').getElementsByTagName('input')[0].value = listName;
  document.getElementById("autocomplete-results2").innerHTML = ''
  document.getElementById("autocomplete-results2").style.backgroundColor = 'white';
  return 0;
}
