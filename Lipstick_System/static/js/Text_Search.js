$(document).ready(function() {
    var brandSelect=document.getElementById("brand-list");//抓品牌選單
    var lipSelect=document.getElementById("color-list");  //抓口紅選單     
    var div = document.getElementById('color');//抓顯示口紅

    var products=document.getElementById("theBrandLips").textContent;//抓所有口紅
    let brandLips=products.split("], [");//將品牌們分開

    var brand=document.getElementById("allBrand").textContent;//抓所有品牌
    let brands=brand.split(",");//將品牌們分開

    lipSelect.innerHTML="<option value=0>請先選擇品牌</option>";
    var inner='<option value=0>選擇品牌</option>';
    for(var i=1;i<brands.length;i++){
        inner=inner+'<option value='+brands[i]+'>'+brands[i]+'</option>';
    }
    brandSelect.innerHTML=inner;//innerHTML 賦值inner給這element屬性

    var brandIndex=0;

    //動到"brand-list"這select元素後呼叫此方法
    brandSelect.addEventListener('change',function (){
        div.style.background ="";
        if(brandSelect.selectedIndex==0){
            lipSelect.innerHTML="<option value=0>請先選擇品牌</option>";
        }
        else{
            brandIndex=brandSelect.selectedIndex-1;//扣掉第0個空白選項
            let product=brandLips[brandIndex].replace(/\[|\]|\'|\"/g,"").split(", ");//將該品牌的口紅們分開
            var Sinner='<option value="0">選擇口紅</option>';
            for(var i=0;i<product.length;i++){
                Sinner=Sinner+'<option value="'+product[i]+'">'+(product[i].split("->")[0]+"->"+product[i].split("->")[1])+'</option>';
            }
            //抓到"color-list"這select元素，修改其值
            lipSelect.innerHTML=Sinner;
        }
    })

    lipSelect.addEventListener('change',function (){
        //跟剛剛一樣，製造一個字串，以html的語法填入陣列
        let product=brandLips[brandIndex].split(", ");//將該品牌的口紅們分開
        let index=lipSelect.selectedIndex-1;//扣掉第0個空白選項
        var input=product[index];
        input=input.replace(/\[|\]|\'|\"/g,"");
        let products=input.split("->")//分開名字 色號 色碼   
        div.style.background =  products[2];
    })  
})