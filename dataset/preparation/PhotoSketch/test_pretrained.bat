@echo off

python test_pretrained.py ^
    --name pretrained ^
    --dataset_mode test_dir ^
    --dataroot .\A\ ^
    --results_dir .\results\ ^
    --checkpoints_dir .\checkpoints\ ^
    --model pix2pix ^
    --which_direction AtoB ^
    --norm batch ^
    --input_nc 3 ^
    --output_nc 1 ^
    --which_model_netG resnet_9blocks ^
    --no_dropout

pause
