$("#typearea").keyup(function(e){
    if(e.keyCode == 13)
    {
        var $userBubble = "<div class='d-flex justify-content-end mb-4 ispeakdiv'>"+
								"<div class='msg_cotainer_send mywords'>"
								    + $(this).val() +
								"</div>"+
						 "</div>";
        $('.chatarea').append($userBubble);
        $(".chatarea").scrollTop($('.chatarea').prop("scrollHeight"));
        $.getJSON('/input_process',
            {
                "input_text": $(this).val()
            },
               function(data) {
              console.log(data);
              if(data["result"] != null) {
                var byteCharacters = data["result"];
                var byteNumbers = new Array(byteCharacters.length);
                for (var i = 0; i < byteCharacters.length; i++) {
                  byteNumbers[i] = byteCharacters.charCodeAt(i);
                }

                var byteArray = new Uint8Array(byteNumbers);
                var blob = new Blob([ byteArray ], {
                   type : "image/png"
                });
                console.log(blob);
                var imageUrl = URL.createObjectURL(blob);
                console.log(imageUrl);
                var image = new Image();

                image.src = byteCharacters;
                image.width = 300;
                image.height=150;
                image.alt="here should be some image";

                 $('.chatarea').append(image);
              }
            });
        $(this).val("");
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


