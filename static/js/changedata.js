function changeStat(id){
	var val=$("#stat").val();
	$.post("/change_app_stat/"+id,{'stat':val},function(ret){
	});
};

function changeScore(id){
	var val=$("#score").val();
	$.post("/change_com_score/"+id,{'score':val},function(ret){
	});
};


		 