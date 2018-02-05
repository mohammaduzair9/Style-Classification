import baker
import json
from path import Path
from cytoolz import merge, join, groupby
from cytoolz.compatibility import iteritems
from cytoolz.curried import update_in
from itertools import starmap
from collections import deque
from lxml import etree, objectify
from scipy.io import savemat
from scipy.ndimage import imread


def keyjoin(leftkey, leftseq, rightkey, rightseq):
    
    return starmap(merge, join(leftkey, leftseq, rightkey, rightseq))


def root(folder, filename, height, width):
    E = objectify.ElementMaker(annotate=False)
    return E.annotation(
            E.folder(folder),
            E.filename(filename),
            E.source(
                E.database('MS COCO 2014'),
                E.annotation('MS COCO 2014'),
                E.image('Flickr'),
                ),
            E.size(
                E.width(width),
                E.height(height),
                E.depth(3),
                ),
            E.segmented(0)
            )


def instance_to_xml(anno):
    E = objectify.ElementMaker(annotate=False)
    xmin, ymin, width, height = anno['bbox']
    xmin = int(xmin)
    ymin = int(ymin)
    width = int(width)
    height = int(height)

    return E.object(
            E.name(anno['class']),
            E.bndbox(
                E.xmin(xmin),
                E.ymin(ymin),
                E.xmax(xmin+width),
                E.ymax(ymin+height),
                ),
            )


@baker.command
def write_categories(coco_annotation, dst):
    content = json.loads(path(coco_annotation).expand().text())
    categories = tuple( d['name'] for d in content['categories'])
    savemat(path(dst).expand(), {'categories': categories})


def get_instances(coco_annotation):
    coco_annotation = Path(coco_annotation).expand()
    content = json.loads(coco_annotation.text())  
 
    class1 = list(content['cats']['class']['1'].values())
    class2 = list(content['cats']['class']['2'].values())
    class3 = list(content['cats']['class']['3'].values())
    categories = {class1[1]:class1[0],class2[1]:class2[0],class3[1]:class3[0]}
    
    #categories = {1:'Text'}
    #categories = {d['id']: d['name'] for d in content['categories']}
    
    return categories, tuple(keyjoin('id', content['imgs'].values(), 'image_id', content['anns'].values()))
    #return categories, tuple(keyjoin('id', content['images'], 'image_id', content['annotations']))

def rename(name, year=2014):
        out_name = Path(name).stripext()
        # out_name = out_name.split('_')[-1]
        # out_name = '{}_{}'.format(year, out_name)
        return out_name


@baker.command
def create_imageset(annotations, dst):
    annotations = path(annotations).expand()
    dst = Path(dst).expand()
    val_txt = dst / 'val.txt'
    train_txt = dst / 'train.txt'

    for val in annotations.listdir('*val*'):
        val_txt.write_text('{}\n'.format(val.basename().stripext()), append=True)

    for train in annotations.listdir('*train*'):
        train_txt.write_text('{}\n'.format(train.basename().stripext()), append=True)

@baker.command
def create_annotations(dbpath, subset, dst):
    annotations_path = Path(dbpath).expand() / '{}_Text.json'.format(subset)
    images_path = 'path to JPEG Images containing Images'
    categories , instances= get_instances(annotations_path)
    
    dst = Path(dst).expand()

    #for i, instance in enumerate(instances):
        #if i==10:
        #    print(instance)
        #print(instances[i]['category'])
        #print([instance['class']])
        #instances[i]['category_id'] = instance['class']
        #instances[i]['category_id'] = categories[instance['category_id']]
        #if i==10:
        #    print(instance)
        #print(instance['class'])
        #instances[i][1] = 'Text'
        
    #exit()
    for name, group in iteritems(groupby('file_name', instances)):
        images_path = 'path to JPEG Images containing Images'
        images_path = images_path + '/' + name;
        print(images_path)
        img = imread(images_path)
        if img.ndim == 3:
            out_name = rename(name)
            annotation = root('VOC2012', '{}.jpg'.format(out_name), 
                              group[0]['height'], group[0]['width'])
            for instance in group:
                annotation.append(instance_to_xml(instance))
            etree.ElementTree(annotation).write(dst / '{}.xml'.format(out_name))
            print (out_name)
        else:
            print (instance['file_name'])





if __name__ == '__main__':
    baker.run()
