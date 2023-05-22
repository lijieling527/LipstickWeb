$(document).ready(function() {
    // 監聽文件上傳事件
    $('#imageUpload').change(function() {
        var file = this.files[0];
        var reader = new FileReader();

        reader.onload = function(e) {
            var imageSrc = e.target.result;

            // 將圖片顯示在網頁上
            $('#imageContainer').html('<img src="' + imageSrc + '">');

            // 傳送圖片給Python後端進行處理
            $.ajax({
                url: '/picture_color_code',
                type: 'POST',
                data: { "image": imageSrc },
                success: function(response) {
                    // 在成功回調中處理Python後端返回的RGB值
                    var rgbValues = response.rgb;
                    console.log(rgbValues);
                    // 在此可以根據需要進行進一步處理或顯示
                },
                error: function(xhr, status, error) {
                    // 處理錯誤
                    console.log(error);
                }
            });
        };
        reader.readAsDataURL(file);
    });
  });