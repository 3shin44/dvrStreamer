# dvrStreamer

## 需求

辨識監控影像中的訪客（人型物體），產生截圖便於後續查找訪客紀錄

## 功能分析

- 以OpenCV: full-body detection分析影像

## 實測結果

精確度不佳，辨識不到或錯認。

以範例影片為例，辨識到非人型物體，畫面中有其他人並未辨識到：

![image](./snapshot/snapshot_2.jpg)
![image](./snapshot/snapshot_32.jpg)

## 討論

- 精確度問題：找尋其他解決方案，以辨識影像中是否出現訪客

- 運作環境：Raspberry pi, 一般家用監視器影像

## 測試資料來源

- Video: https://www.youtube.com/watch?v=llZxhGBiNeY

## 其他方案討論

- 其他模型: 使用過OpenCV:Face Detection, YOLO v4 (You Only Look Once), 效果不佳或安裝問題未能使用