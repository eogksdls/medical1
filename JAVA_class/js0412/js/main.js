$(function(){

    let no = [1,2,3,4,5,6,7,8,9,10];
    let name = ['홍길동','유관순','이순신','김구','강감찬','김유신','홍길순','홍길자','이순심','이순돌'];
    let kor = [77,69,85,89,53,67,75,68,60,50];
    let eng = [64,53,98,52,53,52,70,79,100,95];
    let math = [97,80,86,71,92,72,62,73,61,86];
    let total = [238,202,269,212,198,191,207,220,221,231];
    let avg = [79.3,67.3,89.7,70.7,66,63.7,69,73.3,73.7,77];
    
    let hdata = "";
    for(let i=0; i<no.length; i++){
        hdata += "<tr id='"+no[i]+"'>";
        hdata += "<td><input type='checkbox' name='stu' class='stuCheck' value='"+no[i]+"'></td>";
        hdata += "<td>"+no[i]+"</td>";
        hdata += "<td>"+name[i]+"</td>";
        hdata += "<td>"+kor[i]+"</td>";
        hdata += "<td>"+eng[i]+"</td>";
        hdata += "<td>"+math[i]+"</td>";
        hdata += "<td>"+total[i]+"</td>";
        hdata += "<td>"+avg[i]+"</td>";
        hdata += "<td>0</td>";
        hdata += "<td><button class='delBtn'>삭제</button></td>";
        hdata += "</tr>";
        
    }; //for
    // html소스를 tbody에 추가
    $("#body").html(hdata);

// 최초실행 ---------------------------------------------------------------

    //학생입력버튼 클릭
    $("#writeBtn").click(function(){
        //alert("test");
        $(".p_all").css("display","block");
    });
    
    $("#cancelBtn").click(function(){
        //alert("test");
        $(".p_all").css("display","none");
    });


    //학생입력확인 버튼
    $("#confirmBtn").click(function(){
        // 글자-text() innerText
        // input-val() value, html() innerHTML
        console.log("이름 : "+$("#name").val());
        console.log("국어 : "+$("#kor").val());
        console.log("영어 : "+$("#eng").val());
        console.log("수학 : "+$("#math").val());
        // 학생 추가 시 새로운 번호 생성(일단 가장 큰 번호 호출하기)
        //console.log(Math.max.apply(null,no)+1);
        //no.push(Math.max.apply(null,no)+1); //no배열에 추가
        
        //공백확인
        if($("#name").val().length < 2){
            alert("이름을 입력하여야 학생등록이 가능합니다.");
            $("#name").focus();
            return false;
        }else if($("#kor").val().length < 1){
            alert("국어 점수를 입력해주세요.");
            $("#kor").focus();
            return false;
        }else if($("#eng").val().length < 1){
            alert("영어 점수를 입력해주세요.");
            $("#eng").focus();
            return false;
        }else if($("#math").val().length < 1){
            alert("수학 점수를 입력해주세요.");
            $("#math").focus();
            return false;
        }

        
        let i_no = Math.max.apply(null,no)+1;
        no.push(i_no);
        let i_name = $("#name").val();
        let i_kor = Number($("#kor").val());
        let i_eng = Number($("#eng").val());
        let i_math = Number($("#math").val());
        let i_total = i_kor+i_eng+i_math;
        let i_avg = (i_total/3).toFixed(1); // 소수점 둘째 자리까지 반올림
        let i_rank = 0;

        //table tr추가
        let hdata = "";
        hdata += "<tr id='"+i_no+"'>";
        hdata += "<td><input type='checkbox' name='stu' class='stuCheck' value='"+i_no+"'></td>";
        hdata += "<td>"+i_no+"</td>";
        hdata += "<td>"+i_name+"</td>";
        hdata += "<td>"+i_kor+"</td>";
        hdata += "<td>"+i_eng+"</td>";
        hdata += "<td>"+i_math+"</td>";
        hdata += "<td>"+i_total+"</td>";
        hdata += "<td>"+i_avg+"</td>";
        hdata += "<td>"+i_rank+"</td>";
        hdata += "<td><button class='delBtn'>삭제</button></td>";
        hdata += "</tr>";

        // html소스를 tbody에 추가
        //$("#body").html(hdata); //기존 html에 덮어쓰기
        //$("#body").prepend(hdata); //기존 html 위쪽에 추가
        $("#body").append(hdata); //기존 html 뒤쪽에 추가

        //input 초기화
        $("#name").val("");
        $("#kor").val("");
        $("#eng").val("");
        $("#math").val("");
        $(".p_all").css("display","none");

    });// 학생입력버튼

    //전체선택
    $("#allChk").click(function(){
        if($(this).is(":checked") == true){
            //모든 체크박스 체크
            console.log("체크되었습니다.");
            $(".stuCheck").each(function(){ //class='stuCheck'의 모든 체크박스 불러오기
                $(this).prop("checked",true);
            })
        }else{
            //console.log("체크해제 되었습니다.");
            $(".stuCheck").each(function(){ //class='stuCheck'의 모든 체크박스 불러오기
                $(this).prop("checked",false);
            })
        }
    });//체크박스 전체선택


    //table에 있는 삭제버튼 클릭
    $(document).on("click",".delBtn",function(){
        let del_id = $(this).parent().parent().attr("id");
        console.log("현재 선택된 class id : "+del_id);
        if(confirm(del_id+"번 학생의 성적을 삭제하시겠습니까?")){
           $("#"+del_id).remove();
        }
        
    });// table 삭제버튼
    
    // 동적으로 할당될 경우 실행 안됨(새롭게 추가된 학생 삭제 불가능)
    //$(".delBtn").click(function(){
        //let del_id = $(this).parent().parent().attr("id");
        //console.log("현재 선택된 class id : "+del_id);
        //if(confirm(del_id+"번 학생의 성적을 삭제하시겠습니까?")){
           //$("#"+del_id).remove();
        //}
        
    //});// table 삭제버튼

    //하단 삭제버튼 클릭
    $("#deleteBtn").click(function(){
        //alert("test");
        console.log("체크박스 개수 : "+$(".stuCheck").length);
        //체크된 개수를 셀수 있는 코드
        console.log("체크박스에서 체크된 개수 : "+$(".stuCheck:checked").length);
        console.log("체크박스에서 체크된 개수 : "+$("input:checkbox[name='stu']:checked").length);
        
        //체크되어 있는 것이 없을 때
        if($(".stuCheck:checked").length < 1){
            alert("삭제할 학생을 선택해주세요.");
            return false;
        }
        //현재 체크박스가 체크가 되어있는지 확인
        if(!confirm("정말 삭제하시겠습니까?")){
            return false; //no버튼 클릭시 다시 돌아감
        }
        //모든 체크박스를 가져오기
        $(".stuCheck").each(function(){
            if($(this).is(":checked") == true){
                console.log("현재 선택된 class id : "+$(this).val());
                $("#"+$(this).val()).remove();
            };
        });
    });//하단 삭제버튼




});//무명함수