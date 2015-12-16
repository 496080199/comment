function videoSelected() {
   var video = document.getElementById('id_video').files[0];
   if (video) {
   var videoSize = 0;
   if (video.size > 1024 * 1024)
       videoSize = (Math.round(video.size * 100 / (1024 * 1024)) / 100).toString() + 'MB';
   else
       videoSize = (Math.round(video.size * 100 / 1024) / 100).toString() + 'KB';

   document.getElementById('videoName').innerHTML = 'videoName: ' + video.name;
   document.getElementById('videoSize').innerHTML = 'videoSize: ' + videoSize;
   document.getElementById('videoType').innerHTML = 'videoType: ' + video.type;
   }
}

function audioSelected() {
   var audio = document.getElementById('id_audio').files[0];
   if (audio) {
   var audioSize = 0;
   if (audio.size > 1024 * 1024)
       audioSize = (Math.round(audio.size * 100 / (1024 * 1024)) / 100).toString() + 'MB';
   else
       audioSize = (Math.round(audio.size * 100 / 1024) / 100).toString() + 'KB';

   document.getElementById('audioName').innerHTML = 'audioName: ' + audio.name;
   document.getElementById('audioSize').innerHTML = 'audioSize: ' + audioSize;
   document.getElementById('audioType').innerHTML = 'audioType: ' + audio.type;
   }
}

function uploadFile() {
		var formobj=document.getElementById('form')
        var fd = new FormData(formobj);
 /*       fd.append("video", document.getElementById('video').files[0]);
        fd.append("audio", document.getElementById('audio').files[0]);
        fd.append("name", document.getElementById('name').value);
        fd.append("desc", document.getElementById('desc').value);
        fd.append("content", document.getElementById('content').value);
        fd.append("image", document.getElementById('image').files[0]);
        */
        var xhr = new XMLHttpRequest();
        xhr.upload.addEventListener("progress", uploadProgress, false);
        xhr.addEventListener("load", uploadComplete, false);
        xhr.addEventListener("error", uploadFailed, false);
        xhr.addEventListener("abort", uploadCanceled, false);
        xhr.open("POST", "to_ask");
        xhr.send(fd);
      }

function uploadProgress(evt) {
	if (evt.lengthComputable) {
		var percentComplete = Math.round(evt.loaded * 100 / evt.total);
 		document.getElementById('progressNumber').innerHTML = percentComplete.toString() + '%';
	}
    else {
          document.getElementById('progressNumber').innerHTML = 'unable to compute';
    }
}

function uploadComplete(evt) {
        /* This event is raised when the server send back a response */
    alert("upload complete");
    window.location.href="/user_login";
}

function uploadFailed(evt) {
    alert("There was an error attempting to upload the file.");
}

function uploadCanceled(evt) {
    alert("The upload has been canceled by the user or the browser dropped the connection.");
}