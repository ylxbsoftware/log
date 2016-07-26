### javascript学习点滴

      'use strict'

      var a = 1; //严格模式下必须先声明变量
      var person = {
        name: 'wan',
        age: '20',
        address: 'shenzhen'
      };

      console.log('true', 'name' in person);
      console.log('true', 'toString' in person);
      console.log('false', person.hasOwnProperty('toString'));
      console.log('true', person.hasOwnProperty('age'));
      delete person.age;
      console.log('false', person.hasOwnProperty('age'));

      //map和set是es6中新增的数据类型
      var m = new Map();

      m.set('micro', 50);
      m.set('kob', 90);
      m.set('samin', 80);

      console.log(m.get('samin'));

      var s = new Set();

      s.add(1);
      s.add(2);
      s.add(3);
      s.add(4);
      s.add(5);

      console.log(s);

      for (var t of s) {
        console.log(t);
      }

      var abc = ['123', '123231', '2342342'];

      abc.forEach(function(element, index) {
        console.log(index, element);
      });

      console.log('window的全局作用域：', window.s);

      //查看调用parseINT()调用的次数
      var count = 0;
      var old_parseint = parseInt;

      window.parseInt = function() {
        count += 1;
        return old_parseint.apply(null, arguments);
      }

      parseInt('3');
      parseInt('5');
      parseInt('6');
      parseInt('7');
      console.log('count', count);

      //map高阶函数
      var intArr = [1, 2, 3, 4, 5, 6];
      console.log('map', intArr.map(String));

      var result = intArr.reduce(function(x, y) {
        return x * y;
      });

      console.log(result, 1 * 2 * 3 * 4 * 5 * 6);

      var falseArr = [true, false, true, false];
      var resultArr = falseArr.filter(function(s) {
        return s;
      });

      console.log(resultArr);

      //sort高阶函数
      var word = ['micoro', 'apple', 'Word', 'Big'];

      var sorted = word.sort(function(x, y) {
        var a = x.toLowerCase();
        var b = y.toLowerCase();
        if (a > b) {
          return 1;
        }
        if (a < b) {
          return -1
        }
        return 0;
      });

      console.log('排序后的数组(升序)：', sorted);

