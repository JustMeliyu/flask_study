
function select_fun(){
    var obj = document.getElementById("article_type");
    for(i=0;i<obj.length;i++){
        if(obj[i].value==str)
            obj[i].selected = true;
    }
}

function is_checked() {
    var remember_me = document.getElementsByName('remember_me');
    return remember_me.checked
    // if (obj.checked == true){
    //     remember_me.checked = true;
    // }else {
    //     remember_me.checked = false;
    // }
}