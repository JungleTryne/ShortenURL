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
  if (document.getElementById('alert_url').classList.contains('show')) {
    document.getElementById('alert_url').classList.remove('show')
  }
}

function copyUrl() {
  var copyText = document.getElementById("new_url").innerHTML;
  navigator.clipboard.writeText(copyText).then(function() {
    document.getElementById('copy_link').classList.remove('btn-success');
    document.getElementById('copy_link').innerHTML = 'Скопировано'
  });
}

function sendPostRequest() {
  var url = document.getElementById("UrlInputForm").value;
  var token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
  if(validURL(url)) {
    if (document.getElementById('alert_url').classList.contains('show')) {
      document.getElementById('alert_url').classList.remove('show')
    }
    var xhr = new XMLHttpRequest();
    xhr.open('POST','/generate_code/',false);
    var body = "url=" + encodeURIComponent(url) + "&csrfmiddlewaretoken=" + token;
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.send(body);
    if (xhr.readyState == 4)
      if (xhr.status == 200)
        var json_data = xhr.responseText; 
      else {
        console.log('status is not 200');
        return
      }
    else {
      console.log("readyState is not 4");
      return
    }
    console.log(json_data)
    document.getElementById('show_card').innerHTML = 
        '<div class="card" style="width: 18rem; margin: 0 auto; margin-top: 1rem;">\
        <div class="card-body">\
        <h5 class="card-title">Ваш URL</h5>\
        <p class="card-text" id="new_url">'+json_data+'</p>\
        <button id="copy_link" class="btn btn-success" onclick="copyUrl()">Скопировать</button>\
        </div>\
        </div>'
  }
  else {
    document.getElementById('alert_url').classList.add('show')
    document.getElementById("close_alert").addEventListener("click", closeAlert);
  }
}

document.getElementById("sendUrl").addEventListener("click", sendPostRequest);
