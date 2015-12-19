function changeStat(id){
	var val=$("#stat").val();
	var xhr = new XMLHttpRequest();
	xhr.open("GET","/change_app_stat/"+id+"/"+val,true);
	xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
	xhr.send();
};

function changeScore(id){
	var val=$("#score").val();
	var xhr = new XMLHttpRequest();
	xhr.open("GET","/change_com_score/"+id+"/"+val,true);
	xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
	xhr.send();
};