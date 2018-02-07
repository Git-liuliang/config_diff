/**
 * Created by liuliangliang on 2018/1/30.
 */





$(document).on("click", ".ajaxlog", function () {

   list = $(".key:checked");

    var arr = [];
    list.each(function () {
            arr.push($(this).val())
    });
    var post_data = {};
    for (var key in arr) {
        post_data["nid_"+key] = arr[key];
    }

    console.log(post_data);
    url = "/action/";
    vali_ajax(url, post_data);


    $(".showlog").append("wait time ....."+"<br>");
    $(".showlog").append("fetch the config from the remote server"+"<br>");
    
    $(".listform").css("display","none");
    $(".spinner").css("display","block");

});

function vali_ajax(url,post_data) {
      $.ajax( {
            url:url,
            type:"POST",
            data:post_data,
           success:function (data) {
            data = JSON.parse(data);
            if (data["status"] == 1) {
                $(".showlog").text(data["result"]);
            } else {
			$(".spinner").css("display","none");
			for (line in data["result"]){
                             
                             $(".showlog").append(data["result"][line]+"<br>");
                        }
                        $(".showlog").addClass("border_color_green");
            }
        }
    });
}






