##javascript权威指南(学习笔记)

###第一章

####1.1 JavaScript语言核心
	
	//JavaScript支持多种数据类型

	var x = 1;  
	    x = 0.01;
		x = "hello world";
		x = 'javascript';
		x = true;
		x = false;
		x = null;
		x = undefined;
		
JavaScript中最重要的数据类型是对象和数组。

	//对象
	var person = {
		name:"万宝",
		flag:true
	};


	//通过.或者[]来访问对象。
	person.name
	person['flag']
	
	person.weight=62;   //通过赋值创建一个属性
	person.content={};	//{}是一个空对象，它没有属性
	
	//数组
	var arr=[];    //空数组
	var nums=[1,2,4,5,6];
	nums[0] //第一个元素
	nums.length  //数组元素个数

	//函数是一种值，可以赋值给变量
	var square=function(x){
		return x*x;
	}


	function move(){
		var answer=confirm("准备好了吗?");
		if(answer) window.location="http://www.taobao.comn";
	}

	setTimetou(move,60000);    //一分钟后执行该函数

	

	//load事件只有在文档加载完毕后才会触发
	
	window.load = function(){

		//找到所有img节点，绑定点击事件
		var imgs=document.getElementByTagName("img");	
		
		for(var i=0;i<imgs.lenght;i++){
			var img=imgs[i];
			if(img.addEventListener){
				img.addEventListener("click",hide,false);;
			}else{
				img.attachEvent("onclick",hide);   //兼容IE8以前的浏览器
			}
		}		
		
	}
	//隐藏函数
	function hide(event){
		event.target.style.visibility = "hide";
	}
	
	
	parseFloat();	//转换为浮点类型
	toFixed(2);   //四舍五入到两位数字
	

存储数据到localStorage对象的属性中。

	function save(amount,year){
		if(window.localStorage){   //只有在浏览器支持的时候才运行这里的代码
			localStorage.amount = amount;
			localStorage.year = year;
		}
	}

	encodeURIComponent();
	JSON.parse();  //将数据解析为js数组

	
###第二章 词法结构

- 字符集
- JavaScript采用Unicode字符集编写
- 区分大小写
- //单行注释和多行注释/******/
- 标识符和保留字

###第三章 类型，值和变量

普通的JavaScript对象是"命名值"得无序集合。JavaScript同样定义了另外一种特殊对象-数组。表示一种带编号值得有序集合。

JavaScript解释器有自己的内存管理机制，可以自动对内存进行垃圾回收。这意味着程序可以按需创造对象。

JavaScript是一门面向对象的语言，这意味着我们不用全局的定义函数去操作不同类型的值。

####3.1 数字

- 整型直接量
- 浮点型直接量

####3.2 日期和时间

####3.3 文本

- 3.3.1 字符串的使用


    	var s = "hello,world";
    	s.charAt(0);  //取得第一个字符
    	s.charAt(s.length-1);  //取得最后一个字符
    	s.substring(1,4);  //第二到第四个字符
		s.slice(1,4);  //同上
		s.slice(-3);  //最后三个字符
		s.indexOf("e");  //e首次出现的位置
		s.lastIndexOf("e"); //e最后一次出现的位置
		s.indexOf("e",3);  //e在索引位置3以后出现的位置
		s.split(",")；   //分隔字符串
		s.replace("h","H");  //全文替换
		s.toUpperCase();  //转换为大写

- 3.3.2 正则表达式

- 3.3.3 布尔值
	
下面这些值会被转换为false。
		
		undefined,null,0,-0,NaN,""	

####3.4 null和undefined
####3.5 全局对象
>全局属性，比如undefine，NaN，Infinify
>全局函数，比如isNaN(),parseInt()和eval().
>构造函数，Date(),RegExp(),String()
>全局对象，比如Math和JSON

####3.6 作用域链