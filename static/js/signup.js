//유효성 검사 로직
const $inputEelement = $("input, select");  //모든 input 요소를 검사 할 것.
$(".form__submit").attr("disabled", true);   //일단 submit disabled

//input 에서 벗어날 때마다 검사
$("input, select").change(function(){
    canSignup = true;
    $inputEelement.each(function(index, item){
        if(item.value){
        }else {
            console.log(item);
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

(function location(){
    navigator.geolocation.getCurrentPosition(
    function(position) {
    console.log("위도 : " + position.coords.latitude);
    console.log("경도 : " + position.coords.longitude);
    }, 
    );
                
    })();

const getAddr = () => {
    navigator.geolocation.getCurrentPosition(function(position){
        $.ajax({
            url : 'https://dapi.kakao.com/v2/local/geo/coord2address.json?x=' + position.coords.longitude +'&y=' + position.coords.latitude,
            type : 'GET',
            headers : {
              'Authorization' : 'KakaoAK eebc5ddba4a23626be8715744818895c'
            },
            success : function(data) {
              console.log(data['documents'][0]['address']['address_name']);
              
              document.querySelector("#location").value = data['documents'][0]['address']['address_name'];
              },
            error : function(e) {
              console.log(e);   
            }
          })})};

          getAddr();

