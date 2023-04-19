This Repo has been forked from the official yolo7 segmentation repo.

Using Yolov7 segmentation, I achieved 0.793 (MAP50) on a test data of 211 images of panoramic images of five classes.

This is the the precision-recall curve for the five different classes.

![BoxPR_curve](https://user-images.githubusercontent.com/127892363/225750299-b6499bed-daeb-4b75-bffe-604b49527ed1.png)


ALso this is some sample segmented images from the test data:

![iScreen Shoter - Google Chrome - 230419002611](https://user-images.githubusercontent.com/86482704/232967046-0c1473ba-6455-4af5-a31a-3b82cd84373b.jpg)

![iScreen Shoter - Google Chrome - 230419002643](https://user-images.githubusercontent.com/86482704/232967074-3765704c-f303-43bf-a4c3-2d4391f29a62.jpg)

![iScreen Shoter - Google Chrome - 230419002611](https://user-images.githubusercontent.com/86482704/232967095-42d17ec4-f546-4e25-8a4c-53438a7506df.jpg)



---------------------------------------------------------------------------------------------


Other Contributions:

-> Changing the Head layers of the orginal Yolo7, has significally chnaged the seg loss, as the following graph:

The new head layers can be found in a file called new_yolo7_seg.yaml.

![compare_seg_loss](https://user-images.githubusercontent.com/127892363/226108525-f5c93f60-9ba1-410e-a260-71169e7f8064.PNG)


But others parts of the loss functions are worse than the original implementation, as the following:

![compare_obj_loss](https://user-images.githubusercontent.com/127892363/226108573-d5b83a8f-fea2-4ed0-9852-a1d1cb163906.PNG)

![compare_boxLoss](https://user-images.githubusercontent.com/127892363/226108582-29fd1b1b-918b-424d-97e2-128091f69b87.PNG)


![compare_class_loss](https://user-images.githubusercontent.com/127892363/226108585-89f38726-02a7-49cb-adb0-93d673d8ff60.PNG)


*Other tuning may be needed to raise a conclusion.


-> Also other contribution is to write a simple code to target any yolo dataset and filter it based on 
   target class/ classes, this is a paid feature on roboflow if number of imgaes is more than 1000.
   Even it is very simple, its very effective and none has implemented it on the computer vision community.

   The implementation can be found in a file called choose_classes.py



--------------------------------------------------------------------------------------------



This link contain the model weights on my google drive:

https://drive.google.com/file/d/1vEoOUMVtCOK2Rk8c73ALB4-rqEBFV8qZ/view?usp=sharing
