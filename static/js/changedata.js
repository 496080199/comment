function changeStat(id){
	var val=$("#stat").val();
	$.post("/change_app_stat/"+id,{'stat':val},function(ret){
	});
};

function changeScore(id){
	var val=$("#score"+id.toString()).val();
	$.post("/change_com_score/"+id,{'score':val},function(ret){
	});
	var total_fee=$("#total_fee").val();
	var worth=val/10*total_fee;
	if(worth>0){
	document.getElementById("worth"+id.toString()).innerHTML="<label>"+worth+"元</label>";
	}
	
};


		 