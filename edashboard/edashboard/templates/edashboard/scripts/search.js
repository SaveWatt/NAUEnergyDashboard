{% load staticfiles %}
var input2 = document.getElementById("buildingsearchexpcompsearch");
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
    autocomplete_results = document.getElementById("autocomplete-results2");
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
  document.getElementById("autocomplete-results2").innerHTML = ''
  document.getElementById("autocomplete-results2").style.backgroundColor = 'white';
  return 0;
}
