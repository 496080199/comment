jQuery.validator.addMethod("checkVideo", function(value, element) {
	var video = document.getElementById('id_video').files[0];
	if (video!=null){
		var type=video.type
		if(type == "video/mp4"){
			return true
		}else{
			return false
		}
	}
	return true
}, "请上传mp4视频文件");
jQuery.validator.addMethod("checkAudio", function(value, element) {
    var audio = document.getElementById('id_audio').files[0];
    if (audio!=null){
    
		var type=audio.type
		if(type == "audio/mp3"){
			return true
		}else if(type == "audio/wav"){
			return true
		}else{
			return false
		}
	}
	return true
}, "请上传mp3或wav音频文件");
jQuery.extend(jQuery.validator.messages, {
    required: "必填字段",
	remote: "请修正该字段",
	email: "请输入正确格式的电子邮件",
	url: "请输入合法的网址",
	date: "请输入合法的日期",
	dateISO: "请输入合法的日期 (ISO).",
	number: "请输入合法的数字",
	digits: "只能输入整数",
	creditcard: "请输入合法的信用卡号",
	equalTo: "请再次输入相同的值",
	accept: "请输入拥有合法后缀名的字符串",
	maxlength: jQuery.validator.format("请输入一个 长度最多是 {0} 的字符串"),
	minlength: jQuery.validator.format("请输入一个 长度最少是 {0} 的字符串"),
	rangelength: jQuery.validator.format("请输入 一个长度介于 {0} 和 {1} 之间的字符串"),
	range: jQuery.validator.format("请输入一个介于 {0} 和 {1} 之间的值"),
	max: jQuery.validator.format("请输入一个最大为{0} 的值"),
	min: jQuery.validator.format("请输入一个最小为{0} 的值")
});

$().ready(function() {
 $("#form").validate({
        rules: {
   content: "required",
   video: {
   checkVideo: true,
   },
   audio: {
   checkAudio: true,
   },
  }
    });
});
