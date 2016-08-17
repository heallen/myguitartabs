$(document).ready(function(){
	$('#songs h3').click(function(){
		$('#songs ul').slideToggle(300);
	});
	$('#artists h3').click(function(){
		$('#artists ul').slideToggle(300);
	});
	$('#categories h3').click(function(){
		$('#categories ul').slideToggle(300);
	});

	$('#songs h3, #artists h3, #categories h3').hover(
		function(){
			$(this).css("color", "#CEECF5");
		},
		function(){
			$(this).css("color", "#E6E6E6");
		}
	);

});