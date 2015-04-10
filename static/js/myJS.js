//for sending a friend request
function addFriend (argument) {
	//alert(argument);

	//calling the ajax function to send the request
	$("#btn-"+argument).load("/amigo/sendRequest/"+argument);
	$('#btn-'+argument).removeClass("btn-primary");
	$('#btn-'+argument).addClass("btn-warning");

}
//for accepting a friend request
function acceptRequest (argument) {
	$("#btn-"+argument).load("/amigo/acceptRequest/"+argument);
	$('#btn-'+argument).removeClass("btn-info");
	$('#btn-'+argument).addClass("btn-success");
}

//for liking a status
function statusLike (argument) {
	alert(argument + " liked!!");
}

//for disliking a status

function statusDisLike (argument) {
	alert(argument + " disliked!!");
}