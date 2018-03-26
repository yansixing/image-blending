# image-blending
Mix two images into a magical effect! <br /><br />
原理：由两张图片front layer和back layer生成，生成的图片是有alpha通道的RGBA模式（如png格式）。在网页中或预览模式图片背景色一般由白色填充，而点开放大到沉浸模式时背景色为黑色填充，因此可以推断front layer中的白色和back layer中的黑色都是由背景提供的。<br />
<br />
wiki:<a href="https://en.wikipedia.org/wiki/Alpha_compositing#Alpha_blending">Alpha_blending</a><br /><br />
Thanks to <a href = "https://blog.0xbbc.com/2016/09/magic-image-alpha-channel/">0xBBC</a>.

<img src="https://github.com/yansixing/image-blending/blob/master/img3.png" width="400px" height="300px">
