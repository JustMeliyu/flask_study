
function select_fun(){
    var obj = document.getElementById("article_type");
    for(i=0;i<obj.length;i++){
        if(obj[i].value==str)
            obj[i].selected = true;
    }
}