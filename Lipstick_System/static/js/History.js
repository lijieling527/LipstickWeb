var value;

window.addEventListener('DOMContentLoaded', event => {

    $('button').click(function () {
        value = $(this).val(); // 获取当前点击按钮的value属性值
    });
});

function noReloadprice(method) {  
    formData = "result" + "=" + value;
    
    $.ajax({
        url: '/historyPagepriceSort/'+method,  // 指向Flask應用的URL路由
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