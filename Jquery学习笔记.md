### Jquery学习笔记

1.事件绑定

    //多事件绑定二
    $("#test3").on({
        mousedown: function(e) {
            $(this).text('触发事件：' + e.type)
        },
        mouseup: function(e) {
            $(this).text('触发事件：' + e.type)
        }
    })

    //通过委托机制，点击a元素的时候，事件触发
    $('body').on('click', 'a', function(e) {
       alert(e.target.textContent)
    })

2.选项卡

    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>选项卡</title>
    </head>
    <body>
      <script type="text/javascript" src="http://code.jquery.com/jquery-2.1.4.js"></script>
      <div class="maintab">
        <ul class="tabtitle">
          <li class="tabhover">
            <a href="#">选择标题1</a>
          </li>
          <li class="taba">
            <a href="#">选择标题2</a>
          </li>
          <li class="taba">
            <a href="#">选择标题3</a>
          </li>
        </ul>
        <div class="tabcontent">选择内容1</div>
        <div class="tabcontent" style="DISPLAY: none">选择内容2</div>
        <div class="tabcontent" style="DISPLAY: none">选择内容3</div>
      </div>

      <script type=text/javascript>
        $(document).ready(function () {
            $('.tabtitle li').click(function () {
              var index = $(this).index();
              $(this).attr('class',"tabhover").siblings('li').attr('class','taba');
              $('.tabcontent').eq(index).show(200).siblings('.tabcontent').hide();
            });
        })
      </script>

    </body>
    </html>

3.动画切换比较

        $("#btnShow").click(function() {
        var v = $("#animation").val();
        if (v == "1") {
            $("p").toggle();
        } else if (v == "2") {
            $("p").slideToggle("slow");
        } else if (v == "3") {
            $("p").fadeToggle(1000, "linear");
        }
    });

4.查找在数组中索引的位置

        var v = $("#animation").val();
        var $aaron = $("#aaron");
        $aaron.empty();
        if (v == "1") {

            var index = $.inArray('Aaron', ['test', 'Aaron', 'array', '慕课网']);

            $aaron.text('Aaron的索引是: ' + index)

        } else if (v == "2") {

            //指定索引开始的位置
            var index = $.inArray('a', ['a', 'b', 'c', 'd', 'a', 'c'], 2);

            $aaron.text('a的索引是: ' + index)
        }
    });

5.遍历数组和对象

    $("#exec").click(function() {
        var v = $("#animation").val();
        var $aaron = $("#aaron");
        $aaron.empty();
        if (v == "1") {

            // 遍历数组元素
            $.each(['Aaron', '慕课网'], function(i, item) {
                $aaron.append("索引=" + i + "; 元素=" + item);
            });
        } else if (v == "2") {
            // 遍历对象属性
            $.each({
                name: "张三",
                age: 18
            }, function(property, value) {
                $aaron.append("属性名=" + property + "; 属性值=" + value);
            });
        }
    });

6.通过data存储数据

     $('.left').click(function() {
        var ele = $(this);
        //通过$.data方式设置数据
        $.data(ele, "a", "data test")
        $.data(ele, "b", {
            name : "慕课网"
        })
        //通过$.data方式取出数据
        var reset = $.data(ele, "a") + "</br>" + $.data(ele, "b").name
        ele.find('span').append(reset)
    })
    </script>
    <script type="text/javascript">
    $('.right').click(function() {
        var ele = $(this);
        //通过.data方式设置数据
        ele.data("a", "data test")
        ele.data("b", {
            name: "慕课网"
        })
        //通过.data方式取出数据
        var reset = ele.data("a") + "</br>" + ele.data("b").name
        ele.find('span').append(reset)
    })
