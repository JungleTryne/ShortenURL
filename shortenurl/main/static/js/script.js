//checking the URL template
function validURL(str) {
    try {
      new URL(str);
      return true;
    } catch (_) {
      return false;
    }
  }

//closing the alert of wrong URL template
function closeAlert() {
  if (document.getElementById('alert_url').classList.contains('show'))
    document.getElementById('alert_url').classList.remove('show');
}

//button for copying shortened URL
function copyUrl() {
  var copyText = document.getElementById('new_url');
  copyText.select();
  document.execCommand("copy");
}

//sending Post Request to the server for shortening the URL
function sendPostRequest() {
  var url = document.getElementById('UrlInputForm').value;
  var token = document.getElementsByName('csrfmiddlewaretoken')[0].value;

  if(validURL(url)) {
    if (document.getElementById('alert_url').classList.contains('show'))
      document.getElementById('alert_url').classList.remove('show');

    var xhr = new XMLHttpRequest();
    xhr.open('POST','/generate_code/',false);
    var body = 'url=' + encodeURIComponent(url) + '&csrfmiddlewaretoken=' + token;
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
      console.log('readyState is not 4');
      return
    }
    document.getElementById('show_card').innerHTML =
        '<div class="card" style="width: 30rem; margin: 0 auto; margin-top: 1rem;;">\
        <div class="card-body">\
        <h5 class="card-title">Ваш URL</h5>\
        <input class="input-group-text mb-4" value="'+json_data+'" class="card-text" id="new_url" style="margin: 0 auto; width: 25rem" readonly>\
        <button id="copy_link" class="btn btn-success" onclick="copyUrl()">Скопировать</button>\
        </div>\
        </div>'
  }
  else {
    document.getElementById('alert_url').classList.add('show')
    document.getElementById('close_alert').addEventListener('click', closeAlert);
  }
}

//entry point lol
document.getElementById('sendUrl').addEventListener('click', sendPostRequest);
