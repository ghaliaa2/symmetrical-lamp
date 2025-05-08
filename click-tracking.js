function trackClick(page) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        console.log("Click data logged successfully");
      }
    };
    xhttp.open("POST", "logClick.php", true); 
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("page=" + page);
  }
  
  document.querySelectorAll("button").forEach(button => {
    button.addEventListener("click", function() {
      var page = this.getAttribute("data-page");
      trackClick(page);
    });
  });