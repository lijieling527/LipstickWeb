var value, value2, value3;
window.addEventListener('DOMContentLoaded', event => {

    $('button').click(function () {
        value = $(this).val(); // 获取当前点击按钮的value属性值
    });
    $('.liplink').click(function () {
        value2 = $(this).attr('href'); // 获取当前点击链接的href属性值
    });

    /*$('liplink').click(function () {
        value3 = $(this).val(); // 获取当前点击按钮的value属性值
    });*/
});

function openNewWindow() {
    window.open(value2, "_blank");
}

function noReloadlink() {
    formData = "link_url" + "=" + value;
    openNewWindow();

    $.ajax({
        url: '/add_history',  // 指向Flask應用的URL路由
        type: 'POST',
        data: formData,
        success: function (data) {
            if (data['message'] == "success")
                console.log("success!");
            else if (data['message'] == "unsuccess")
                console.log("not yet login!")
        },
        error: function (data) {
            console.log("Error!");
        }
    });
    return false;
}

function noReloadLike() {
    formData = "image_url" + "=" + value;

    $.ajax({
        url: '/member_delete_like',  // 指向Flask應用的URL路由
        type: 'POST',
        data: formData,
        success: function (data) {
            if (data['message'] == "success")
                swal({
                    title: "刪除成功",
                    text: "",
                    icon: "error",
                })
            else if (data['message'] == "unsuccess")
                document.location.href = "/login";
        },
        error: function (data) {
            console.log("Error!");
        }
    });
    return false;
}

function noReloadprice(method) {  
    formData = "result" + "=" + value;
    
    $.ajax({
        url: '/collectionPagePriceSort/'+method,  // 指向Flask應用的URL路由
        type: 'POST',
        data: formData,
        success: function (data) {
            console.log(data["html"]);
            $('body').html(data["html"]);
        },
        error: function (data) {
            console.log("Error!");
        }
    });
    
    return false;
}