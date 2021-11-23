//유효성 검사 로직
const $inputEelement = $("input, select");  //모든 input 요소를 검사 할 것.
$(".form__submit").attr("disabled", true);   //일단 submit disabled

//input 에서 벗어날 때마다 검사
$("input, select").focusout(function(){
    canSignup = true;
    $inputEelement.each(function(index, item){
        if(item.value){
        }else {
            canSignup = false;
        }
    });
    console.log(canSignup);
    if(canSignup == false)
        $(".form__submit").attr("disabled", true);
    else{
        $(".form__submit").attr("disabled", false);
    }
});




const checkPwd = () =>{
    let pwd = document.querySelector("#password_check").value;
    let realpwd = document.querySelector("#password").value;

    console.log(realpwd);

    if (pwd != realpwd){
        alert("입력하신 비밀번호와 일치하지 않습니다. ");
        console.log(pwd);
        document.querySelector("#password").value = null;
        document.querySelector("#password_check").value = null;
        console.log(realpwd);
        document.querySelector("#password").focus();
    }
}
