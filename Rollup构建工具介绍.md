# Rollup.js
>此文章by wanbao 原创文章，译自[官网](https://rollupjs.org/),欢迎大力转载，但希望能全文转载。

### 为什么


通过 ES2015 的解构赋值语法引入模块，可以让打包工具（browserify）最终编译出来的代码量最小化。

通过它可以让你的 bundle 最小化，有效减少文件请求大小——以至于连 vue 都迅速地转投它来打包模块。

Tree-shaking
在 Rollup 编译模块的过程中，通过 Tree-shacking 的方式来剔除各模块中最终未被引用到的方法，通过仅保留被调用到的代码块来缩减 bundle 的大小。

开始：
 
	npm install --global rollup 

### 命令行的方式运行

浏览器：

	rollup main.js --format iife --output bundle.js
	
Node.js

	# compile to a CommonJS module
	rollup main.js --format cjs --output bundle.js

### 配置文件的方式
创建 ```rollup.config.js```文件，配置如下：

	export default {
	  entry: 'src/main.js',
	  format: 'cjs',
	  dest: 'bundle.js' // equivalent to --output
	};


开发模式，需要安装rollup-watch 插件，自动监听

	{
	  ...,
	  "scripts": {
	    "build": "rollup -c",
		 "dev": "rollup -c -w"
	  },
	  ...
	}
	

### 插件系统

 为了构建更为复杂的bundles,比如说导入npm安装的模块，利用babel编译代码，或者配合json文件等，我们就需要利用rollup的插件，在Rollup打包的过程当中能够改变某些行为方式。[插件地址](https://github.com/rollup/rollup/wiki/Plugins)

```` rollup-plugin-json  ```` 允许Rollup从json文件中导入数据

	export default {
	  entry: 'src/main.js',
	  format: 'cjs',
	  plugins:[json()],
	  dest: 'bundle.js' // equivalent to --output
	};
	
	
需要注意的是，在导入package.json文件后，main.js我们仅仅是需要version这个变量，那么package.json文件中其他的变量都不会导入进来，这得益于tree-shaking这个特性。

	
```` rollup-plugin-node-resolve ```` 让Rollup寻找外部模块

```` rollup-plugin-babel ```` ES6转换器

	// rollup.config.js
	import resolve from 'rollup-plugin-node-resolve';
	import babel from 'rollup-plugin-babel';
	
	export default {
	  entry: 'src/main.js',
	  format: 'cjs',
	  plugins: [
	    resolve(),
	    babel({
	      exclude: 'node_modules/**' // only transpile our source code
	    })
	  ],
	  dest: 'bundle.js'
	};
	
在此之前，先创建````src/.babelrc````文件：

	{
	  "presets": [
	    ["latest", {
	      "es2015": {
	        "modules": false
	      }
	    }]
	  ],
	  "plugins": ["external-helpers"]
	}	
	
	
安装```` npm i -D babel-preset-latest babel-plugin-external-helpers ````  此时，就能开始写ES6代码了。

### 支持Sourcemaps

配置

	export default {
	  entry: 'src/main.js',
	  format: 'umd',
	  dest: 'bundle.js',
	  sourceMap: true
	};
	
### 友好提示

#### 1.什么是tree-shaking?
		
#### 2.为什么ES2015模块比amd,cmd要好？

ES2015模块是一种在不久的将来出现在浏览器和Node.js中的官方标准。它在静态分析代码的时候能够像tree-shaking一样压缩代码，并且拥有循环引用，实时绑定等高级特性。

### 3.谁制作了Rollup的logo?It is lovely.

[Julian Lloyd](https://medium.com/@Rich_Harris/tree-shaking-versus-dead-code-elimination-d3765df85c80#.jnypozs9n)
	
### 对比其他工具

coming soon...	


### 集成gulp

Rollup返回一个能够被gulp识别的promises,所以集成很简单。

下面的语法类似于一个配置文件，但是属性被分成两种不同的操作。构造一个bundle并且输出到目标文件。

	var gulp = require('gulp')
    rollup = require('rollup')
    rollupTypescript = require('rollup-plugin-typescript');
	
	gulp.task('build', function () {
	  return rollup.rollup({
	    entry: "./src/main.ts",
	    plugins: [
	      rollupTypescript()
	    ],
	  })
    .then(function (bundle) {
      bundle.write({
        format: "umd",
        moduleName: "library",
        dest: "./dist/library.js",
        sourceMap: true
      });
    })
	});