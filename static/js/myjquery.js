$(document).ready(function(){
	
	$("input").click(function(){
		if(!this.checked)
			$(this).prop('checked',true);
		var a=$(this).next();
		var b="<strike>"+a.text()+"</strike>";
		a.html(b);
		var entryid;
		entryid=$(this).attr("e_id");	
		$.get('/calendar/completed_entry/',{entry_id:entryid}, function(data){
			console.log("got here");
		});
	});
	$("font").click(function(){
		console.log("pressed me");
		var answer=confirm("Are you sure want to delete this entry?");
		entryid=$(this).attr("e_id");
		console.log(entryid);
		if(answer){
			$.get('/calendar/delete_entry/',{entry_id:entryid},function(data){
				console.log("deleting");
			});
			$(this).prev().hide();
			$(this).hide();
			$(this).next().slideUp("fast");	
		}	
		else{

		}
	});	
});
