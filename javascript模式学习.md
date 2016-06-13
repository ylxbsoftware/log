1. 使用hasOwnProperty方法过滤来自原型链中继承来的树形。

    	var own = {
        a: 1,
        b: 2
    	};
    
    	if (typeof Object.prototype.clone === 'undefined') {
        		Object.prototype.clone = function() {};
    	}
    
    	for (var i in own) {
        	if (own.hasOwnProperty(i)) {
            	console.log(own[i]);
        	}
    	}
   
	这样可以过滤添加的clone方法， 另外一种方法：
	
    	for (var i in own) {
        	if (Object.prototype.hasOwnProperty.call(own, i)) {
           		console.log(own(i));
        	}
    	}

	好处： 在own对象中重新定义了hasOwnProperty方法的情况下， 可以避免调用时的命名冲突。
	为了避免查找属性时从Object对象一路找到原型的冗长过程， 你可以定义一个变量来缓存它。

    	var i, hasOwn = Object.prototype.hasOwnProperty;
    	for (i in own) {
        	if (hasOwn.call(own, i)) {
            	console.log(own[i])
        	}
   		}

2. 扩充内置原型， 添加自定义方法(不推荐) 

		if (typeof Object.prototype.myMethod !== 'function') {
			Object.prototype.myMethod = function() {
		    	//实现
			}
		}

3. 避免隐式类型转换

    	var zero = 0;
    	if (zero == false) {
        	//会执行
    	}

		方法： 推荐使用 === 和 !== 运算符

4. 避免使用eval()

5. 使用parseInt() 进行数字转换

	在使用parseInt将字符串转换为数字时， 函数的第二个参数应该被指定， 但是通常被忽略了。
	当字符串以0为前缀时转换就会出现问题。

    	var year = '06';
    	parseInt(year, 10);

	如果使用parseInt(year), 06 会被认为是八进制数。
	字符串转换为数字还有两种方法：

    	+ '08'结果为8
    	Number('08') 结果为8

	这两种方法比parseInt更快一些， 因为顾名思义parseInt是一种解析而不是简单地转换。 但当你期望将 '08 hello' 这类	字符串转换为数字的时候， 则必须使用parseInt, 其他方法都会返回NaN.

6. 构造函数和普通函数
    
    	function MyConstructor() { ... }
    	function myFunction() { ... }
