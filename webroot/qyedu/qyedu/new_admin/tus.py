# 展示信息跳转
def show_message(msg,url):
	str = '<script>alert("'+ msg + '");location.href="' + url + '"</script>'
	return str