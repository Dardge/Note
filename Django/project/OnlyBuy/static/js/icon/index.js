$(function () {
    //轮播图
    //保存图片路径
    var baseUrl = "../images/index/";
    var arr = ["index_banner3.jpg", "index_banner1.jpg", "index_banner2.jpg", "index_banner4.jpg", "index_banner5.jpg"];
    var index = 0;
    var timer = setInterval(autoPlay, 1000);//每个timeout秒调用一次autoPlay函数

    function autoPlay() {
        $('#banner li').eq(index).css('background', '#fff');//更新下标前先将当前下标的li元素背景色还原
        index++;
        if (index == arr.length) {
            index = 0;
        }
        var url = baseUrl + arr[index];
        $("#banner img").attr('src', url);
        //修改索引的背景颜色
        $('#banner li').eq(index).css('background', 'red');//eq()方法获取的时JQ对象
    }

    //鼠标移入移出 #banner   ()
    $('#banner').mouseover(function () {
        //停止定时器
        clearInterval(timer);
    }).mouseout(function () {
        //重启定时器
        timer = setInterval(autoPlay, 1000);
    });
    // //原生方法
    // $('#banner')[0].onmouseout = function () {
    //     timer = setInterval(autoPlay, 100);
    // };

    //前后翻，图片
    $('#banner a.left').click(function () {
        $('#banner li').eq(index).css('background', '#fff');//更新下标前先将当前下标的li元素背景色还原
        index--;
        if (index==-1){
            index=arr.length-1;
        }
        var url = baseUrl + arr[index];
        $("#banner img").attr('src', url);
        //修改索引
        $('#banner li').eq(index).css('background', 'red');//eq()方法获取的时JQ对象
    });
    $('#banner a.right').click(function () {
        autoPlay();
    });

    //遍历li元素，添加属性ind
    //each():jquery提供的遍历方法
    for (var i=0;i<arr.length;i++){
        //为对象添加属性ind,表示下标
        $('#banner li')[i].ind=i;
    }
    console.log($('#banner li').eq(2));
    $('#banner li').click(function () {
        console.log(this.ind);
        // $('#banner img').attr('src','baseUrl + arr[ind]')//???????????????????
    })

    // $('#banner li').each(function () {
    //     console.log($(this));
    // });

});
