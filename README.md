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
