$(document).ready(function(){
	
	$("input").click(function(){
		if(!this.checked)
			$(this).prop('checked',true);
		var a=$(this).next();
		var b="<strike>"+a.text()+"</strike>";
		a.html(b);
		var entryid;
		entryid=$(this).attr("e_id");	
		console.log(entryid);
		$.get('/calendar/completed_entry/',{entry_id:entryid}, function(data){
			console.log("got here");
		});
	});	
		
});
