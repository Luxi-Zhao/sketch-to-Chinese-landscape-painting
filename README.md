# Sketch to Chinese Landscape Painting 

This is the repository of project **Sketch to Chinese Landscape Painting**. It contains datasets, codes and pre-trained models.  

The dataset folder contains 3 datasets. The `sketch` folder contains sketch images generated by `PhotoSketch` model stored in `preparation` folder [3]. The `hed` folder contains HED edge maps [2]. The `painting` folder contains selected original paintings [1]. 

The `src` folder contains Jupyter notebooks for running training. The notebook and code in `sketch2hed` folder contain training procedure for Pix2Pix model `sketch2hed`. The `hed2paint` folder consists of notebooks about training procedure for another Pix2Pix model `hed2paint` [5]. By following the instruction from notebooks, the training can be initialized. In addition, there is folder containing the code for computing FID score [4].

The `model` folder contains our pre-trained models. Since the pre-trained models are too large to be directly uploaded, they are all zipped and split into smaller pieces. To use the pre-trained models, first run `zip -s 0 MODEL.zip --out combined_model.zip`, then run `unzip combined_model.zip`.

## References

[1]  A. Xue, “End-to-end chinese landscape painting creation using generative adversarial networks,”2020.
[2]  S. Xie and Z. Tu, “Holistically-nested edge detection,” 2015.
[3]  M. Li, Z. Lin, R. Mˇ ech, , E. Yumer, and D. Ramanan, “Photo-sketching: Inferring contourdrawings from images,”WACV, 2019.
[4]  M. Seitzer,  “pytorch-fid:  FID Score for PyTorch,”, version 0.1.1., 2020.
[5]  J.-Y. Zhu,  T. Park,  P. Isola,  and A. A. Efros,  “Unpaired image-to-image translation usingcycle-consistent adversarial networks,” inComputer Vision (ICCV), 2017 IEEE InternationalConference on, 2017.
