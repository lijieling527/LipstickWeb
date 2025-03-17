var value,value2,value3;
window.addEventListener('DOMContentLoaded', event => {    
    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) 
            navbarCollapsible.classList.remove('navbar-shrink');
        else 
            navbarCollapsible.classList.add('navbar-shrink');
    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    //  Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            rootMargin: '0px 0px -40%',
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

    document.getElementById("pic_search").addEventListener('click', () => {
        document.location.href = "/pic_search";
    });

    $('button').click(function() {
        value = $(this).val(); // 获取当前点击按钮的value属性值
    });
   
    /*$('#liplink').click(function () {
        // 获取表单元素
        var form = $('#linkform');

        // 提交表单
        form.submit();
    });*/
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
        success: function(data){
            if(data['message'] == "success")
                console.log("success!");
            else if(data['message'] == "unsuccess")
                console.log("not yet login!")
        },
        error: function(data){
            console.log("Error!");
        }       
    });
    return false;
}

function noReload(){
    formData = "image_url" + "=" + value;

    $.ajax({
        url: '/member_add_like',  // 指向Flask應用的URL路由
        type: 'POST',
        data: formData,
        success: function(data){
            if(data['message'] == "success")
                swal({
                    title: "成功新增至喜好清單",
                    text: "",
                    icon: "success",
                })
            else if(data['message'] == "unsuccess")
                document.location.href = "/login";
        },
        error: function(data){
            console.log("Error!");
        }
    });
    return false;
}