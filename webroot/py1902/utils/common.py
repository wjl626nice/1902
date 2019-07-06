def msg(msg, icon=5, time=2000):
    """
    在iframe错误提示
    :param msg:
    :param icon:
    :param time:
    :return: str
    """
    html = """
        <script type="text/javascript" src="/static/admin/lib/jquery/1.9.1/jquery.min.js"></script>
        <script type="text/javascript" src="/static/admin/lib/layer/2.4/layer.js"></script>
        <script>
            $(function(){
                layer.msg('%s',{icon:%d,time:%d},function(){
                    // 获取父窗口的弹出框标识
                    var index = parent.layer.getFrameIndex(window.name);
                    // 刷新父窗口
                    parent.location.reload();
                    // 根据弹出框的标识---关闭父窗口的弹出框
                    parent.layer.close(index);
                });
            });
        </script>
    """ % (msg, icon, time)
    return html