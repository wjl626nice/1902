from bs4 import BeautifulSoup

html_str = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title>
        【10图】碧源月湖两室，可自住或办公，房东诚意出租，随时看,开元路-郑州58同城    </title>
    <meta name="description" content="郑州惠济开元路2室2厅1卫价格1800元/月诚心出租此房屋，看房质量不要看报的价格，根据房子质量给出你心目中合理的价格；1、我的房子地理位置非常好，2、交通便利，附近公交很方便，地铁、公交也有，上班的话，节约了您的步行时间，在郑州四通发达"/>
    <meta http-equiv="Cache-Control" content="no-transform " />
    <meta http-equiv="mobile-agent" content="format=xhtml; url=https://m.58.com/zz/zufang/38418522983076x.shtml">
<meta http-equiv="mobile-agent" content="format=html5; url=https://m.58.com/zz/zufang/38418522983076x.shtml">
<meta http-equiv="mobile-agent" content="format=wml; url=https://m.58.com/zz/zufang/38418522983076x.shtml">


    <!--TODO 新增：页面主样式-->
    <link rel="stylesheet" href="//c.58cdn.com.cn/frs/fangfe/zufang-pc-site/1.0/zf-detail/index_v20190614211142.css">

    <!--公共组件（header、footer）样式-->
    <link type="text/css" rel="stylesheet" href="//c.58cdn.com.cn/componentsLoader/dist/CompontsLoader_v20190402152128.css" media="all"/>
    <!-- 孙悟空引入的样式-->
    <!--
    <link rel="stylesheet" href="//c.58cdn.com.cn/ui6/my/css/MrSun_pc_v20160114174536.css"/>
    -->
    <!-- limitbutton的样式 -->
    <!--
    <link type="text/css" rel="stylesheet" href="//c.58cdn.com.cn/ui7/css/easydialog_v20151228154544.css" media="all"/>
    -->
    <!-- seo优化 -->
    <link rel="alternate" media="only screen and(max-width: 640px)" href="https://m.58.com/zz/zufang/38418522983076x.shtml">

    <!--字体加密相关-->
    <script>!function(w,d){if(!w.ActiveXObject||d.documentMode>8){d.write("<style>@font-face{font-family:'fangchan-secret';src:url('data:application/font-ttf;charset=utf-8;base64,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') format('truetype')}.strongbox{font-family:'fangchan-secret','Hiragino Sans GB','Microsoft yahei',Arial,sans-serif,'宋体'!important}</style>")}else{d.write("<style>@font-face{font-family:'fangchan-secret';src:url('//fangfe.58.com/sfont/709b3ed7e7419df783e85f2156ea3beb.eot')}.strongbox{font-family:'fangchan-secret','Hiragino Sans GB','Microsoft yahei',Arial,sans-serif,'宋体'!important}.strongbox{visibility:hidden}</style>");var i=d.createElement('img');i.onerror=function(){setTimeout(function(){var s=document.createElement('style'),n=document.getElementsByTagName('script')[0];s.type='text/css';s.styleSheet.cssText='.strongbox{visibility:visible!important}';n.parentNode.insertBefore(s,n);},1300)};i.src='//fangfe.58.com/sfont/709b3ed7e7419df783e85f2156ea3beb.eot';}}(window,document);</script>
    <!-- 页面基本的信息和配置 -->
    <script type="text/javascript">
        document.domain = '58.com';
        try {
            var ____json4fe = "";
            ____json4fe = {"rootcatentry":{"dispid":1,"name":"\u623f\u4ea7\u4fe1\u606f","listname":"house"},"catentry":{"dispid":8,"name":"\u79df\u623f","listname":"zufang"},"locallist":[{"dispid":342,"name":"\u90d1\u5dde","listname":"zz"},{"dispid":5518,"name":"\u60e0\u6d4e","listname":"huiji"},{"dispid":12657,"name":"\u5f00\u5143\u8def","listname":"kaiyuanl"}],"infoid":38418522983076,"userid":54844713088787,"linkman":null,"is_huzhuan":"false","modules":"finalpage","shipin":"","start":1560818276000,"isbiz":true,"isport":true,"xiaoqu":{"name":"\u78a7\u6e90\u6708\u6e56\u666f\u56ed","lat":34.878822,"lon":113.639258,"baidulat":34.878822,"baidulon":113.639258},"info":{"isChengxin":false},"_trackPagetype":"detail","_trackURL":"{'cate':'1,8','cateBusiness':null,'area':'342,5518,12657','is_biz':true,'stats':11,'pagetype':'detail','source':6,'page':'','is_real':false,'8635':'','shopid':'','product':'[jingxuan]','infolabel':'[null]','type':'[fufei]','infoSource':1,'userid':54844713088787,'trackkey':'38418522983076_ede04a2e-8a5e-4eb4-85a6-90a08844d9af_20190618083756_1560818276025','fcinfotype':'gz','anxuan':0}","_trackParams":[{"I":1016,"V":"1800"},{"I":1019,"V":"3"},{"I":1020,"V":"5"},{"I":12385,"V":"2"},{"I":1021,"V":"2"},{"I":12384,"V":"2"},{"I":1022,"V":"11,12,9,8,10,13,14,6,17,15,674989,674990,674991"},{"I":12386,"V":"1"},{"I":111501,"V":"\/anjuke_58\/4b5d0274a7d6f63ca8644a1e9943ba8a"},{"I":11419,"V":"\/anjuke_58\/6063ed5b782d7975211ecb770dfb2e5f|\/anjuke_58\/69c9e926ececdc59fd9bfe56fc1bb9b6|\/anjuke_58\/430af9a4d9865c995ad6f03363035118|\/anjuke_58\/4b5d0274a7d6f63ca8644a1e9943ba8a|\/anjuke_58\/d11855d5714cc61b97e1f02628a6c91b|\/anjuke_58\/35cab1da3f68cd224f159caf7d72a4fa|\/anjuke_58\/e19e9d13d88ff5e2efe9cb2c5a7de106|\/anjuke_58\/ad63e90c8ad7fa2776e49803886badaa|\/anjuke_58\/7b556fb9f04b52fd3060b1ed2a689d03"},{"I":1025,"V":"50"},{"I":1028,"V":"4"},{"I":12135,"V":"683018|4"},{"I":11420,"V":"\/anjuke_58\/1584888d2abe0584d42e250c0d359e91"},{"I":11421,"V":""},{"I":1597,"V":"1"},{"I":1596,"V":"20"},{"I":10652,"V":"35756204979713"},{"I":1594,"V":"1"},{"I":8992,"V":"26"},{"I":1592,"V":"1"},{"I":10589,"V":"26000000"},{"I":1591,"V":"2"},{"I":1590,"V":"2"},{"I":9184,"V":"2019-12-16 00:00:00"},{"I":1588,"V":"2012883"},{"I":12470,"V":""},{"I":10200,"V":"0"},{"I":10201,"V":"0"},{"I":10202,"V":"0"},{"I":10203,"V":"0"},{"I":9053,"V":"1"},{"I":5333,"V":"\u674e\u59ae\u65e6"},{"I":6692,"V":"113.639258"},{"I":5100,"V":"\u5f00\u5143\u8def"},{"I":6691,"V":"34.878822"},{"I":5379,"V":""}],"_trackPageview":"\/house\/rentDetail","supplycount":"{\"paramdata\":{\"MinPrice\":1800,\"huxingting\":\"2\",\"huxingshi\":\"2\",\"huxingwei\":\"1\",\"jushishuru\":1,\"HireType\":\"\"}}","entName":"\u521b\u4f73\u623f\u4ea7","shopUrl":"http:\/\/t5863717028265476.5858.com","userName":"\u674e\u59ae\u65e6","headPic":"\/\/pic1.ajkimg.com\/display\/6f1bd407ca6ec4bdab07b3be1a2a254d\/100x133.jpg","creditRecord":"\/\/houserent.58.com\/landlord\/center?infoId=38418522983076&brokerId=7703505&city=zz","sanWangBrokerId":"7703505","my58":null,"serviceTime":null,"ssp_abtest":"legoC_fc","slotIds":"8,16,1000170,1000014,1000015,1000016,1000017,1000018","req_version":"1.0.0"};
            ____json4fe.modules = 'finalpage';
            ____json4fe.sid = '136809752204579573080767332';
            ____json4fe.pid = '756';
            ____json4fe.sessionid = '';
            ____json4fe.newImVersion = true;
            ____json4fe.privacyCallUrl = 'https://apihouse.58.com/house/privacyCall?value=BA3A701F4F575D57BB832004CFE0DF84F2D6441607A08A2AF24F439B7E7D2F6C5C7194E6BDFD82F181B61A1A0B48A6DE0A8492C9C2AC444F5F0ED15BA5AF8BE2FF916C3594B218840B1FE151C30B2BC658642CDDDBAB4E5C2C24017CAC84EA46782ED8521C7762E3FBA3891896E50FE0C5FDA2C08E95DB87AE092C113D13CE45EC2F0E79C946AF1EA3FC577C6B36110C65896FE38917F0CDA6CED7F20F259B3ADBAA2C45E079FC85BBD480CDD1D286B853A5653CA2320B03073F78866E63A1F4E4E510C57E89A5956D5F195DB699C9FF6A27CFA3EA943256DD667CD6E005FFCBB46C405F22B8A26F1D8A86783D1022698676B550F4D91BAEBF136B28109F9C48AA1E95B23D1BE8D447990805E00AF2D4D380D5CBD6B96149A3907FBCBC73591A455A9E95C5ACD78DE0C2A98EAA863B41838886216C6810CE7E60FEAB9426EF8A';
            ____json4fe.hunterCheckUrl = 'http://apihouse.58.com/house/api_hunter_check?userid=7703505&infoid=38418522983076&rootcateid=1&secondcateid=8&platform=1&cityid=342&cellphone=609fjpv4gYnCTxP3HhPWulGWnI4bd6MRQpYVwnnrwAeHG7FUvBg3NQ';
            ____json4fe.practitionerIdUrl = 'https://rentercenter.58.com/broker/api_get_cert_company';
            ____json4fe.legoFeeURL = '';
        } catch (e) {
        }

        var _trackPagetype = ____json4fe._trackPagetype;
        var _trackURL = ____json4fe._trackURL;
        var _trackParams = ____json4fe._trackParams;
        var _trackPageview = ____json4fe._trackPageview;

                var fromMess = 'zzxqsidebar';
            </script>
</head>
<body>
    <div id="adfad">asdfasdf</div>
    <!-- 导航条 -->
    <div id="commonTopbar" class="commonTopbar"></div>

    <!-- 关键字搜索 --><!-- 需要修改：替换原来的<div class="conwrap">....</div-->
    <div id="header-wrap" class="header-wrap">
        <div class="content clearfix">
            <a class="logo fl" href="//zz.58.com/house.shtml" target="_blank" onClick="clickLog('from==fcpc_list_zz_58fclogo')"></a>
            <a class="top-publish-news fr"
               href="//post.58.com/fang/342/8/s5"
               target="_blank"
               onClick="clickLog('from=fcpc_list_zz_fabu')"
            >免费发布</a>
        </div>

        <div class="nav-top-bar fl f12">
            <a href="https://zz.58.com/" target="_blank">郑州58同城 </a>
                        > <a href="https://zz.58.com/zufang/" target="_blank">郑州租房</a>
                        > <a href="https://zz.58.com/huiji/zufang/" target="_blank">惠济租房</a>
                        > <a href="https://zz.58.com/kaiyuanl/zufang/" target="_blank">开元路租房</a>
                    </div>
    </div>

    <!--房源信息-->
    <div class="main-wrap">
        <!--房源题目-->
        <div class="house-title">
            <h1 class="c_333 f20 strongbox" id="title">碧源月湖两室，可自住或办公，房东诚意出租，随时看</h1>

            <p class="house-update-info c_888 f12">
                06-10&nbsp;&nbsp;&nbsp;&nbsp;<em id="totalcount">0</em> 次浏览
            </p>

            <div class="title-right-info f12">
                <a id="su_kfdnew" class="collect-house pr c_888 clt-btn" href="javascript:;"
                    onclick="clickLog('from=fcpc_detail_zz_shoucang0')"><i class="icon"></i><span>加入收藏</span></a>
                <a id="richscan" class="richscan-house pr c_888" href="javascript:;"
                    onmouseover="clickLog('from=fcpc_detail_zz_saoyisao')"><i class="icon"></i>扫一扫</a>
                <a id="gaq_phone" class="see-by-phone pr c_888" href="javascript:;"
                    onclick="clickLog('from=fcpc_detail_zz_toshouji')"><i class="icon"></i>发送到手机</a>
                <!-- 增加举报位置 -->
                <a id="report" class="report pr c_888" href="javascript:;"
                    onclick="clickLog('from=fcpc_detail_bj_report')"><i class="icon"></i>举报</a>
                <!-- 增加举报位置end -->

            </div>
            <div id="richscan-bar" class="richscan-wrap">
                <p class="code"></p>

                <p class="word">扫码获取房源信息</p>
                <i class="jianjiao icon"></i>
            </div>
            <div id="manage-bar" class="manage-wrap">
                <i class="jianjiao icon"></i>

                <a id="gaq_update" class="ab" href="javascript:;" target="_blank">修改</a>
                <a id="gaq_delete" class="ab" href="javascript:;" target="_blank">删除</a>
                <a id="gaq_refresh" class="ab" href="javascript:;" target="_blank">刷新</a>
                <a class="ab" href="https://infotopweb.union.vip.58.com/infotopnet/trytop/37775045184144/101110010"
                    target="_blank" rel="nofollow">置顶</a>
            </div>
        </div>

        <!--房源基本信息-->
        <div class="house-basic-info">
            <div class="house-basic-pic fl">
                <!-- todo 没有了原先的default样式 -->
                <div id="bigImg" class="basic-top-bigpic pr " onclick="clickLog('from=fcpc_detail_zz_tupian_datu0')"><!---->
                    <!-- 视频加1 start -->
                                        <!-- 视频加1 end -->
                                        <img id="smainPic"
                        src="//pic5.58cdn.com.cn/anjuke_58/4b5d0274a7d6f63ca8644a1e9943ba8a?w=640&h=480&crop=1">
                    <span id="sImgNu" class="leftNum pa f12">1/10</span>
                    
                    <!-- 视频加2 start -->
                                        <!-- 视频加2 end -->

                    <div class="basic-pic-load" id="loadingSmall" style="display: none;">
                        <div class="top icon"></div>
                        <div class="bottom icon"></div>
                    </div>
                </div>

                <div class="basic-pic-list pr">
                    <ul id="leftImg" class="pic-list-wrap pa">
                                                        <li id="xtu_xtu_1" class="actives"                                    data-src="//pic5.58cdn.com.cn/anjuke_58/4b5d0274a7d6f63ca8644a1e9943ba8a?w=640&h=480&crop=1">
                                    <img data-src="//pic5.58cdn.com.cn/anjuke_58/4b5d0274a7d6f63ca8644a1e9943ba8a?w=182&h=150&crop=1" src="//pic5.58cdn.com.cn/anjuke_58/4b5d0274a7d6f63ca8644a1e9943ba8a?w=182&h=150&crop=1">
                                </li>
                                                                <li id="xtu_xtu_2"                                     data-src="//pic2.58cdn.com.cn/anjuke_58/6063ed5b782d7975211ecb770dfb2e5f?w=640&h=480&crop=1">
                                    <img data-src="//pic2.58cdn.com.cn/anjuke_58/6063ed5b782d7975211ecb770dfb2e5f?w=182&h=150&crop=1" src="//pic2.58cdn.com.cn/anjuke_58/6063ed5b782d7975211ecb770dfb2e5f?w=182&h=150&crop=1">
                                </li>
                                                                <li id="xtu_xtu_3"                                     data-src="//pic2.58cdn.com.cn/anjuke_58/69c9e926ececdc59fd9bfe56fc1bb9b6?w=640&h=480&crop=1">
                                    <img data-src="//pic2.58cdn.com.cn/anjuke_58/69c9e926ececdc59fd9bfe56fc1bb9b6?w=182&h=150&crop=1" src="//pic2.58cdn.com.cn/anjuke_58/69c9e926ececdc59fd9bfe56fc1bb9b6?w=182&h=150&crop=1">
                                </li>
                                                                <li id="xtu_xtu_4"                                     data-src="//pic4.58cdn.com.cn/anjuke_58/430af9a4d9865c995ad6f03363035118?w=640&h=480&crop=1">
                                    <img data-src="//pic4.58cdn.com.cn/anjuke_58/430af9a4d9865c995ad6f03363035118?w=182&h=150&crop=1" src="//pic4.58cdn.com.cn/anjuke_58/430af9a4d9865c995ad6f03363035118?w=182&h=150&crop=1">
                                </li>
                                                                <li id="xtu_xtu_5"                                     data-src="//pic4.58cdn.com.cn/anjuke_58/d11855d5714cc61b97e1f02628a6c91b?w=640&h=480&crop=1">
                                    <img data-src="//pic4.58cdn.com.cn/anjuke_58/d11855d5714cc61b97e1f02628a6c91b?w=182&h=150&crop=1" src="//pic4.58cdn.com.cn/anjuke_58/d11855d5714cc61b97e1f02628a6c91b?w=182&h=150&crop=1">
                                </li>
                                                                <li id="xtu_xtu_6"                                     data-src="//pic3.58cdn.com.cn/anjuke_58/35cab1da3f68cd224f159caf7d72a4fa?w=640&h=480&crop=1">
                                    <img data-src="//pic3.58cdn.com.cn/anjuke_58/35cab1da3f68cd224f159caf7d72a4fa?w=182&h=150&crop=1" src="//pic3.58cdn.com.cn/anjuke_58/35cab1da3f68cd224f159caf7d72a4fa?w=182&h=150&crop=1">
                                </li>
                                                                <li id="xtu_xtu_7"                                     data-src="//pic3.58cdn.com.cn/anjuke_58/e19e9d13d88ff5e2efe9cb2c5a7de106?w=640&h=480&crop=1">
                                    <img data-src="//pic3.58cdn.com.cn/anjuke_58/e19e9d13d88ff5e2efe9cb2c5a7de106?w=182&h=150&crop=1" src="//pic3.58cdn.com.cn/anjuke_58/e19e9d13d88ff5e2efe9cb2c5a7de106?w=182&h=150&crop=1">
                                </li>
                                                                <li id="xtu_xtu_8"                                     data-src="//pic6.58cdn.com.cn/anjuke_58/ad63e90c8ad7fa2776e49803886badaa?w=640&h=480&crop=1">
                                    <img data-src="//pic6.58cdn.com.cn/anjuke_58/ad63e90c8ad7fa2776e49803886badaa?w=182&h=150&crop=1" src="//pic6.58cdn.com.cn/anjuke_58/ad63e90c8ad7fa2776e49803886badaa?w=182&h=150&crop=1">
                                </li>
                                                                <li id="xtu_xtu_9"                                     data-src="//pic6.58cdn.com.cn/anjuke_58/7b556fb9f04b52fd3060b1ed2a689d03?w=640&h=480&crop=1">
                                    <img data-src="//pic6.58cdn.com.cn/anjuke_58/7b556fb9f04b52fd3060b1ed2a689d03?w=182&h=150&crop=1" src="//pic6.58cdn.com.cn/anjuke_58/7b556fb9f04b52fd3060b1ed2a689d03?w=182&h=150&crop=1">
                                </li>
                                                                <li id="xtu_xtu_10"                                     data-src="//pic5.58cdn.com.cn/anjuke_58/1584888d2abe0584d42e250c0d359e91?w=640&h=480&crop=1">
                                    <img data-src="//pic5.58cdn.com.cn/anjuke_58/1584888d2abe0584d42e250c0d359e91?w=182&h=150&crop=1" src="//pic5.58cdn.com.cn/anjuke_58/1584888d2abe0584d42e250c0d359e91?w=182&h=150&crop=1">
                                </li>
                                                    </ul>
                    <a id="slbt" class="basic-pic-left icon pa" href="javascript:void(0);" onclick="clickLog('from=fcpc_detail_zz_tupian_last0')"></a>
                    <a id="srbt" class="basic-pic-right icon pa" href="javascript:void(0);" onclick="clickLog('from=fcpc_detail_zz_tupian_next0')"></a>
                </div>
            </div>
            <div class="house-basic-right fr">
                <div class="house-basic-desc">
                    <div class="house-desc-item fl c_333">
                        <div class="house-pay-way f16"><span class="c_ff552e"><b
                                    class="f36 strongbox">&#x9fa4;&#x9f64;&#x9ea3;&#x9ea3;</b>
                                 元/月</span>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c_333">押一付三</span>
                            <!-- 增加 start -->
                                                        <!-- 增加 end -->
                        </div>
                        <ul class="f14">
                            <li><span class="c_888 mr_15">租赁方式：</span><span>整租</span>
                            </li>
                            <li><span class="c_888 mr_15">房屋类型：</span><span
                                    class="strongbox">&#x993c;室&#x993c;厅&#x9fa4;卫&nbsp;&nbsp;&#x958f;&#x9ea3;                                    平&nbsp;&nbsp;精装修 </span>
                            </li>
                            <li><span class="c_888 mr_15">朝向楼层：</span><span class="strongbox">南&nbsp;&nbsp;低层 / &#x993c;&#x9ea3;层</span>
                            </li>
                                                        <li><span class="c_888 mr_15">所在小区：</span><span><a class="c_333 ah"
                                                                                href="https://zz.58.com/xiaoqu/biyuanyuehu/?from=zf" target="_blank"
                                        onclick="clickLog('from=fcpc_detail_zz_xiaoqu0')">碧源月湖景园</a></span>
                                                                <em class="zs c_888 f12">
                                                                        (在租 <a class="c_0091d7 ah"
                                        href="https://zz.58.com/xiaoqu/biyuanyuehu/?from=zfchuzu/"
                                        target="_blank" onclick="clickLog('from=fcpc_detail_zz_zaizu0')">
                                        1825</a>套
                                    | 在售 <a class="c_0091d7 ah"
                                        href="https://zz.58.com/xiaoqu/biyuanyuehu/?from=zfershoufang/"
                                        target="_blank" onclick="clickLog('from=fcpc_detail_zz_zaishou0')">
                                        589</a>
                                    套)
                                                                    </em>
                                                            </li>
                                                        <li><span class="c_888 mr_15">所属区域：</span><span>
                                                                        <a class="c_333 ah" href="https://zz.58.com/huiji/zufang/" target="_blank"
                                        onclick="clickLog('from=fcpc_detail_zz_quyu0')">惠济</a>&nbsp;&nbsp;
                                                                        <a class="c_333 ah" href="https://zz.58.com/kaiyuanl/zufang/" target="_blank"
                                        onclick="clickLog('from=fcpc_detail_zz_shangquan0')">开元路</a>
                                                                    </span><em class="dt c_888 f12"></em>
                            </li>
                            <li >
                                <span class="c_888 mr_15">详细地址：</span>
                                <span  class="dz" >
                                    开元路                                </span>
                                <span  class="fj" >
                                    <a rel="nofollow" class="c_0091d7 ah f12" href="/job/" target="_blank"
                                        onclick="clickLog('from=fcpc_detail_zz_fujingongzuo')">附近高薪工作
                                    </a>&nbsp;&nbsp;
                                                                        <a class="c_0091d7 ah f12" id="dituNav" href="javascript:;" jumpto="ditu"
                                        onclick="clickLog('from=fcpc_detail_zz_chakanditu')">查看地图</a>
                                                                    </span>
                            </li>
                        </ul>
                    </div>

                    <div class="house-agent-info fr" id="bigCustomer">
                        <div class="agent-head-portrait pr" onclick="clickLog('from=fcpc_detail_zz_touxiang')">
                            <a href="https://houserent.58.com/landlord/center?infoId=38418522983076&brokerId=7703505&city=zz"
                                target="_blank"><img
                                    src="https://pic1.ajkimg.com/display/6f1bd407ca6ec4bdab07b3be1a2a254d/100x133.jpg">
                                <i class="icon2"></i>
                            </a>
                            <!--服务小区-->
                            <!-- todo 添加服务小区部分 -->
                                                    </div>

                        <p class="agent-name f16 pr"><a class="c_000"
                                href="https://houserent.58.com/landlord/center?infoId=38418522983076&brokerId=7703505&city=zz"
                                target="_blank" title="点击查看ta的信用"
                                onclick="clickLog('from=fcpc_detail_zz_xingming')">李妮旦(经纪人)</a>
                                                            <i class="icon pho-approve" title="手机已认证"></i>
                                                                                        <i class="icon single-approve" title="身份证已认证"></i>
                                                                                                            </p>
                                                <p class="agent-subgroup f12">郑州创佳房地产营销策划有限公司第十五分公司                                                        <i class="icon" title="58同城商家认证">1年</i>
                                                    </p>

                        <div class="business-wrap">
                            <span class="business-wrap-span">
                                <p class="agent-store f12">
                                    <a class="ah"
                                        href="https://houserent.58.com/landlord/center?infoId=38418522983076&brokerId=7703505&city=zz"
                                        target="_blank"
                                        onclick="clickLog('from=fcpc_detail_zz_jingjiren_jinrudianpu')">进入店铺</a>&nbsp;&nbsp;
                                    <a class="ah"
                                        href="https://houserent.58.com/landlord/center?infoId=38418522983076&brokerId=7703505&city=zz"
                                        target="_blank"
                                        onclick="clickLog('from=fcpc_detail_zz_jingjiren_xinyongjilu')">他的信用记录</a>
                                </p>
                            </span>
                        </div>
                        
                        
                        <!--<div class="agent-chat">
                        <a class="bangbang-chat icon im-chat" data-im="" href="javascript:;"></a>
                        <a id="qqChatBtn" class="qq-chat icon" href="javascript:;" target="_blank"
                           onclick="clickLog('from=fcpc_detail__QQ')"></a>
                    </div>-->


                    </div>
                    <!--end-->
                </div>

                <div class="house-fraud-tip clear">
                    <!-- 更新日期超过90天隐藏电话联系和微聊 2018.01.13 -->
                                            <div class="house-chat-phonenum">
                            <p class="phone-logo"><i class="phone-icon"></i></p>
                            <p class="chat-phone-layer show-phone" onclick="clickLog('from=fcpc_detail_zf_zz_call');this.style.display='none'">电话联系TA</p>
                            <p class="phone-num strongbox">&#x9fa4;&#x9f64;&#x9fa4;&#x9ea3;&#x9a4b;&#x9f64;&#x958f;&#x9e3a;&#x9f64;&#x9fa4;&#x9fa4;</p>
                            <p class="phone-belong"></p>
                        </div>
                                            <span class="house-chat-im im-chat"
                              data-im="%7B%22rootcateid%22%3A1%2C%22cateid%22%3A8%2C%22userid%22%3A54844713088787%2C%22postid%22%3A38418522983076%7D"
                              onclick="clickLog('from=pc_detail_im_fc_zf_click')">
                        <i class="im-icon"></i>微聊
                        </span>
                    
                    <!--
                <span class="frand-remarks pr f12">签约前切勿付
                      <i class="c_ff552e">订金、押金、 <br/>租金</i>等一切费用！务必
                      <i class="c_ff552e">实地<br/> 看房</i>，查验房东和房屋证件！
                      <em id="report" class="frand-logo pa f12 c_ff552e"><i class="icon"></i>举报</em>
                </span>
                -->
                    <span class="wx-wrap">
                        <i>扫一扫，微信咨询</i>
                    </span>

                    <div id="report-bar" class="report-column pr">
                        <i class="jianjiao icon"></i>

                        <a class="ab" href="https://about.58.com/info/deleteinfo.aspx" target="_blank"
                           onclick="clickLog('from=fcpc_detail_zz_jubao_dianhuamy')">电话被冒用</a>
                        <a class="ab"
                           href="https://rentercenter.58.com/report/detail_app?infoId=38418522983076&terminal=0&cateId=8"
                           onclick="clickLog('from=fcpc_detail_zz_jubao_xxxujia')" target="_blank">信息虚假</a>
                        <a class="ab" href="https://110.58.com/?postId=38418522983076&category=1001"
                           onclick="clickLog('from=fcpc_detail_zz_jubao_baoan')" target="_blank">我要报案</a>
                    </div>

                </div>
            </div>
            <br class="clear" />
        </div>

        <!--房源描述-->
        <div class="house-detail-desc">
            <!--主要描述-->
            <div class="main-detail-info">

                <ul class="nav-detail-bar">
                    <li class="on" onclick="clickLog('from=fcpc_detail_zz_fymiaoshu')">
                        <a id="housedetailNav" href="javascript:;" jumpto="housedetailNav">房源详情</a></li>
                                        <li onclick="clickLog('from=fcpc_detail_zz_xiaoquxq0')">
                        <a id="districtNav" href="javascript:;" jumpto="district-wrap">小区详情</a>
                    </li>
                                    </ul>
                                <div class="report-text">
                    签约前切勿付
                    <span class="color">订金、押金、租金</span>
                    等一切费用！务必
                    <span class="color">实地看房，</span>
                    查验房东和房屋证件！
                </div>

                <!--房屋配置-->
                                <ul class="house-disposal">
                                                <li class="bed"><i class="icon"></i>床</li>
                                                    <li class="chest"><i class="icon"></i>衣柜</li>
                                                    <li class="sofa"><i class="icon"></i>沙发</li>
                                                    <li class="telev"><i class="icon"></i>电视</li>
                                                    <li class="icebox"><i class="icon"></i>冰箱</li>
                                                    <li class="washer"><i class="icon"></i>洗衣机</li>
                                                    <li class="air-condition"><i class="icon"></i>空调</li>
                                                    <li class="water-heater"><i class="icon"></i>热水器</li>
                                                    <li class="broadband"><i class="icon"></i>宽带</li>
                                                    <li class="central-heater"><i class="icon"></i>暖气</li>
                                                    <li class="fuel-gas"><i class="icon"></i>可做饭</li>
                                                    <li class="balcony"><i class="icon"></i>阳台</li>
                                                    <li class="toilet"><i class="icon"></i>独立卫生间</li>
                                        </ul>
                                <div class="house-word-introduce f16 c_555">
                    <!-- 增加 start -->
                    <ul class='introduce-item'>
                                                <li><span class='a1'>房屋亮点</span>
                            <span class='a2'>
                                                                      <em>配套齐全</em>
                                                                      <em>精装修</em>
                                                             </span></li>
                                                <li>
                            <span class='a1'>房源描述</span>
                            <span class='a2'><p >	<span ><strong>诚心出租此房屋，看房质量不要看报的价格，根据房子质量给出你心目中合理的价格；</strong></span></p><p >	<span ><strong>1、我的房子地理位置非常好，</strong></span></p><p >	<span ><strong>2、交通便利，附近公交很方便，地铁、公交也有，上班的话，节约了您的步行时间，在郑州四通发达；</strong></span></p><p >	<span ><strong>3、购物方便，附近大中型超市、医院 学校 都有，您可以买日常所必须，买菜也很方便，周围配套应有尽有</strong></span></p><p >	<span ><strong>4、小区环境好，管理成熟区内有物业部门实行专业管理，管理有序规范房源价值房子价格在周边以及同等房间，房子价格便宜合适，超值.</strong></span></p></span>
                        </li>
                    </ul>
                    <!-- 增加 end -->
                </div>
                <!--房屋图集-->
                <ul class="house-pic-list " id="housePicList">
                                                <li data-index="0" class="pic even"
                                onclick="clickLog('from=fcpc_detail_zz_fyms_tupian_no1')">
                                <img lazy_src="https://pic5.58cdn.com.cn/anjuke_58/4b5d0274a7d6f63ca8644a1e9943ba8a?w=696&h=522&crop=1">
                            </li>
                                                        <li data-index="1" class="pic"
                                onclick="clickLog('from=fcpc_detail_zz_fyms_tupian_no2')">
                                <img lazy_src="https://pic2.58cdn.com.cn/anjuke_58/6063ed5b782d7975211ecb770dfb2e5f?w=696&h=522&crop=1">
                            </li>
                                                        <li data-index="2" class="pic even"
                                onclick="clickLog('from=fcpc_detail_zz_fyms_tupian_no3')">
                                <img lazy_src="https://pic2.58cdn.com.cn/anjuke_58/69c9e926ececdc59fd9bfe56fc1bb9b6?w=696&h=522&crop=1">
                            </li>
                                                        <li data-index="3" class="pic"
                                onclick="clickLog('from=fcpc_detail_zz_fyms_tupian_no4')">
                                <img lazy_src="https://pic4.58cdn.com.cn/anjuke_58/430af9a4d9865c995ad6f03363035118?w=696&h=522&crop=1">
                            </li>
                                                        <li data-index="4" class="pic even"
                                onclick="clickLog('from=fcpc_detail_zz_fyms_tupian_no5')">
                                <img lazy_src="https://pic4.58cdn.com.cn/anjuke_58/d11855d5714cc61b97e1f02628a6c91b?w=696&h=522&crop=1">
                            </li>
                                                        <li data-index="5" class="pic"
                                onclick="clickLog('from=fcpc_detail_zz_fyms_tupian_no6')">
                                <img lazy_src="https://pic3.58cdn.com.cn/anjuke_58/35cab1da3f68cd224f159caf7d72a4fa?w=696&h=522&crop=1">
                            </li>
                                                        <li data-index="6" class="pic even hide"
                                onclick="clickLog('from=fcpc_detail_zz_fyms_tupian_no7')">
                                <img lazy_src="https://pic3.58cdn.com.cn/anjuke_58/e19e9d13d88ff5e2efe9cb2c5a7de106?w=696&h=522&crop=1">
                            </li>
                                                        <li data-index="7" class="pic hide"
                                onclick="clickLog('from=fcpc_detail_zz_fyms_tupian_no8')">
                                <img lazy_src="https://pic6.58cdn.com.cn/anjuke_58/ad63e90c8ad7fa2776e49803886badaa?w=696&h=522&crop=1">
                            </li>
                                                        <li data-index="8" class="pic even hide"
                                onclick="clickLog('from=fcpc_detail_zz_fyms_tupian_no9')">
                                <img lazy_src="https://pic6.58cdn.com.cn/anjuke_58/7b556fb9f04b52fd3060b1ed2a689d03?w=696&h=522&crop=1">
                            </li>
                                                        <li data-index="9" class="pic hide"
                                onclick="clickLog('from=fcpc_detail_zz_fyms_tupian_no10')">
                                <img lazy_src="https://pic5.58cdn.com.cn/anjuke_58/1584888d2abe0584d42e250c0d359e91?w=696&h=522&crop=1">
                            </li>
                                                        <li class="view-more-pic view-more" id="viewMorePic">
                                <a href="javascript:;" onclick="clickLog('from=fcpc_detail_zz_fyms_tupian_chakanqb')">查看全部图片（10张）</a>
                            </li>
                                        </ul>

                <!--小区简介-->
                                <div id="district-wrap" class="district-info-header">
                    <div class="district-pic fl">
                        <a  href="//zz.58.com/xiaoqu/biyuanyuehu/?from=zf"                                 target="_blank" onclick="clickLog('from=fcpc_detail_zz_xiaoquxq_huanjing')">
                            <img src="https://img.58cdn.com.cn/ui8/house/detail/images/defaultDisPic.png?w=140&h=140&crop=1"
                                 alt="小区">
                        </a>
                    </div>
                    <div class="district-decs fl">
                                                <p class="title f18">
                            <a class="c_333 ah rjj" \
                                                              href="//zz.58.com/xiaoqu/biyuanyuehu/?from=zf"
                                                              target="_blank" onclick="clickLog('from=fcpc_detail_zz_xiaoquxq_xiaoqu')">小区:
                                碧源月湖景园<i class="icon"></i></a>
                        </p>
                                                                        <p class="addr c_555 f14">小区地址：开元路 </p>
                                                                        <a class="trend c_0091d7 f14 pr ah" href="https://zz.58.com/fangjia/biyuanyuehu/"
                           target="_blank" onclick="clickLog('from=fcpc_detail_zz_xiaoquxq_fangzu')"><i
                                    class="icon"></i>房租走势</a>
                                            </div>
                    <div class="district-online-sale fr c_888 f14">
                                                <a class="c_888 ab" href="https://zz.58.com/xiaoqu/biyuanyuehu/?from=zfchuzu/"
                           target="_blank" onclick="clickLog('from=fcpc_detail_zz_xiaoquxq_zaizu0')">
                            <em class="c_333 f24 lh50">1825</em>
                            <em>在租房源</em>
                        </a>
                                                                        <a class="c_888 ab" href="https://zz.58.com/xiaoqu/biyuanyuehu/?from=zfershoufang"
                           target="_blank" onclick="clickLog('from=fcpc_detail_zz_xiaoquxq_zaishou0')">
                            <em class="c_333 f24 lh50">589</em>
                            <em>在售二手房</em>
                        </a>
                                            </div>
                </div>

                <ul class="district-info-list c_333 f14 lh28">
                                        <li>
                        <span class="c_888 mr_15">建筑年代：</span><span>2017</span>
                    </li>
                                        <li>
                        <span class="c_888 mr_15">建筑类型：</span><span>小高层|超高层</span>
                    </li>
                                        <li>
                        <span class="c_888 mr_15">物业公司：</span><span>深圳市彩生活服务集团有限公司</span>
                    </li>
                                        <li>
                        <span class="c_888 mr_15">物业费用：</span><span>0.00元/平米/月</span>
                    </li>
                                        <li>
                        <span class="c_888 mr_15">所属商圈：</span>
                        <span>
                            <a class="c_333 ah" href="https://zz.58.com/xiaoqu/5518/" traget="_blank" onclick="clickLog('from=fcpc_detail_zz_xiaoquxq_quyu0')">惠济</a>&nbsp;/&nbsp;
                            <a class="c_333 ah" href="https://zz.58.com/xiaoqu/12657/" traget="_blank" onclick="clickLog('from=fcpc_detail_zz_xiaoquxq_shangquan0')">开元路</a>
                        </span>
                    </li>
                                    </ul>
                                <!--地图街景-->

                <div id="ditu">

                    <div id="dtjt_wrap" class="mb15">
                        <div id="dtjt_title">
                            <span id="baidu_tab" class="active"
                                  onclick="clickLog('from=fcpc_detail_zz_xiaoquxq_xqditu')">小区地图&nbsp;</span>
                            <span>/</span>
                            <span id="soso_tab"
                                  onclick="clickLog('from=fcpc_detail_zz_xiaoquxq_xqjiejing')">&nbsp;小区街景</span>
                        </div>
                        <div id="baidu_map" class="map active">
                            <div id="dtjt_info">
                                <div id="map"></div>
                                <div id="map_tab_jtlx" class="map_tab map_tab_sel"></div>
                            </div>
                        </div>
                        <div id="soso_map" class="map">
                            <div id="static_map_background"></div>
                            <div id="static_map"></div>
                            <div id="map_drag"></div>
                        </div>
                                                <div class="view-more-detailmap view-more">
                            <a href="https://api.map.baidu.com/marker?location=34.878822,113.639258&title=碧源月湖景园&content=开元路&output=html&src=58.com"
                               target="_blank" onclick="clickLog('from=fcpc_detail_zz_xiaoquxq_ditu_xiangxi')">地图详情
                                <i class="icon"></i>
                            </a>
                        </div>
                                            </div>
                </div>


                <!--猜你喜欢-->
                <!-- <div id="guessYourLike">
                </div> -->

                <div id="guess-your-like" class="guess-your-like">

                </div>

                <!--猜您需要的 -->
                <div class="guess-your-service">
                    <p class="f18 c_333">相关服务</p>

                    <div class="service-list">
                        <a rel="nofollow" class="move-house first" href="https://zz.58.com/banjia/" target="_blank"
                           onclick="clickLog('from=fcpc_detail_zz_fuwu_banjia')">
                            <p class="f18 c_333 lh44 rjj">搬家服务<i class="icon"></i></p>

                            <p class="f14 c_555 lh20">行李太多搬不动？<br />专业人员来帮忙</p>
                        </a>
                        <a rel="nofollow" class="keep-clean" href="https://zz.58.com/baojie/" target="_blank"
                           onclick="clickLog('from=fcpc_detail_zz_fuwu_baojie')">
                            <p class="f18 c_333 lh44 rjj">保洁服务<i class="icon"></i></p>

                            <P class="f14 c_555 lh20">健康卫生无小事<br />保洁服务一条龙</P>
                        </a>
                    </div>
                </div>

                <!--大家都在看-->
                <div id="see-again-house"  class="see-again-house">

                </div>

                <!--土巴兔底部广告-->
                <div id="tbt-bottom-ad" class="tbt_bottom_ad"></div>
                <!--精选底部广告-->
                <div id="jx_bottom_ad" class="jx_bottom_ad"></div>
                <!--其他底部广告-->
                <div id="googlead_list"></div>

            </div>
            <!--右侧推荐及广告-->
            <div class="side-right-info fr">
                <div id="agent-other-house" class="agent-other-house">

                </div>

                <!-- <div id="superApartment">
                </div> -->

                <div id="premium-brand-apartment" class="premium-brand-apartment">
                </div>


                <!--右侧精选广告-->
                <div id="jx_right_ad" class="jx_right_ad"></div>
                <!--右侧其他广告位-->
                <div id="sideAD"></div>
                <!--土巴兔广告位-->
                <div id="tbt-right-ad" class="tbt-right-ad"></div>


            </div>
        </div>

        <!--其他推荐-->
        <div class="other-series-recommend">
            <ul class="other-series-nav f14 c_888" id="rec-bottom-nav">
                <li data-key="0" class="on">热门搜索</li>
                <li data-key="1">相关推荐</li>
                <li data-key="2">郑州租房相关</li>
            </ul>
            <ul class="other-detail-introduce f12 c_888" id="rec-bottom-list">
                                <li data-key="0" class="on">
                                                <a href="https://zz.58.com/zufang/jh_%E4%B9%90%E6%88%90%E5%B0%8F%E5%8C%BA/" target="_blank">乐成小区</a>
                                                    <a href="https://zz.58.com/zufang/jh_%E5%B9%B8%E7%A6%8F%E6%B1%87/" target="_blank">幸福汇</a>
                                                    <a href="https://zz.58.com/zufang/jh_%E6%96%B0%E5%8D%8E%E5%B0%8F%E5%8C%BA%E5%87%BA%E7%A7%9F/" target="_blank">新华小区出租</a>
                                                    <a href="https://zz.58.com/zufang/jh_%E4%B8%8A%E7%8F%AD%E6%97%8F%E7%A7%9F%E6%88%BF/" target="_blank">上班族租房</a>
                                                    <a href="https://zz.58.com/zufang/jh_%E7%B2%BE%E8%A3%85%E6%88%BF%E6%BA%90/" target="_blank">精装房源</a>
                                                    <a href="https://zz.58.com/zufang/jh_%E5%8D%8A%E5%B2%9B%E5%85%AC%E5%AF%93/" target="_blank">半岛公寓</a>
                                                    <a href="https://zz.58.com/zufang/jh_%E6%89%BE%E7%A7%9F%E6%88%BF/" target="_blank">找租房</a>
                                        </li>
                                                        <li data-key="1">
                                                                <a href="https://zhengzhou.anjuke.com/community/view/227797" target="_blank">华林都市家园</a>
                                                                    <a href="https://zhengzhou.anjuke.com/community/view/227860" target="_blank">富田太阳城</a>
                                                                    <a href="https://zhengzhou.anjuke.com/community/view/833208" target="_blank">曼哈顿广场</a>
                                                                    <a href="https://zhengzhou.anjuke.com/community/view/1082115" target="_blank">融信江湾城</a>
                                                                    <a href="https://zhengzhou.anjuke.com/community/view/779023" target="_blank">汇泉西悦城</a>
                                                                    <a href="https://zhengzhou.anjuke.com/community/view/832092" target="_blank">瀚宇天悦湾</a>
                                                                    <a href="https://zhengzhou.anjuke.com/community/view/227391" target="_blank">恒大绿洲</a>
                                                                    <a href="https://zhengzhou.anjuke.com/community/view/227170" target="_blank">亚星盛世家园</a>
                                                                    <a href="https://zhengzhou.anjuke.com/community/view/860790" target="_blank">东润城</a>
                                                                    <a href="https://zhengzhou.anjuke.com/community/view/1106211" target="_blank">玉兰先禾(商住楼)</a>
                                                                    <a href="https://www.anjuke.com/zhengzhou/cm371987-zu/" target="_blank">鑫苑世家</a>
                                                                    <a href="https://www.anjuke.com/zhengzhou/cm227411-zu/" target="_blank">汉飞金沙国际</a>
                                                                    <a href="https://www.anjuke.com/zhengzhou/cm832703-zu/" target="_blank">金林公馆</a>
                                                                    <a href="https://www.anjuke.com/zhengzhou/cm249702-zu/" target="_blank">中豪汇景湾</a>
                                                                    <a href="https://www.anjuke.com/zhengzhou/cm880298-zu/" target="_blank">聂庄棚户区</a>
                                                                    <a href="https://www.anjuke.com/zhengzhou/cm227737-zu/" target="_blank">名门盛世</a>
                                                                    <a href="https://www.anjuke.com/zhengzhou/cm517769-zu/" target="_blank">盛润锦绣城</a>
                                                                    <a href="https://www.anjuke.com/zhengzhou/cm266252-zu/" target="_blank">正弘数码公寓</a>
                                                                    <a href="https://www.anjuke.com/zhengzhou/cm861011-zu/" target="_blank">升龙凤凰城A区</a>
                                                                    <a href="https://www.anjuke.com/zhengzhou/cm227544-zu/" target="_blank">正商东方港湾</a>
                                                        </li>
                                            <li data-key="2">
                                                    </li>
                                            <li data-key="3">
                                                    </li>
                                </ul>
        </div>
    </div>

    <!-- 大图模式 -->
    <div class="piclayer"></div>
    <div class="picmask">
        <div class="big-top-bigpic pr">
            <img id="mainPic" src="">
            <!-- 模板：新添加位置 -->
            <div class="big-pic-load" id="loadingBig">
                <div class="top icon"></div>
                <div class="bottom icon"></div>
            </div>
        </div>
        <div class="big-pic-list pr">
            <ul id="smallPic" class="bigpic-list-wrap pa">
                                        <li id="tu_1"  class="actives"                             data-src="//pic5.58cdn.com.cn/anjuke_58/4b5d0274a7d6f63ca8644a1e9943ba8a">
                            <img src="https://pic5.58cdn.com.cn/anjuke_58/4b5d0274a7d6f63ca8644a1e9943ba8a">
                        </li>
                                            <li id="tu_2"                             data-src="//pic2.58cdn.com.cn/anjuke_58/6063ed5b782d7975211ecb770dfb2e5f">
                            <img src="https://pic2.58cdn.com.cn/anjuke_58/6063ed5b782d7975211ecb770dfb2e5f">
                        </li>
                                            <li id="tu_3"                             data-src="//pic2.58cdn.com.cn/anjuke_58/69c9e926ececdc59fd9bfe56fc1bb9b6">
                            <img src="https://pic2.58cdn.com.cn/anjuke_58/69c9e926ececdc59fd9bfe56fc1bb9b6">
                        </li>
                                            <li id="tu_4"                             data-src="//pic4.58cdn.com.cn/anjuke_58/430af9a4d9865c995ad6f03363035118">
                            <img src="https://pic4.58cdn.com.cn/anjuke_58/430af9a4d9865c995ad6f03363035118">
                        </li>
                                            <li id="tu_5"                             data-src="//pic4.58cdn.com.cn/anjuke_58/d11855d5714cc61b97e1f02628a6c91b">
                            <img src="https://pic4.58cdn.com.cn/anjuke_58/d11855d5714cc61b97e1f02628a6c91b">
                        </li>
                                            <li id="tu_6"                             data-src="//pic3.58cdn.com.cn/anjuke_58/35cab1da3f68cd224f159caf7d72a4fa">
                            <img src="https://pic3.58cdn.com.cn/anjuke_58/35cab1da3f68cd224f159caf7d72a4fa">
                        </li>
                                            <li id="tu_7"                             data-src="//pic3.58cdn.com.cn/anjuke_58/e19e9d13d88ff5e2efe9cb2c5a7de106">
                            <img src="https://pic3.58cdn.com.cn/anjuke_58/e19e9d13d88ff5e2efe9cb2c5a7de106">
                        </li>
                                            <li id="tu_8"                             data-src="//pic6.58cdn.com.cn/anjuke_58/ad63e90c8ad7fa2776e49803886badaa">
                            <img src="https://pic6.58cdn.com.cn/anjuke_58/ad63e90c8ad7fa2776e49803886badaa">
                        </li>
                                            <li id="tu_9"                             data-src="//pic6.58cdn.com.cn/anjuke_58/7b556fb9f04b52fd3060b1ed2a689d03">
                            <img src="https://pic6.58cdn.com.cn/anjuke_58/7b556fb9f04b52fd3060b1ed2a689d03">
                        </li>
                                            <li id="tu_10"                             data-src="//pic5.58cdn.com.cn/anjuke_58/1584888d2abe0584d42e250c0d359e91">
                            <img src="https://pic5.58cdn.com.cn/anjuke_58/1584888d2abe0584d42e250c0d359e91">
                        </li>
                                </ul>
        </div>
        <div id="viewNum" class="big-pic-leftnum pa f12">4/6</div>
        <a id="blbt" class="big-pic-left pa" href="javascript:void(0);" onclick="clickLog('from=fcpc_detail_zz_tupian_last')"><!---->
            <i class="icon"></i>
        </a>
        <a id="brbt" class="big-pic-right pa" href="javascript:void(0);" onclick="clickLog('from=fcpc_detail_zz_tupian_next')"> <!---->
            <i class="icon"></i>
        </a>

        <div class="picclose icon"></div>

    </div>

    <!-- 防诈骗 -->
    <div class="defraud-layer"></div>

    <!--底部footer-->
    <div id="commonFooter" class="commonFooter"></div>

    <!-- 加载地图js 后期可以根据组件抽离-->
    <script charset="utf-8"
            src="https://map.qq.com/api/js?v=2.exp&key=d84d6d83e0e51e481e50454ccbe8986b&libraries=convertor">
    </script>

    <!--1.新增：页面主js-->
    <script type="text/javascript" charset="utf-8" src="//j1.58cdn.com.cn/frs/fangfe/zufang-pc-site/1.0/zf-detail/index_v20190614211142.js"></script>

    <!--2.加载公共组件：header、footer-->
    <script type="text/javascript">
        window.wbAsyncInit = function wbAsyncInit(CL) {
            CL.invoke('topbar', {
                aroundCity: false,
                weather: false,
                appQR: true, // homepage QR
                homepageLink: true,
                size: 'default' // default: 1190px, narrow: 1000px
            });
            /**
             * 统一收藏弹窗 顶部 + 右侧
             */
            CL.invoke('popcollection', {
                clickBtn: $('.clt-btn'),
                source: "passport",
                infoid: ____json4fe.infoid,
                cateid: ____json4fe.catentry && ____json4fe.catentry.dispid || '',
                callback: function () {
                    $.fn.collectHouse();
                }
            });

            CL.invoke("footer");
        };
    </script>
    <script src="//j1.58cdn.com.cn/componentsLoader/dist/ComponentsLoader_v20190402152128.js"></script>


    <!-- 3.孙悟空引入的js -->
    <!--
    <script src="//j1.58cdn.com.cn/ui6/my/js/swkWidgetPc_v20170307175855.js"></script>
    -->


    <!--4.微聊-->
    <script type="text/javascript" defer src="https://j1.58cdn.com.cn/webim/js/entry_v20181119152007.js"></script>

        <script src="//adshow.58.com/js/ssp_init.js"></script>
    <script type="text/javascript" src="//j1.58cdn.com.cn/crop/ecom/m/tcb/ideaShow/main_v20180917142647.js"></script>

    <!-- 不清楚什么条件下存在???和后端同学确认 -->
    <script>
        /*//加置顶购买入口
        var tgbanner = {};
        require(['common/tg_banner'], function (obj) {
            tgbanner = obj;
            tgbanner.init();
        });*/
    </script>

    <!-- 5.limitbutton -->
    <!--
    <script src="//j1.58cdn.com.cn/ui7/js/limitbutton.js?20160111"></script>
    <script>
        $(function () {
            clickLog('expview-ZUFANG_103_1691715904'); //这个是已有的统计代码
            window.limitButton = new LimitButton({
                button: $('#postBtn')
            }); //这三行是新增的
        });
    </script>
    -->

    <!--6.推荐广告-->
    <script type="text/javascript" src="https://j1.58cdn.com.cn/crop/ecom/m/tcb/ideaShow/main_v20180917142647.js"></script>

</body>
</html>

"""

obj = BeautifulSoup(html_str,'lxml')
print(obj, type(obj))
# 获取标签对象
print(obj.title)
# 获取标签的名字
print(obj.title.name)
# 获取标签的内容
print(obj.title.text)
print(obj.title.string)
# print(obj.title.parent)
print(obj.title.parent.name)
# 获取页面的第一个p
print(obj.p)
print(obj.p['class'])
# 获取所有p
# print(obj.find_all('p'))
# print(obj.find(id="title"))
# 根据标签的id查找标签
print(obj.find(id="title"))

# print(obj.find_all('a'))
div_obj = obj.find(id="leftImg")
# 从div中获取所有的img
print(div_obj.find_all('img'))
for img in div_obj.find_all('img'):
    print(img.get('src'))

div_obj = obj.find(id="bigCustomer")
# 获取所有的文本
print(div_obj.get_text())
print(div_obj)
# 获取当前标签下的子标签
# print(div_obj.contents)

# 获取父标签
print(obj.title.parent, obj.title.parent.name)

# 获取同级元素的上上个
print(obj.p.previous_sibling.previous_sibling)
print(obj.p)
# 获取同级元素的下下个
print(obj.p.next_sibling.next_sibling)

# 通css查找标签
print(obj.select('title'))
print(obj.select('h1'))
print(obj.select_one('h1'))
print(obj.select('.house-desc-item'))
print(obj.select('#adfad'))

