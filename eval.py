#在训练集上进行评价


import subprocess
from pathlib import Path

def main():
    measure_path=Path('./software/Linux')
    data_path=Path('./dataset/train')

    
    for dataset in data_path.iterdir():
        for measure in measure_path.iterdir():
            print(measure.name,dataset.name,'seq=01')
            res=subprocess.run([str(measure),str(dataset),'01','3'],capture_output=True, text=True)
            print(res.stdout)
            print('---------------')

            print(measure.name,dataset.name,'seq=02')
            res=subprocess.run([str(measure),str(dataset),'02','3'],capture_output=True, text=True)
            print(res.stdout)
            print('---------------')
 

if __name__ == '__main__':
    main()