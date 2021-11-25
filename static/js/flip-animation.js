
$(".lend_btn").click(function(event){
    console.log("뒤집기 실행");
    let target = $(this).closest(".item_container-flip");

    console.log(target.css('transform'));
    //만약 뒷면이면 앞으로
    if (target.attr("data-sur") == "back"){
        target.attr("data-sur", "front");
        target.css({'transform':'rotateY(0deg)'})
    } 
    //앞면이면 뒷면으로
    else {
        console.log("뒤집기 실행");
        target.attr("data-sur", "back");
        target.css({'transform':'rotateY(180deg)'})
    }
});