function validURL(str) {
    var pattern = new RegExp('^(https?:\\/\\/)?'+ // protocol
      '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|'+ // domain name
      '((\\d{1,3}\\.){3}\\d{1,3}))'+ // OR ip (v4) address
      '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ // port and path
      '(\\?[;&a-z\\d%_.~+=-]*)?'+ // query string
      '(\\#[-a-z\\d_]*)?$','i'); // fragment locator
    return !!pattern.test(str);
  }

function closeAlert() {
  console.log("closing...");
  if (document.getElementById('alert_url').classList.contains('show')) {
    document.getElementById('alert_url').classList.remove('show')
  }
}

function sendPostRequest() {
  var url = document.getElementById("UrlInputForm").value;
  if(validURL(url)) {
      console.log("url is valid");
      if (document.getElementById('alert_url').classList.contains('show')) {
        document.getElementById('alert_url').classList.remove('show')
      }
  }
  else {
    document.getElementById('alert_url').classList.add('show')
    document.getElementById("close_alert").addEventListener("click", closeAlert);
  }
}

document.getElementById("sendUrl").addEventListener("click", sendPostRequest);
