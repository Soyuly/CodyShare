//유효성 검사 로직
const $inputEelement = $("input, select");  //모든 input 요소를 검사 할 것.
$(".form__submit").attr("disabled", true);   //일단 submit disabled

//input 에서 벗어날 때마다 검사
$("input, select").change(function(){
    var re_start=document.getElementsByName('start').value;
    var re_end=document.getElementsByName('end').value;
    re_start = re_start.split('-');
    console.log(re_start);

    if(canSignup == false)
        $(".form__submit").attr("disabled", true);
    else{
        $(".form__submit").attr("disabled", false);
    }
});
