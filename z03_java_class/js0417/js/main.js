$(function(){
    // 최초실행 ---------------------------------------------------------------
    //let no = [1,2,3,4,5,6,7,8,9,10];
    //let name = ['홍길동','유관순','이순신','김구','강감찬','김유신','홍길순','홍길자','이순심','이순돌'];
    //let kor = [77,69,85,89,53,67,75,68,60,50];
    //let eng = [64,53,98,52,53,52,70,79,100,95];
    //let math = [97,80,86,71,92,72,62,73,61,86];
    //let total = [238,202,269,212,198,191,207,220,221,231];
    //let avg = [79.3,67.3,89.7,70.7,66,63.7,69,73.3,73.7,77];
    
    //tbody 부분에 10개행 생성
    //let hdata = "";
    //for(let i=0; i<no.length; i++){
        //hdata += "<tr id='"+no[i]+"'>";
        //hdata += "<td><input type='checkbox' name='stu' class='stuCheck' value='"+no[i]+"'></td>";
        //hdata += "<td>"+no[i]+"</td>";
        //hdata += "<td>"+name[i]+"</td>";
        //hdata += "<td>"+kor[i]+"</td>";
        //hdata += "<td>"+eng[i]+"</td>";
        //hdata += "<td>"+math[i]+"</td>";
        //hdata += "<td>"+total[i]+"</td>";
        //hdata += "<td>"+avg[i]+"</td>";
        //hdata += "<td>0</td>";
        //hdata += "<td><button class='delBtn'>삭제</button></td>";
        //hdata += "</tr>";
        
    //}; //for
    // html소스를 tbody에 추가
    //$("#body").html(hdata);

    //------------------------------------------------------------------------------------
    //전역변수
    let s_count = 10; //학생번호
    let o_id = 0; 
    let o_no = 0; // 학번
    let o_name = ""; //수정 전 이름
    let o_kor = 0; //수정 전 국어성적
    let o_eng = 0;//수정 전 영어성적
    let o_math = 0;//수정 전 수학성적

    //최초 데이터 불러오기
    $.ajax({
        url: "http://192.168.0.242:5500/JAVA_class/js0417/json/stu_score.json",
        type: "get",
        data: {},
        dataType: "json",
        success:function(data){
            alert("데이터 불러오기 성공");
            console.log(data);
            s_count = data.length;
            //console.log(s_count);

            let hdata = "";
            for(let i=0; i<s_count; i++){
                hdata += "<tr id='"+data[i].no+"'>";
                hdata += "<td><input type='checkbox' name='stu' class='stuCheck' value='"+data[i].no+"'></td>";
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
    // 최초실행 --------------------------------------------------------------------------------------------
    
    //검색버튼 클릭
    $("#searchBtn").click(function(){
        if($("#s_word").val().length < 1){
            alert("검색할 학생의 이름을 1글자 이상 입력하세요.");
            return false;
        }

        let s_word = $("#s_word").val();
        console.log("검색어 : "+s_word);

        //alert("test");
        //검색한 데이터 불러오기
        $.ajax({
            url: "http://192.168.0.242:5500/JAVA_class/js0417/json/stu_score.json",
            type: "get",
            data: {},
            dataType: "json",
            success:function(data){
                //alert("데이터 불러오기 성공");
                console.log(data);
                //-----------------------------------------------------------
                let hdata = "";
                for(let i=0; i<s_count; i++){

                    //홍길동.indexOf("홍")
                    if(data[i].name.indexOf(s_word) != -1){
                        hdata += "<tr id='"+data[i].no+"'>";
                        hdata += "<td><input type='checkbox' name='stu' class='stuCheck' value='"+data[i].no+"'></td>";
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
                    };//if
                    
                };//for
                //html소스를 tbody에 추가
                $("#body").html(hdata);
            },
            error:function(){
                alert("데이터 불러오기 실패");}   

        });//ajax
    });//학생검색

    //학생입력버튼 클릭
    $("#writeBtn").click(function(){
        //alert("test");
        if($(".stuCheck:checked").length >= 1){
            alert("학생입력을 하시려면 체크를 해제하셔야 가능합니다.\n자동 체크해제를 하겠습니다.");
            //체크된 것 모두 해제
            $(".stuCheck").each(function(){
                $(this).prop("checked",false);
            });
            return false;
        }
        $(".p_all").css("display","block");
        $(".p_main h2").text("학생성적입력");
        $("#name").attr("readonly",false);
    });
    
    $("#cancelBtn").click(function(){
        $(".p_all").css("display","none");
        //alert("test");
        //초기화
        $("#id").val("");
        $("#name").val("");
        $("#kor").val("");
        $("#eng").val("");
        $("#math").val("");
    });


    //학생입력,수정 확인 버튼
    $("#confirmBtn").on("click",function(){

        if($("#id").val()==""){ //학생성적입력창인 경우 -> id value가 없음
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

            
            s_count += 1;
            let i_no = s_count;
            //no.push(i_no);
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

        }else{ //학생성적수정창인 경우 -> id value가 있음
            alert("학생수정창 클릭");

            //수정된 성적 (new)
            o_no = $("#id").val();
            o_name = $("#name").val();
            o_kor = Number($("#kor").val());
            o_eng = Number($("#eng").val());
            o_math = Number($("#math").val());
            let o_total = o_kor + o_eng + o_math;
            let o_avg = o_total / 3;

            console.log("id : "+o_no);
            console.log("name : "+o_name);
            console.log("kor : "+o_kor);
            console.log("eng : "+o_eng);
            console.log("math : "+o_math);

            let hdata = "";
            //------------------------------------
            hdata += "<td><input type='checkbox' name='stu' class='stuCheck' value='"+o_no+"'></td>";
            hdata += "<td>"+o_no+"</td>";
            hdata += "<td>"+o_name+"</td>";
            hdata += "<td>"+o_kor+"</td>";
            hdata += "<td>"+o_eng+"</td>";
            hdata += "<td>"+o_math+"</td>";
            hdata += "<td>"+o_total+"</td>";
            hdata += "<td>"+o_avg+"</td>";
            hdata += "<td>"+0+"</td>";
            hdata += "<td><button class='delBtn'>삭제</button></td>";
            //htm를 tbody에 추가!
            $("#"+o_no).html(hdata);

            //input 초기화
            $("#id").val("");
            $("#name").val("");
            $("#kor").val("");
            $("#eng").val("");
            $("#math").val("");
            $(".p_all").css("display","none");

        }

    });// 학생입력, 수정버튼


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

    //학생수정버튼 클릭시
    $("#modifyBtn").click(function(){
        //console.log("체크박스에서 체크된 개수: "+$(".stuCheck:checked").length);
        //1명만 선택
       if($(".stuCheck:checked").length != 1){
           alert("1명의 학생만 선택하셔야 수정이 가능합니다.");
           return false;
       }
       
       //선택된 데이터 값 가져오기
       let o_id = $(".stuCheck:checked").parent();
       o_no = o_id.next().text();
       o_name = o_id.next().next().text();
       o_kor = o_id.next().next().next().text();
       o_eng = o_id.next().next().next().next().text();
       o_math = o_id.next().next().next().next().next().text();

       console.log("학번 : "+o_id.next().text());
       
       //수정창 열기
       $(".p_all").css("display","block");
       //선택된 학생정보 가져오기
       $(".p_main h2").text("학생성적수정");
       $("#name").attr("readonly",true);
       $("#id").val(o_no);
       $("#name").val(o_name); //readonly로 수정불가능하게 설정
       $("#kor").val(o_kor);
       $("#eng").val(o_eng);
       $("#math").val(o_math);

       
    });//modifybtn

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