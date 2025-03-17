$(document).ready(function() {
    console.log("ready")
    var p=document.getElementsByClassName('P');
    function choice(e){        
        var rgba= p[e].value;
        console.log(p[e].value);
        var t = document.getElementById('confirmColor');
        t.value = rgba;
    };
    p[0] .onclick = function (){choice(0)};
    p[1] .addEventListener('click',function() {choice(1)});
    p[2] .addEventListener('click',function() {choice(2)});
    p[3] .addEventListener('click',function() {choice(3)});
    p[4] .addEventListener('click',function() {choice(4)});
    p[5] .addEventListener('click',function() {choice(5)});
    p[6] .addEventListener('click',function() {choice(6)});
    p[7] .addEventListener('click',function() {choice(7)});
    p[8] .addEventListener('click',function() {choice(8)});
    p[9] .addEventListener('click',function() {choice(9)});
    p[10].addEventListener('click',function() {choice(10)});
    
})    
const colorThief = new ColorThief();
function getOffset( el ) {
    var _x = 0;
    var _y = 0;
    while( el && !isNaN( el.offsetLeft ) && !isNaN( el.offsetTop ) ) {
          _x += el.offsetLeft - el.scrollLeft;
          _y += el.offsetTop - el.scrollTop;
          el = el.offsetParent;
    }
    return { top: _y, left: _x };
}
function readURL(input){
    if(input.files && input.files[0]){
        var reader = new FileReader();
        var canvas=document.getElementById('canvas');
        var ctx = canvas.getContext('2d');
        var img = new Image();
        img.addEventListener('load',function(){
            let mainData=colorThief.getColor(img, 10);
            let palette=colorThief.getPalette(img);
            let mainColor = 'rgb(' + mainData[0] + ', ' + mainData[1] +', ' + mainData[2] + ')';
            var mainColor16 = '#' + mainData[0].toString (16)+ mainData[1].toString (16)+ mainData[2].toString (16)  ;
            var d = document.getElementById('P0');
            d.style.background =  mainColor;
            d.value = mainColor16;
            for (var i = 1; i < 11; i++){
                var Pdata=palette[i-1];
                var Pcolor = 'rgb(' + Pdata[0] + ', ' + Pdata[1] +', ' + Pdata[2] + ')';
                var Pcolor16 = '#' + Pdata[0].toString (16)  + Pdata[1].toString (16)   + Pdata[2].toString (16)  ;
                d = document.getElementById('P'+i);
                d.style.background =  Pcolor;
                d.value = Pcolor16;
            }
            let height = img.height;
            let width = img.width;
            var n=height/500
            canvas.width=width/n;
            canvas.height=height/n;
            ctx.drawImage(img,0,0,width/n,height/n);
            img.style.display = 'none';
        })
        reader.onload = function (e) {
            img.setAttribute("src", e.target.result)
        }
        reader.readAsDataURL(input.files[0]); 
        canvas.addEventListener('mousemove', function pick(event) {
            var x = event.layerX;
            var y = event.layerY;
            var X = getOffset( canvas ).left;
            var Y = getOffset( canvas ).top;
            var pixel = ctx.getImageData(x-X, y-Y, 1, 1);
            var data = pixel.data;
            var color = document.getElementById('color');
            var rgb = 'rgb(' + data[0] + ', ' + data[1] +', ' + data[2] + ')';
            color.style.background =  rgb;
            let xy="{"+x+X+"///"+y+Y+"}";
            //color.textContent = rgb+xy;
        });
        canvas.addEventListener('click', function(e){
            var x = e.layerX;
            var y = e.layerY;
            var X = getOffset( canvas ).left;
            var Y = getOffset( canvas ).top;
            var pixel = ctx.getImageData(x-X, y-Y, 1, 1);
            var data = pixel.data;
            var rgb = '#' + data[0].toString (16) + data[1].toString (16) + data[2].toString (16) ;
            color= document.getElementById('confirmColor');
            color.value = rgb;
        }, false);
    }
}