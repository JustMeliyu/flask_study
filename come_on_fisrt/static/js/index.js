//ajax分页开始
$(document).ready(function(e) {
    JiaZai();
    var zys = 0;
//页面加载数据
})
function JiaZai() {
    var n = $("#fy_n").val();//页数显示框里面显示的页数
    $.ajax({
        url: "shipinguanlichuli.php",
        data: {n: n, gjz: ""},//n是显示的页数。gjz是表格显示中有关键字查询，这里gjz传一个空值，意思是没有查询条件，查询所有的。
        type: "POST",
        dataType: "JSON",
        success: function (data) {
            var s = "";
            for (var i in data) {
                s += "<tr><td><input type='checkbox' class='qx'  value='" + data[i].id + "' name='sc[]' /></td><td class='hidden-xs'>" + data[i].id + "</td><td>" + data[i].name + "</td><td class='hidden-xs'>" + data[i].details + "</td><td class='hidden-xs'>" + data[i].wprice + "</td><td class='hidden-xs'>" + data[i].dprice + "</td><td class='hidden-xs'>" + data[i].class + "</td><td><a href='xiugai.php?c=" + data[i].id + "'>修改</a></td><td><a href='shanchuchuli.php?c=" + data[i].id + "' onclick=\"return confirm('确定删除吗？')\">删除</a></td></tr>";//拼接表格显示内容
            }
            $("#a22").html(s);//把拼接好的字符串放到要显示的div里面。
        }
    });

    //获取分页数(列表)
    $.ajax({
        url: "zyschuli3.php",
        type: "POST",
        dataType: "TEXT",
        success: function (data) {
            //总页数
            var ys = Math.ceil(data / 15);
            zys = ys;
            var s = "<div><a id='fy_shang' class='b4'>上一页</a></div>";
            var dangqian = $("#fy_n").val(); //当前页数
            for (var i = dangqian - 2; i <= dangqian + 2; i++) {
                if (i > 0 && i <= ys) {
                    if (dangqian == i) {
                        s += "<div class='b4' class='active'><a class='fy_zhong b4'>" + i + "</a></div>";
                    }
                    else {
                        s += "<div class='b4'><a class='fy_zhong'>" + i + "</a></div>"
                    }
                }
            }
            s += "<div><a id='fy_xia' class='b4'>下一页</a></div>";
            $("#fy_list").html(s);

            //给分页列表加事件
            JiaShiJian();
        }
    })

    //给分页列表加事件的方法
    function JiaShiJian() {
        $("#fy_shang").click(function () {
            var n = $("#fy_n").val();
            if (n > 1) {
                n--;
            }
            else {
                n = 1;
            }
            $("#fy_n").val(n);

            //加载数据
            JiaZai();
        })
        $("#fy_xia").click(function () {
            var n = $("#fy_n").val();
            if (n < zys) {
                n++;
            }
            else {
                n = zys;
            }
            $("#fy_n").val(n);

            //加载数据
            JiaZai();
        })
        $(".fy_zhong").click(function () {
            var n = $(this).text();
            $("#fy_n").val(n);

            //加载数据
            JiaZai();
        })
    }
}
