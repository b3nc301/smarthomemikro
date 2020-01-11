$(":checkbox").click(function() {
	var data = $("#futes").is(':checked') + ","+ $("#riasztas").is(':checked') +","+$("#lampa1").is(':checked')+","+$("#lampa2").is(':checked')
    $.ajax({
        url: '',
        type: 'POST',
        data:data,
        success: function(msg) {
            alert('Email Sent');
        }               
    });
	/*$.post("",
  {
			futes:$("#futes").is(':checked'),
			riasztas:$("#riasztas").is(':checked'),
            lampa1:$("#lampa1").is(':checked'),
			lampa2:$("#lampa2").is(':checked'),
  },
  );*/
});
