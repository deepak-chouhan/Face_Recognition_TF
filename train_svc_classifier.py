from Training.top_svc_classifier import svc_classifier as sc
import argparse
import os 


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dir", type=str, required=True,
	help="path to input video file")
ap.add_argument("-o", "--outdir", type=str, required=False, default='Model',
	help="OpenCV object tracker type")
args = vars(ap.parse_args())

print(f"Data directory - {args['dir']}")
print(f"output directory - {args['outdir']}")

sc.train_classifier(data_dir=args['dir'],
                    export_dir=args['outdir'])
