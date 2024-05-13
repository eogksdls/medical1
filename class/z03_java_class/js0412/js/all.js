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
        hdata += "<td><input type='checkbox' name='stu' class='stuChk' value='"+no[i]+"'></td>";
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
// 최초실행-----------------------------------------------------------------------
    
    //학생성적입력
    $("#confirmBtn").click(function(){
        console.log("이름 : "+$("#name").val());
        console.log("국어점수 : "+$("#kor").val());
        console.log("영어점수 : "+$("#eng").val());
        console.log("수학점수 : "+$("#math").val());

        let i_no = Math.max.apply(null,no)+1;
        no.push(i_no);
        let i_name = $("#name").val();
        let i_kor = Number($("#kor").val());
        let i_eng = Number($("#eng").val());
        let i_math = Number($("#math").val());
        let i_total = i_kor+i_eng+i_math;
        let i_avg = (i_total/3).toFixed(1); // 소수점 첫째자리까지 나타내기
        let i_rank = 0;

        if($("#name").val().length < 2){
            alert("이름을 입력하셔야 학생성적 등록이 가능합니다.");
            $("#name").focus();
            return false;
        }else if($("#kor").val().length < 1){
            alert("국어 성적을 입력해주세요.");
            $("#kor").focus();
            return false;
        }else if($("#eng").val().length < 1){
            alert("영어 성적을 입력해주세요.");
            $("#eng").focus();
            return false;
        }else if($("#math").val().length < 1){
            alert("수학 성적을 입력해주세요.");
            $("#math").focus();
            return false;
        }

        //table에 학생 추가
        let hdata = "";
        hdata += "<tr id='"+i_no+"'>";
        hdata += "<td><input type='checkbox' name='stu' class='stuChk' val='"+i_no+"'></td>";
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
        
        //html 소스를 tbody에 추가
        $("#body").append(hdata);

        //input 초기화
        $("#name").val("");
        $("#kor").val("");
        $("#eng").val("");
        $("#math").val("");
        $(".p_all").css("display","none");
    });//학생성적입력

    // 개별 삭제(새롭게 추가된 학생 삭제 가능)
    $(document).on("click",".delBtn",function(){
        let del_id = $(this).parent().parent().attr("id");
        console.log("현재 선택된 class id : "+del_id);
        //삭제 전 물어보는 창
        if(confirm(del_id+"번 학생의 성적을 삭제하시겠습니까?")){
            $("#"+del_id).remove();
        };
    });//개별삭제(새롭게 추가된 학생도 가능)


    //개별 삭제(새롭게 추가된 학생은 삭제 안됨)
    //$(".delBtn").click(function(){
        //let del_id = $(this).parent().parent().attr("id");
        //console.log("현재 선택된 class id : "+del_id);
        //삭제 전 물어보는 창 띄움
        //if(confirm(del_id+"번 학생의 성적을 삭제하시겠습니까?")){
            // $("#"+del_id).remove();
        //};
    //}); //개별 삭제
    
    //전체선택
    $("#allChk").click(function(){
        if($(this).is(":checked") == true){
            console.log("모두 체크되었습니다.");
            $(".stuChk").each(function(){
                $(this).prop("checked",true);
            })
        }else{
            console.log("모두 해제되었습니다.");
            $(".stuChk").each(function(){
                $(this).prop("checked",false);
            })
        }
    });//전체선택

    //선택 학생성적삭제
    $("#deleteBtn").click(function(){
        console.log("체크박스 개수 : "+$(".stuChk").length); //체크박스 총 개수
        console.log("내가 체크한 박스 개수 : "+$(".stuChk:checked").length);

        //체크 없이 삭제 버튼을 눌렀을 때
        if($(".stuChk:checked").length < 1){
            alert("삭제할 학생을 선택해주세요.")
            return false;
        };
        //현재 체크박스가 체크되어 있는지 확인
        if (!confirm("정말 삭제하시겠습니까?")){
            return false; // 취소 버튼 누르면 무효되게
        };
        //체크된 박스 삭제하기
        $(".stuChk").each(function(){ //체크박스 정보 다 가져오고나서 체크된것만 확인
            if($(this).is(":checked") == true){
                $("#"+$(this).val()).remove();
            };
        });
    });//선택 학생성적삭제

    //학생검색

    //---------------------------------------------------------------------

    //학생성적입력 팝업 칸
    $("#writeBtn").click(function(){
        $(".p_all").css("display","block");
    })
    $("#cancelBtn").click(function(){
        $(".p_all").css("display","none");
    })







});//무명함수