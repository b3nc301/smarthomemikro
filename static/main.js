$(":checkbox").click(function () {
	var data = $("#futauto").is(':checked')+ "," + $("#futon").is(':checked') + "," + $("#riaszt").is(':checked') +","+$("#lampa1").is(':checked')+","+$("#lampa2").is(':checked')+","+$("#temp").val();
	if($("#futauto").is(':checked')) {$("#futon").attr("disabled",true);}
	else {$("#futon").removeAttr("disabled");}
	$.post("",data,);
}
);
$("#temp").change(
	function () {
	var data = $("#futauto").is(':checked')+ "," + $("#futon").is(':checked') + "," + $("#riaszt").is(':checked') +","+$("#lampa1").is(':checked')+","+$("#lampa2").is(':checked')+","+$("#temp").val();
	if($("#futauto").is(':checked')) {$("#futon").attr("disabled",true);}
	else {$("#futon").removeAttr("disabled");}
	$.post("",data,);
});