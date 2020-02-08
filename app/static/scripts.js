$("#typearea").keyup(function(e){
    if(e.keyCode == 13)
    {
        var $userBubble = $('.ispeakdiv').clone().appendTo(".chatarea");

        $(this).val("");
        return;

    }

});
$( "#button" ).click(function() {
  $(".asked").append($("#typearea").val());
  $("#typearea").val("")
});

