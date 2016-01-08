function changeStat(id){
	var val=$("#stat"+id.toString()).val();
	$.post("/change_app_stat/"+id,{'stat':val},function(ret){
	});
};

function changeScore(id){
	var val=$("#score"+id.toString()).val();
	$.post("/change_com_score/"+id,{'score':val},function(ret){
	});
	var price=$("#price").text();
	//alert(price)
	var worth=val/10*price;
	if(worth>0){
	document.getElementById("worth"+id.toString()).innerHTML="<label>付费："+worth.toFixed(2)+"元</label>";
	}
	
};


		 