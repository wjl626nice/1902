function checkUsernameAndPassword(un, pwd, checkCode){
	// 用户名 字母开头，后面可以包含字母数字下划线 长度 6-10
	var unReg = /^[a-zA-Z]\w{5,9}$/;
	// 密码 以大写字母开头，后面可以包含字母数字下划线 长度 8-15
	var pwdReg = /^\d{7,14}$/;
	
	if(!unReg.test(un) || !pwdReg.test(pwd) || checkCode != ccode){
		return {
			msg:"用户名或密码或验证码格式不正确",
			enabled:false	
		};
	}else{
		return {
			msg:"用户名或密码格式正确",
			enabled:true	
		};
	}
}

function createRandomNum(){
	var randomNum1 = Math.floor(Math.random()*10);
	var randomNum2 = Math.floor(Math.random()*10);
	var randomNum3 = Math.floor(Math.random()*10);
	var randomNum4 = Math.floor(Math.random()*10);
	
	// 字符串加数字，字符串的拼接，不是算术运算符
	var checkCode = "" + randomNum1 + randomNum2 + randomNum3 + randomNum4; 
	// console.log(checkCode);
	ccode = checkCode;
	document.querySelector("#ccode").innerHTML = checkCode;
}

var preUrl = "http://39.105.222.9:8095/";
var regUrl = "blog/reg_user/";
var loginUrl = "blog/login_user/";
var logoutUrl = "blog/logout_user/";
var allBlog = "blog/query_blog/";
var myBlog = "blog/query_self_blog/";
var publicBlog = "blog/add_blog/";
var deleteBlog = "blog/del_blog/";
var myfollows = "blog/query_user_blog/";