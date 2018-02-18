var form = document.getElementById('photographer_form')
form.onsubmit = function (e) {
  // stop the regular form submission
  e.preventDefault();
    // collect the form data while iterating over the inputs
  var data = {};
  for (var i = 0, ii = form.length; i < ii; ++i) {
    var input = form[i];
    if (input.name == "interests") {
      var input2 = form[i+1];
      var input3 = form[i+2];
    	data[input.name] = [input.value, input2.value, input3.value];
    	i+=2;
    }
    else {
    	data[input.name] = input.value;
    }
  }
  var xhr = new XMLHttpRequest();
  xhr.open(form.method, form.action, true);
  xhr.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
  xhr.setRequestHeader("Access-Control-Allow-Origin", "*");

	//alert(JSON.stringify(data));
 // send the collected data as JSON
  xhr.send(JSON.stringify(data));

  xhr.onloadend = function () {
    // done
  };
};