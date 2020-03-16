$("#typearea").keyup(function(e){
    if(e.keyCode == 13) // If the user types ENTER
    {// We display a user chat bubble with the input text
        var $userBubble = "<div class='d-flex justify-content-end mb-4 ispeakdiv'>"+
								"<div class='msg_cotainer_send mywords'>"
								    + $(this).val() +
								"</div>"+
						 "</div>";
        $('.chatarea').append($userBubble);
        $(".chatarea").scrollTop($('.chatarea').prop("scrollHeight")); //Always scroll down
        $.getJSON('/input_process', //communicate with the backend
            {
                "input_text": $(this).val()
            },
               function(data) {
              console.log(data);

              if(!data["result"].includes("NO AVAILABLE IMAGE")) { //if there is a map (sometimes there will be no map to display)
                var byteCharacters = data["result"];
                //if there is a map we have to encode it
                var byteNumbers = new Array(byteCharacters.length);
                for (var i = 0; i < byteCharacters.length; i++) {
                  byteNumbers[i] = byteCharacters.charCodeAt(i);
                }
                //so we can have a .png file
                var byteArray = new Uint8Array(byteNumbers);
                var blob = new Blob([ byteArray ], {
                   type : "image/png"
                });
                console.log(blob);
                var imageUrl = URL.createObjectURL(blob);
                console.log(imageUrl);
                var image = new Image();
                //we can define the seize
                image.src = byteCharacters;
                image.width = 300;
                image.height=150;
                image.alt="J'ai pas compris, Fiston...";
                //then we display it
                $('.chatarea').append(image);
                // With a space to separate two bubbles
                $('.chatarea').append("<br><br>");

              }
              if(data["wiki"] != null) { // if there are wikipedia data returnd by flask
                description = data["wiki"];
                botMessage(description); //We display the text
              }
            });
        $(this).val("");
    }

});

function botMessage(message){ //this function displays the bot's answer
        var $botBubble = "<div class='d-flex justify-content-start mb-4 papyspeaksdiv'>"+
								"<div class='msg_cotainer botwords'>"
								    + message +
								"</div>"+
						 "</div>";
        $('.chatarea').append($botBubble);
        $(this).val("");
        $(".chatarea").scrollTop($('.chatarea').prop("scrollHeight"));

}


