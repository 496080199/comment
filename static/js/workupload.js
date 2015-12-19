function videoSelected() {
   var video = document.getElementById('id_video').files[0];
   if (video) {
   var videoSize = 0;
   if (video.size > 1024 * 1024)
       videoSize = (Math.round(video.size * 100 / (1024 * 1024)) / 100).toString() + 'MB';
   else
       videoSize = (Math.round(video.size * 100 / 1024) / 100).toString() + 'KB';

   document.getElementById('videoName').innerHTML = '视频名称: ' + video.name;
   document.getElementById('videoSize').innerHTML = '视频大小: ' + videoSize;
   document.getElementById('videoType').innerHTML = '视频类型: ' + video.type;
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

   document.getElementById('audioName').innerHTML = '音频名称: ' + audio.name;
   document.getElementById('audioSize').innerHTML = '音频大小: ' + audioSize;
   document.getElementById('audioType').innerHTML = '音频类型: ' + audio.type;
   }
}

function uploadFile() {
		var formobj=document.getElementById('form')
        var fd = new FormData(formobj);
        var xhr = new XMLHttpRequest();
        xhr.upload.addEventListener("progress", uploadProgress, false);
        xhr.addEventListener("load", uploadComplete, false);
        xhr.addEventListener("error", uploadFailed, false);
        xhr.addEventListener("abort", uploadCanceled, false);
        xhr.open("POST", "/to_ask");
        xhr.send(fd);
      }

function uploadEditFile() {
		var formobj=document.getElementById('form');
		var id=document.getElementById('id');
        var fd = new FormData(formobj);
        var xhr = new XMLHttpRequest();
        xhr.upload.addEventListener("progress", uploadProgress, false);
        xhr.addEventListener("load", uploadEditComplete, false);
        xhr.addEventListener("error", uploadEditFailed, false);
        xhr.addEventListener("abort", uploadCanceled, false);
        xhr.open("POST", "/edit_ask/"+parseInt(id.innerHTML));
        xhr.send(fd);
      }
      
function uploadCom(id) {
		var formobj=document.getElementById('form')
		var id=document.getElementById('id');
        var fd = new FormData(formobj);
        var xhr = new XMLHttpRequest();
        xhr.upload.addEventListener("progress", uploadProgress, false);
        xhr.addEventListener("load", uploadComComplete, false);
        xhr.addEventListener("error", uploadComFailed, false);
        xhr.addEventListener("abort", uploadCanceled, false);
        xhr.open("POST", "/to_com/"+parseInt(id.innerHTML),true);
        xhr.send(fd);
      }
      
 function uploadComEdit() {
		var formobj=document.getElementById('form'); 
		var id=document.getElementById('id');
        var fd = new FormData(formobj);
        var xhr = new XMLHttpRequest();
       	xhr.upload.addEventListener("progress", uploadProgress, false);
       	xhr.addEventListener("load", uploadComComplete, false);
       	xhr.addEventListener("error", uploadComFailed, false);
        xhr.addEventListener("abort", uploadCanceled, false);
        xhr.open("POST", "/edit_com/"+parseInt(id.innerHTML),true);
        xhr.send(fd);
      }

function uploadProgress(evt) {
	if (evt.lengthComputable) {
		var percentComplete = Math.round(evt.loaded * 100 / evt.total);
		document.getElementById('bar').style.width = percentComplete + '%';
 		//document.getElementById('progressNumber').innerHTML = percentComplete.toString() + '%';
	}
    else {
       document.getElementById('progressNumber').innerHTML = '无法计算';
    }
}

function uploadComplete(evt) {
        /* This event is raised when the server send back a response */
    alert("提交成功");
    window.location.href="/user_login";
}
function uploadEditComplete(evt) {
        /* This event is raised when the server send back a response */
     alert("提交成功");
     var id=document.getElementById('id')
	 window.location.href="/show_ask/"+parseInt(id.innerHTML);
}
function uploadComComplete(evt) {
        /* This event is raised when the server send back a response */
    alert("提交成功");
    var id=document.getElementById('id')
    window.location.href="/show_answer/"+parseInt(id.innerHTML);
}

function uploadFailed(evt) {
    alert("提交失败.");

}

function uploadEditFailed(evt) {
    alert("提交失败.");

}
function uploadComFailed(evt) {
    alert("提交失败.");
    var id=document.getElementById('id');
	 window.location.href="/show_answer/"+parseInt(id.innerHTML);
}

function uploadCanceled(evt) {
    alert("用户已取消.");
}
