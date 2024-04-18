// 1. ajax  stu_score.json 10개 데이터를 출력하시오
// 2. 학생입력 -> 학생추가 프로그램 구성
// 3. 학생수정 -> 학생성적수정이 가능하게 구성하시오.
// 4. 학생삭제 -> 선택된 학생이 되도록 구성하시오.

$(function(){
    //전역 변수
    let s_count = 1;
    let m_id = 0; //여기서 m은 modify라는 의미
    let m_no = 0;
    let m_name = ""; 
    let m_kor = 0;
    let m_eng = 0;
    let m_math = 0;



    //1. 최초 데이터 불러오기
    $.ajax({
        url: "http://192.168.0.242:5500/students/json/stu_score.json",
        data: {},
        type: "get",
        dataType: "json",
        success:function(data){
            //alert("데이터 불러오기 성공");
            console.log(data)
            s_count = data.length;

            let hdata = "";
            for(let i=0; i<10; i++){
                hdata += "<tr id='"+data[i].no+"'>";
                hdata += "<td><input type='checkbox' name='stu' class='stuChk' value='"+data[i].no+"'></td>";
                hdata += "<td>"+data[i].no+"</td>";
                hdata += "<td>"+data[i].name+"</td>";
                hdata += "<td>"+data[i].kor+"</td>";
                hdata += "<td>"+data[i].eng+"</td>";
                hdata += "<td>"+data[i].math+"</td>";
                hdata += "<td>"+data[i].total+"</td>";
                hdata += "<td>"+data[i].avg+"</td>";
                hdata += "<td>"+data[i].rank+"</td>";
                hdata += "<td><button class='delBtn'>삭제</button></td>";
                hdata += "</tr>";
                
            }
            $("#body").html(hdata);
        },
        error:function(){
            alert("데이터 불러오기 실패");
        }
    });//ajax
//--------------------------------------------------------------------------------------------------------------------
    //2. 학생입력
    $("#writeBtn").click(function(){
        //선택된 학생이 있으면 입력 못하도록(우리가 설정한 id value값 때문)
        if($(".stuChk:checked").length >= 1){
            alert("학생성적입력을 하시려면 체크를 해제하셔야 가능합니다. \n자동 체크해제를 하겠습니다.");
            $(".stuChk").each(function(){
                $(this).prop("checked",false);
            });// 체크해제
            return false;
        }

        $(".p_all").css("display","block"); //입력 창 띄우기
        $(".p_main h2").text("학생성적입력");
        $("#name").prop("readonly",false);

    });//writeBtn

    //body에 추가 (성적 입력, 성적 수정)
    $("#confirmBtn").click(function(){
        if($("#id").val() == ""){ //id value값이 빈공백이면 학생성적입력
            
            //성적 입력-------------------------------------------
            s_count += 1;
            let n_name = $("#name").val();
            let n_kor = Number($("#kor").val());
            let n_eng = Number($("#eng").val());
            let n_math = Number($("#math").val());
            let n_total = n_kor + n_eng + n_math;
            let n_avg = (n_total/3).toFixed(1); // 소수점 첫째자리까지
    
            let hdata ="";
            hdata += "<tr id='"+s_count+"'>";
            hdata += "<td><input type='checkbox' name='stu' class='stuChk' value='"+s_count+"'></td>";
            hdata += "<td>"+s_count+"</td>";
            hdata += "<td>"+n_name+"</td>";
            hdata += "<td>"+n_kor+"</td>";
            hdata += "<td>"+n_eng+"</td>";
            hdata += "<td>"+n_math+"</td>";
            hdata += "<td>"+n_total+"</td>";
            hdata += "<td>"+n_avg+"</td>";
            hdata += "<td>"+0+"</td>";
            hdata += "<td><button class='delBtn'>삭제</button></td>";
            hdata += "</tr>";
    
            $("#body").append(hdata);

            //input 초기화
            $("#id").val("");
            $("#name").val("");
            $("#kor").val("");
            $("#eng").val("");
            $("#math").val("");
            $(".p_all").css("display","none");

        }else{ //id value값이 빈공백이 아니면 학생성적수정
            alert("학생수정창 클릭");

            //수정된 성적
            m_no = $("#id").val();
            m_name = $("#name").val();
            m_kor = Number($("#kor").val());
            m_eng = Number($("#eng").val());
            m_math = Number($("#math").val());
            let m_total = m_kor + m_eng + m_math;
            let m_avg = (m_total / 3).toFixed(1); 

            console.log("id : "+m_no);
            console.log("name : "+m_name);
            console.log("kor : "+m_kor);
            console.log("eng : "+m_eng);
            console.log("math : "+m_math);
            console.log("total : "+m_total);
            console.log("avg : "+m_avg);
            
            let hdata ="";
            hdata += "<td><input type='checkbox' name='stu' class='stuChk' value='"+m_no+"'></td>";
            hdata += "<td>"+m_no+"</td>";
            hdata += "<td>"+m_name+"</td>";
            hdata += "<td>"+m_kor+"</td>";
            hdata += "<td>"+m_eng+"</td>";
            hdata += "<td>"+m_math+"</td>";
            hdata += "<td>"+m_total+"</td>";
            hdata += "<td>"+m_avg+"</td>";
            hdata += "<td>"+0+"</td>";
            hdata += "<td><button class='delBtn'>삭제</button></td>";
            
            //원래있던 그 자리에 다시 값을 덮어쓰기 -> html
            $("#"+m_no).html(hdata);

            //input 초기화
            $("#id").val("");
            $("#name").val("");
            $("#kor").val("");
            $("#eng").val("");
            $("#math").val("");
            $(".p_all").css("display","none");
        }
    });// 학생입력,수정버튼

    $("#cancelBtn").click(function(){
        $(".p_all").css("display","none");

        //값 초기화
        $("#id").val("");
        $("#name").val("");
        $("#kor").val("");
        $("#eng").val("");
        $("#math").val("");
    });//cancelBtn
//--------------------------------------------------------------------------------------------------------------   
    // 3. 학생수정
    $("#modifyBtn").click(function(){
        //1명의 학생만을 선택해야해
        if($(".stuChk:checked").length != 1){
            alert("1명의 학생만 선택하셔야 수정이 가능합니다.");
            $(".stuChk").each(function(){
                $(this).prop("checked",false);
            });//체크 해제
            return false;
        }
        //선택한 학생의 성적 불러오기
        let m_id = $(".stuChk:checked").parent()
        m_no = m_id.next().text();
        m_name = m_id.next().next().text();
        m_kor = m_id.next().next().next().text();
        m_eng = m_id.next().next().next().next().text();
        m_math = m_id.next().next().next().next().next().text();
        
        console.log($(".stuChk:checked").parent().next().text());

        //수정창 띄우기
        $(".p_all").css("display","block"); 
        $(".p_main h2").text("학생성적수정");
        $("#name").prop("readonly",true);
        
        //수정창에 값 가져오기
        $("#id").val(m_no);
        $("#name").val(m_name); //readonly로 수정 불가능하게 설정
        $("#kor").val(m_kor);
        $("#eng").val(m_eng);
        $("#math").val(m_math);

    });//modifyBtn

    //수정값 반영
    //위에 confirmBtn 코드에 적어놓음
    //--------------------------------------------------------------------------------------

    // 4. 학생삭제
    // 4-1. 개별삭제
    $(document).on("click",".delBtn",function(){
        let del_id = $(this).parent().parent().attr("id");
        if(confirm(del_id+"번 학생의 성적을 삭제하시겠습니까?")){
            $("#"+del_id).remove();
            //"#"+del_id = #del_id
            //id="del_id"
        }
    }); //개별삭제

    //4-2. 선택삭제
    $("#deleteBtn").click(function(){
        if($(".stuChk:checked").length < 1){
            alert("삭제하려는 학생을 선택해주십시오.");
            return false;
        }
        if(!confirm("정말 삭제하시겠습니까?")){
            return false;
        }
        $(".stuChk").each(function(){
            if($(this).is(":checked")==true){
                //console.log("체크된 학생 수 : "+$(this).length); 여쭤보기!!!!
                console.log("체크된 학생 id : "+$(this).val());
                $("#"+$(this).val()).remove();
            };
        });
    });//선택삭제
    //------------------------------------------------------------------------------------------


    
    


}); //jquery