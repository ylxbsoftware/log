### es6深入简出摘要

       Class特性无法发挥出JavaScript原型继承的巨大优势。

##### 1.  for-in是为普通对象设计的，可以遍历得到字符串类型的键，不适用数组遍历。

`强大的for-of循环`

      最简洁，最直接的遍历数组元素的语法
      
      避开了所有for-in循环的所有缺陷
      
      与forEach不同的是，可以正确响应break,continue,return 语句
    
      支持数组，类数组对象（NodeList）,字符串遍历，Map,Set对象遍历。
    
      Set对象可以自动排除重复项。
    
      for-of循环不支持普通对象，如果要迭代一个对象的属性，可以用for-in循环或者
      
      内建的Object.keys()方法。


#####  2.生成器 Generators

   `声明  function*`
    
    `可多次yield，表示遇到yield表达式立即暂停，后续可恢复执行状态。`
    
      function* demo() {
        yield ...
        yield ...
      }
    
      var iter = demo()
    
      iter.next()
      iter.next()

#####  3.模板字符串
    
#####  4.不定参数和默认参数
 
    不定参数： ...args
    
    arguments对象可以被不定参数和默认参数完美代替，移除arguments后
    
    通常会使代码更易阅读。
    
    在使用不定参数和默认参数的函数中禁止使用arguments对象。

#####  5. 解构

       let [var1, var2, ..., varN] = array;
       
       let [head, ...tail] = [1, 2, 3, 4];
       
       console.log(tail)  
       //[2, 3, 4]

#####   6. 箭头函数

      当使用箭头函数创建普通对象时，需要将对象包裹在小括号里。

      var toys = [].map(s => {});   //bug
      var toys = [].map(s => ({}));

#####   7. Symbols

      Symbols是程序创建并且可以用作属性键的值，并且能避免命名冲突的风险。

      var mySymbol = Symbol();
      obj[mySymbol] = 'ok';

#####  8.  集合

      Set, Map, WeakSet, WeakMap

#####  9.  代理 Proxies
    
      代理可以帮助观察或记录对象访问，强化普通对象的能力，例如惰性属性填充。

#####  10. 类 class
#####  11. let 和 const
#####  12. 子类 Subclassing
#####  13. 模块 Modules


