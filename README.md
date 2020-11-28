# 基于PyTorch&YOLOv4的口罩佩戴检测
本项目是利用YOLOv4进行口罩佩戴检测，使用PyTorch实现。虽然现在国内疫情基本得到有效遏制，但防控仍不可过于松懈，在一些公共场合佩戴口罩还是必不可少的。

数据集来源于网络，共1200张训练集，600张口罩佩戴，600张未佩戴口罩；400张测试集，200张口罩佩戴，200张未佩戴口罩。利用YOLOv4在数据集上冻结backbone训练了25个epoch，解冻后再训练了25个epoch，测试mAP为80.75%。检测效果如下：
![test_result](test_result.png)






### 依赖库
- Python >= 3.7
- PyTorch >= 1.4.0
- opencv-python >= 4.2.0.32
- Pillow >= 7.0.0
### 训练&评估结果
![trainloss](total_loss.png)
![mAP](mAP/output/mAP.png)


