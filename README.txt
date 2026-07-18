白云区城管智能人力画像系统 · 对外部署包

最简单的启动方式
1. 确认电脑已安装 Python 3。
2. 双击 start_mac.command（macOS）或 start_windows.bat（Windows）。
3. 浏览器打开：http://127.0.0.1:8788/dual-demo/

服务器部署
- 用 Nginx、Apache 或其他静态文件服务器，将本目录作为网站根目录。
- 保留 dual-demo 文件夹，不要只复制其中的 assets 文件夹。
- 外部访问地址格式：http://服务器IP:8788/dual-demo/

说明
- 这是可直接运行的静态构建包，不需要 Node.js、npm 或源码目录。
- 页面中的 Tailwind 样式和部分头像资源使用外部 CDN，访问端需要能连接互联网。
