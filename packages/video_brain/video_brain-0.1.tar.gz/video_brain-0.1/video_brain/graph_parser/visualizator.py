import numpy as np
import settings
import random
import lmdb
import sys
import matplotlib.pyplot as plt
sys.path.insert(0, settings.caffe_root + 'python')
import caffe

class Visualizator:

    def visualize(self, directory):

        train_images_env = lmdb.open(directory + 'train_rush_images', readonly=True)
        train_labels_env = lmdb.open(directory + 'train_rush_labels', readonly=True)
        val_images_env = lmdb.open(directory + 'val_rush_images', readonly=True)
        val_labels_env = lmdb.open(directory + 'val_rush_labels', readonly=True)

        images = []
        targets = []

        with train_images_env.begin() as txn_train_images:
            with train_labels_env.begin() as txn_train_labels:

                images_cursor = txn_train_images.cursor()
                targets_cursor = txn_train_labels.cursor()

                length = txn_train_images.stat()['entries']
                print(length)

                id_images = []
                for i in range(0,3):
                    id_images.append(random.randint(0, 501-1))

                for id_img in id_images:
                    str_id = '{:08}'.format(id_img)

                    value_images = images_cursor.get(str_id.encode('ascii'))
                    value_targets = targets_cursor.get(str_id.encode('ascii'))

                    datum = caffe.proto.caffe_pb2.Datum()

                    datum.ParseFromString(value_images)
                    flat_img = np.fromstring(datum.data, dtype=np.uint8)
                    img = flat_img.reshape(datum.channels, datum.height, datum.width)
                    img = img.transpose((1, 2, 0))
                    images.append(img)

                    datum.ParseFromString(value_targets)
                    target = caffe.io.datum_to_array(datum)

                    targets.append(target)

        with val_images_env.begin() as txn_val_images:
            with val_labels_env.begin() as txn_val_labels:

                images_cursor = txn_val_images.cursor()
                targets_cursor = txn_val_labels.cursor()

                length = txn_val_images.stat()['entries']
                print(length)

                id_images = []
                for i in range(0, 3):
                    id_images.append(random.randint(0, 501 - 1))

                for id_img in id_images:
                    str_id = '{:08}'.format(id_img)

                    value_images = images_cursor.get(str_id.encode('ascii'))
                    value_targets = targets_cursor.get(str_id.encode('ascii'))

                    datum = caffe.proto.caffe_pb2.Datum()

                    datum.ParseFromString(value_images)
                    flat_img = np.fromstring(datum.data, dtype=np.uint8)
                    img = flat_img.reshape(datum.channels, datum.height, datum.width)
                    img = img.transpose((1, 2, 0))
                    images.append(img)

                    datum.ParseFromString(value_targets)
                    target = caffe.io.datum_to_array(datum)

                    targets.append(target)

        print(len(images))

        labels = []
        with open(directory + 'train_stats.txt', 'r') as file:
            for line in file:
                if 'Number of images for' in line:
                    label = line.split(' ')[-3]
                    labels.append(label)

        plt.figure(figsize=(15,6))
        plt.suptitle(' - '.join(labels))
        cpt = 1
        for image, target in zip(images, targets):

            plt.subplot(2,3,cpt)
            plt.imshow(image)
            plt.title(target)
            cpt += 1

        plt.show()






