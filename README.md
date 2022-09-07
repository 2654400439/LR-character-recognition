# LR-character-recognition
Low resolution character recognition for specific DouYin id recognition task  
本项目实现一个低分辨率文字识别的工作，主要面向[字节跳动2022安全AI挑战赛初赛](https://security.bytedance.com/fe/2022/ai-challenge#/challenge)初赛题目一（低分辨率抖音号识别）  
本项目的代码实现具有一定的针对性，但是通过简单的修改就可以迁移到通用的低分辨率文字识别工作中  
<br><br>
### 题目描述
抖音APP中的抖音号水印是识别视频搬运的重要依据，很多黑灰产、搬运用户等会给搬运的视频进行低分辨率处理，以逃避搬运审核。我们希望选手能够根据低分辨率图像识别出该视频中包含的抖音号。  
### 题目数据
训练数据包括原始投稿图像以及抖音号（抖音号为随机生成非真实用户）。  
测试数据包括低分辨率投稿图像。  
<br>
如下图，抖音号为：6xdRyPM5TS  
![image](https://lf-cdn-tos.bytescm.com/obj/static/security/src/static/douyu-frame-example_0da1dc04.png)  
<br>
### 设计思路
由于训练集是高清图片而测试集是经过多次转发保存后的低分辨率图片，因此本赛题在AI模型训练阶段需要注意存在明显的概念偏移问题（训练集和测试集数据分布不一致）。为解决上述问题，本项目采用测试集低分辨率变“清晰”+训练集高清变模糊，双管齐下的方式来规避概念偏移。  
项目分为*数据预处理模块*、*抖音号字段分割模块*、*超分辨率模块*（FFDNet, [参考实现](https://github.com/cszn/KAIR)）和*文字识别模块*（CRNN, [参考实现](https://github.com/clovaai/deep-text-recognition-benchmark)）
<br>
#### 数据预处理模块（赛后上传）
对应项目中Preprocess文件夹，目前直接放面向过程编写的jupyter notebook文件了，有时间可以整理成python工程文件。（如果确实有需要可以通过issue联系我）  
-->对于训练集的数据预处理包括对每一张图片做两种数据增强（1.尺寸压缩1/2再还原，模拟测试集情况；2.增加高斯噪声），最后将每张图片的三种形式全部放入训练集供模型训练。  
-->对于测试集的数据预处理包括对每张图片通过三次插值的方法尺寸扩大到原来的一倍，在通过滤波器进一步去除噪声，最后对图片适当增加曝光使得抖音号白色字体更加方便后续处理。
<br>
#### 抖音号字段分割模块（赛后上传）
对应项目中Preprocess文件夹，目前直接放面向过程编写的jupyter notebook文件了，有时间可以整理成python工程文件。（如果确实有需要可以通过issue联系我）  
首先通过定义“抖音号”的模板，通过opencv提供的模板匹配函数在整张图片上确定出“抖音号”三个字的位置；之后通过自适应亮度的垂直投影确定抖音号右侧边界；最终根据上下左右边界将抖音号完整的抠出。
<br>
#### 超分辨率模块
通过在训练集上的训练，获得一个能针对模糊抖音号超分辨率的模型，并直接用在测试集上。具体实现参考[FFDNet](https://github.com/cszn/KAIR)。
<br>
#### 文字识别模块
通过在训练集上的训练，获得一个能针对抖音号识别的文字识别模型。具体实现参考[CRNN](https://github.com/clovaai/deep-text-recognition-benchmark)。
