/**
 * 创建函数 createXhr
 * 根据不同的浏览器创建不同的异步对象
 * return : 创建好的异步对象
 */
function createXhr(){
	if(window.XMLHttpRequest){
		return new XMLHttpRequest();
	}else{
		return new ActiveXObject("Microsoft.XMLHTTP");
	}
}