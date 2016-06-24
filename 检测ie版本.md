### 检测IE版本

> 摘自mmGrid
> 
   see: http://tanalin.com/en/articles/ie-version-js/
  	
  	var browser = function () {
  	
    	var isIE = !!window.ActiveXObject;
    	var isIE10 = isIE && !!window.atob;
    	var isIE9 = isIE && document.addEventListener && !window.atob;
    	var isIE8 = isIE && document.querySelector && !document.addEventListener;
    	var isIE7 = isIE && window.XMLHttpRequest && !document.querySelector;
    	var isIE6 = isIE && !window.XMLHttpRequest;

    	return {
      		isIE: isIE,
      		isIE6: isIE6,
      		isIE7: isIE7,
      		isIE8: isIE8,
      		isIE9: isIE9,
      		isIE10: isIE10
    	};
    
  	}();