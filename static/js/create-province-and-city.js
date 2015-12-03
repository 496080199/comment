$(document).on("pageinit", function() {
	// 填充省下拉列表
	var provincesOptionHtml = "";
	var provinces = [];
	for(var el in provinceAndCityArray) {
		provinces.push(provinceAndCityArray[el].name);
		provincesOptionHtml += "<option value=" + el + ">" + provinceAndCityArray[el].name + "</option>";
	}
	$("#selectProvince").append(provincesOptionHtml);
	
	// 填充城市下拉列表
	$("#selectProvince").bind("change", function() {
		var selectedProvince = $("#selectProvince :selected").val();
		if(selectedProvince != -1) {
			var citiesOptionHtml = "";
			var cities = [];
			cities = provinceAndCityArray[selectedProvince].cities;
			for(var elCity in cities) {
				citiesOptionHtml += "<option value=" + cities[elCity] + ">" + cities[elCity] + "</option>";
			}
			// 清空之前的城市列表
			$("#selectCity option[value!=-1]").remove();
			$("#selectCity option[value=-1]").attr("selected", true);
			$("#selectCity").append(citiesOptionHtml);
			$("#selectCity").selectmenu("refresh");
		}
	});
});