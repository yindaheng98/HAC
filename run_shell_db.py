import os

for lmbda in [0.004]:  # Optionally, you can try: 0.003, 0.002, 0.001, 0.0005
    for cuda, scene in enumerate([
        'coffee_martini/frame1',
        'cook_spinach/frame1',
        'cut_roasted_beef/frame1',
        'flame_salmon_1/frame1',
        'flame_steak/frame1',
        'sear_steak/frame1',
    ]):
        one_cmd = f'python train.py -s data/{scene} --eval --lod 0 --voxel_size 0.005 --update_init_factor 16 --iterations 30_000 -m outputs/{scene}/{lmbda} --lmbda {lmbda}'
        os.system(one_cmd)
