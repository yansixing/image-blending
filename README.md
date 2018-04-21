# image-blending

![](https://img.shields.io/badge/python-2.7-blue.svg)
![npm](https://img.shields.io/npm/l/express.svg)


> Mix two images into a magical effect!

> 原理：由两张图片front layer和back layer生成，生成的图片是有alpha通道的RGBA模式（如png格式）。在网页中或预览模式图片背景色一般由白色填充，而放大到沉浸模式时背景色为黑色填充，因此可以推断front layer中的白色和back layer中的黑色都是由背景提供的。<br />
> <br />
> wiki:<a href="https://en.wikipedia.org/wiki/Alpha_compositing#Alpha_blending">Alpha_blending</a><br /><br />
Thanks to <a href = "https://blog.0xbbc.com/2016/09/magic-image-alpha-channel/">0xBBC</a>.

⬇️点击图片进入沉浸模式。（Github默认的背景色是#0e0e0e，改成#000效果更好）

<img src="https://github.com/yansixing/image-blending/blob/master/0.3.png?raw=true" width="400px" height="300px">
<br />
<img src="https://github.com/yansixing/image-blending/blob/master/almost-perfect.png?raw=true" width="379px" height="512px">
