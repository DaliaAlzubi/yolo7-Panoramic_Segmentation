import argparse
import os, glob, cv2
import numbers
# names=['1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '3', '30', '31', '32', '3M ESPE Implant', '4', '5', '6', '7', '8', '9', 'AGS Medikal Implant', 'AMerOss Implant', 'Amalgam filling', 'Anthogyr Implant', 'Bicon Implant', 'BioHorizons Implant', 'BioLife Implant', 'Biomet 3i Implant', 'Blue Sky Bio Implant', 'Camlog Implant', 'Caries', 'Composite filling', 'Cowellmedi Implant', 'Crown', 'DENTSPLY Implant', 'Dentatus Implant', 'Dentis Implant', 'Dentium Implant', 'Euroteknika Implant', 'Filling', 'Frontier Implant', 'Hiossen Implant', 'Implant Direct', 'Implant', 'Keystone Dental Implant', 'Leone Implant', 'MIS Implant', 'Mandible', 'Maxilla', 'Megagen Implant', 'Neodent Implant', 'Neoss Implant', 'Nobel Biocare Implant', 'Novodent Implant', 'NucleOSS Implant', 'OCO Biomedical Implant', 'OsseoLink Implant', 'Osstem Implant', 'Prefabricated metal post', 'Retained root', 'Root canal filling', 'Root canal obturation', 'Sterngold Implant', 'Straumann Implant', 'Titan Implant Implant', 'Zimmer Implant']
# #names = ['1', 'cardmage', 'headlight damage', 'mild damage', 'scratch']
# print(names.index('Root canal filling'))
def main(args):
    index = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25','27', '28', '29', '30', '31', '32','52','73']
    images_path = os.path.join(args.folder, "images")
    labels_path = os.path.join(args.folder, "labels")
    new_images_path = os.path.join(args.folder, "new_images")
    new_labels_path = os.path.join(args.folder, "new_labels")
    if not os.path.exists(new_images_path):
        os.makedirs(new_images_path)
    if not os.path.exists(new_labels_path):
        os.makedirs(new_labels_path)

    for file in glob.glob(os.path.join(labels_path, '*.txt')):
        new_file_path = new_labels_path + '/' + file.rsplit('/', 1)[-1]
        allDamages = []
        with open(file,'r') as f2:
            lines2 = f2.readlines() 
        for line in lines2: 
            line = line.split(' ')
            allDamages.append(line)

        s = ''
        for line in allDamages:
            if line[0] in index:
                # new_file_path = new_labels_path + '/' + file.rsplit('/', 1)[-1]
                
                for d in line:
                    s+=d
                    if d!='\n':
                    #  print(d)
                     s+= ' '
                s+='\n'

        if s != '':
            with open(new_file_path, 'w') as f:
                f.write(s)

            with open(new_file_path, 'r+') as fd:
                lines = fd.readlines()
                fd.seek(0)
                fd.writelines(line for line in lines if line.strip())
                fd.truncate()

            # with open(new_file_path,'rw') as file:
            #     for line in file:
            #         if not line.isspace():
            #             file.write(line)
            img_path = images_path + '/' + file.rsplit('/', 1)[-1].split('.txt')[0] + '.jpg'
            img = cv2.imread(img_path)
            img_saving_path = new_images_path + '/' + file.rsplit('/', 1)[-1].split('.txt')[0] + '.jpg'
            cv2.imwrite(img_saving_path, img)




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument('--damage_name', required=True)
    parser.add_argument('--folder', required=True)
    args = parser.parse_args()
    main(args)