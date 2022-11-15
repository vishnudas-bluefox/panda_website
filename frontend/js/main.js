function data() {

  const url = document.getElementsByClassName("url_holder");
  console.log(url)
  var url = "http://localhost:8000/twitter/fetch/";
  var params = "url=http://youtube.com/gogle/fgdsa55ad";
  var http = new XMLHttpRequest();

  http.open("GET", url+"?"+params, true);
  http.onreadystatechange = function()
  {
    if(http.readyState == 4 && http.status == 200) {
        alert(http.responseText);
          }
    }
  http.send(null);

}
