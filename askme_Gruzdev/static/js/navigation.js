   function myFunction() {
    
  document.getElementById("myDropdown").classList.toggle("show");
  document.getElementByClassName("dropdown-content").style.display="";
  document.getElementById("myInput").value="";
  var div = document.getElementById("myDropdown");
  a = div.getElementsByTagName("a");
 for (i = 0; i < a.length; i++) {
    a[i].style.display="";
  }

  
}

function filterFunction() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  div = document.getElementById("myDropdown");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
      if (a[i].innerHTML.toUpperCase().indexOf(filter) > -1) {
          a[i].style.display = "";
      } else {
          a[i].style.display = "none";
      }
  }
}
