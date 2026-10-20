define(function (require) {
    var axios = require("axios");
    var marked = require("marked");
    // var Vue = require("vue");

    // 检索URL中search部分
    var urlParams = new URLSearchParams(window.location.search);
    // 检索post参数
    var post = urlParams.get("post");
    // 文章子目录
    var url = "./post/";

    if (post == null) {
        url += "0_bookmark.md";
    } else {
        // 用于展示别的文章，使用方法是后面带 post 参数，形如：
        // http://localhost:8001/?post=git_svn_sync
        url += post + ".md";
    }

    // 读取文章内容后放入容器
    async function getFileContext() {
        try {
            const response = await axios.get(url);
            var div = document.createElement("div");
            // MarkDown转换为HTML
            div.innerHTML = marked(response.data);
            document.getElementById("loading").style.display = "none";
            document.getElementById("container").append(div);
            console.log('文件内容：', response.data);
        } catch (error) {
            console.error('获取文件失败：', error);
        }
    }

    getFileContext();
});
