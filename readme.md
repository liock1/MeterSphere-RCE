# MeterSphere未授权RCE

## 前言

文章中涉及的工具仅供已授权的测试目标中使用，对未授权目标的测试所造成的后果均由本人自行承担。

## 界面预览

![image-20220119115513260](https://liocknote.oss-cn-chengdu.aliyuncs.com/uPic/image-20220119115513260.png)

## 漏洞检测

1、检测会上传exp，漏洞详情参考提供的参考链接

```java
public class exp2 {
	public String customMethod(String s) {return "ok"; }
}
```

2、编译后的exp.jar放置在MeterSphere未授权.py当前目录下

![image-20220119115619536](https://liocknote.oss-cn-chengdu.aliyuncs.com/uPic/image-20220119115619536.png)

## 漏洞利用

1、输入待测IP和待测端口，点击漏洞检测

![image-20220215001227842](https://liocknote.oss-cn-chengdu.aliyuncs.com/uPic/image-20220215001227842.png)

2、输入待测IP、待测端口、要执行的命令

![image-20220215001245927](https://liocknote.oss-cn-chengdu.aliyuncs.com/uPic/image-20220215001245927.png)

## EXE版本

1、EXE运行并检测漏洞

![image-20220215000650695](https://liocknote.oss-cn-chengdu.aliyuncs.com/uPic/image-20220215000650695.png)

4、EXE运行并执行命令

![image-20220215001201108](https://liocknote.oss-cn-chengdu.aliyuncs.com/uPic/image-20220215001201108.png)

## 公众号

![扫码_搜索联合传播样式-标准色版](https://liocknote.oss-cn-chengdu.aliyuncs.com/uPic/%E6%89%AB%E7%A0%81_%E6%90%9C%E7%B4%A2%E8%81%94%E5%90%88%E4%BC%A0%E6%92%AD%E6%A0%B7%E5%BC%8F-%E6%A0%87%E5%87%86%E8%89%B2%E7%89%88.png)