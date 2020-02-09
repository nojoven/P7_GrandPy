$("#typearea").keyup(function(e){
    if(e.keyCode == 13)
    {
        var $userBubble = "<div class='d-flex justify-content-end mb-4 ispeakdiv'>"+
								"<div class='msg_cotainer_send mywords'>"
								    + $(this).val() +
								"</div>"+
						 "</div>";
        $('.chatarea').append($userBubble);
        $(this).val("");
        $(".chatarea").scrollTop($('.chatarea').prop("scrollHeight"));
        return;

    }

});


$("#typearea").keyup(function(e){
    if(e.keyCode == 8)
    {
        var $botBubble = "<div class='d-flex justify-content-start mb-4 papyspeaksdiv'>"+
								"<div class='msg_cotainer botwords'>"
								    + $(this).val() +
								"</div>"+
						 "</div>";
        $('.chatarea').append($botBubble);
        $(this).val("");
        $(".chatarea").scrollTop($('.chatarea').prop("scrollHeight"));
        return;

    }

});
