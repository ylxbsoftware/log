
1. 发送ajax请求成功时执行的通用函数。

        $(document).on('ajaxSuccess', function(data, status) {
          if (status.response.indexOf('C0005') > -1) {
             $('.modal, .modal-overlay').remove();
             $.alert('对不起，该账号已经在另一设备登录，请重新登录。', function() {
                  location.href = 'login.html';
             });
          }
        });

2. 发送ajax请求失败时执行的通用函数。

        $(document).on('ajaxError', function(data, status) {
            $('.modal, .modal-overlay').remove();
            $.alert('服务器异常，请稍后重试！');
        });

3. 如何解决所有ajax请求都需要加请求头信息？

        $(document).on('ajaxBeforeSend', function(e, xhr) {
            xhr.setRequestHeader('u', sessionStorage.getItem('u'));
            xhr.setRequestHeader('token', sessionStorage.getItem('token'));
        });

4. 如何解决ajax后退问题?

        history.replaceState(null, null, 'index.html');

  更新当前历史记录条目的状态对象或URL.

5. 如何解决跨域问题？

  nginx反向代理(配置文件)：

      server {
        listen       80;
        server_name  localhost;

        #charset koi8-r;

        location / {
            root   /Users/wanbao/MOA/src;
            index index.html;
         }

         location /qfang-weixin/  {
            proxy_pass        http://weixin1.qfang.com;
            proxy_set_header  X-Real-IP  $remote_addr;
            proxy_set_header  X-Forwarded-For $proxy_add_x_forwarded_for;
          }
      }

  页面例子：
  
        $.ajax({
          url: 'qfang-weixin/qiye/notice/list',
          type: 'POST',
          data: data,
          success:function(data){}
        });

6. css3 旋转动画(过渡效果)

      效果图：
        
              .step-arrow {
                      -webkit-transition: 400ms;
                            transition: 400ms;
                            -webkit-transition-property: -webkit-transform;
                            transition-property: transform;
                  }

      合并写法：
  
        .step-arrow {
                -webkit-transition: transform  400ms;
                transition: transform 400ms;
            }
            
        .expended .step-arrow{
                  -webkit-transform: rotate(180deg);
                  transform: rotate(180deg);
            }

  transition: property duration timing-function delay;

  transition-property 规定设置过渡效果的 CSS 属性的名称。
  transition-duration 规定完成过渡效果需要多少秒或毫秒。
  transition-timing-function  规定速度效果的速度曲线。
  transition-delay  定义过渡效果何时开始。

  过渡调速函数(贝塞尔曲线)
  http://cubic-bezier.com/

  推荐动画效果库：
  https://daneden.github.io/animate.css/

  对比查看各种调速函数
  注意问题：过渡效果如果持续时间过长，会让网站感觉很慢，最多不超过1s.

7. 优先加载会议室然再加载已预定的会议:
 
  这里用到Deferred解决ajax请求的同步问题.

  解决邪恶金字塔问题：

          function initMeeting(mobile, storey) {
           var deferred = $.Deferred();
            $.ajax({
             url: '/qfang-weixin/qiye/meeting/meetingList'
              …
              success: function(data){{
                  if(){
                        ...
                        deferred.resolve();   //标记会议室列表已经处理完成
                  }else{
                       ...
                        deferred.reject();  //标记出错
                  }
            });
            return deferred;
           }
      
          function initReservedMeeting(mobile, floor) {
              var d1 = initMeeting(mobile, floor);
              $.when(d1).done(function() {
                  reservedMeeting(mobile, floor, useDate);   //调用加载已预订的会议
             });
          }

8. 历史记录功能

      使用技术：本地存储 localStorage
      
      客户端存储数据：
        
      localStorage - 没有时间限制的数据存储
      sessionStorage - 针对一个 session 的数据存储,关闭浏览器窗口后，数据消失。

9. 利用gulp 打包压缩

      js，css  , images, html 压缩，合并 ,加md5后缀解决缓存问题。

10. 代码管理

      http://git.oschina.net

11. 引入字体图标

      阿里巴巴矢量图标库
      http://www.iconfont.cn/
