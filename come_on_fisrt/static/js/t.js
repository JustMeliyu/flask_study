function loadData(pageNo, pageSize){
    $(".detail").remove(); //每次重新从 API 数据接口获取数据都要先清除原先表格 `<tr>` 的内容
    $.ajax({
        url: "/history_alarm",
        type: "POST",
        data: JSON.stringify({date:date, page_num:pageNo, page_size:pageSize}),
        success:function(result){
            var results = JSON.parse(result);
            var list = results.alarm;
            var totalCount = results.alarm_count;
            pages = results.page_count;
            if(list.length != 0){
                for(var i=0; i<list.length; i++){
                    var alarm_id = list[i].alarm_id;
                    var alarm_pic = list[i].alarm_pic;
                    var date = list[i].date;
                    var event = list[i].event;
                    var time = list[i].time;
                    var remark = list[i].remark;
                    appendData(alarm_id, alarm_pic, date, event, time, remark);
                    addEvent(alarm_id);
                }
                $("#table").show();
                $("#footer").show();
                displayFooter(totalCount, pages, pageNo);
            } else{
                $("#table").hide();
                $("#footer").hide();
            }
        },
        error:function(){
            //error handle function
        }
    });
}

//注意到我们将 `alarm_id` 作为 `<textarea>` 'class` 的值，也作为提交按钮 `id` 的值，这是因为我们要通过 ajax 将用户输入到某一个 `<textarea>` 的值作为参数传给后台 API 接口，由其写入数据库。
function appendData(alarm_id, alarm_pic, date, event, time, remark){
    var text = '<tr class="detail"><td>'+date+'</td><td>'+time+'</td<td>'+event+'</td>'+
        '<td><img class="img01" src=data:image/jpeg;base64,' + alarm_pic + '</td>'+
        '<td class="modity_btn"><textarea cols="5" rows="3"
class='+alarm_id+'>'+remark+'</textarea>'+'<img id='+alarm_id+' src="{{
    static_url("slice/modify.png") }}"></td></tr>';;

$("#table table").append(text);
}
//该函数定义了如何通过 ajax 将用户输入到某一个 `<textarea>` 的值作为参数传给后台 API 接口，并写入数据库
function addEvent(alarm_id){
    $("#"+alarm_id).click(function(){
        var remark = $("."+alarm_id).val();
        if(remark != ""){
            $.ajax({
                url:"/history_alarm",
                type:"POST",
                data:JSON.stringify({alarm_id:alarm_id, note:remark}),
                success:function(result){
                    var results = JSON.parse(result);
                    if(results.status == "ok"){
                        console.log('ok');
                    }
                }
            })
        }
    })
}

function displayFooter(totalCount, pages, pageNo){
    var newText = '共' + totalCount + '条，' + '第' + pageNo + '页，' + '共' + pages + '页';
    $("#summary").text(newText);
}

$("input[name='page_num']").keydown(function(e){
    if(e.keyCode == 13){
        $("input[name='go_btn']").click();
    }
});

$("input[name='go_btn']").click(function(){
    var goPage = $("input[name='page_num']").val();
    if(goPage >= 1 && goPage <=pages && goPage != pageNo){
        pageNo = goPage;
        loadData(pageNo, pageSize);
    } else{
        return false;
    }
});

$("#01").click(function(){
    pageNo = 1;
    loadData(pageNo, pageSize);
});

$("#04").click(function(){
    pageNo = pages;
    loadData(pageNo, pageSize);
});

$("#02").click(function(){
    if(pageNo == 1){
        return false;
    } else{
        pageNo--;
        loadData(pageNo, pageSize);
    }
});

$("#03").click(function(){
    if(pageNo == pages){
        return false;
    } else{
        pageNo++;
        loadData(pageNo, pageSize);
    }
});