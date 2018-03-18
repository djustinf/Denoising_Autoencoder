'''
Justin Foxhoven
3/17/18
'''

import cv2
import argparse
import utils

def main():
  parser = argparse.ArgumentParser(description='Process some integers.')
  parser.add_argument('-i', '--image', required=True)
  parser.add_argument('-f', '--fract', type=float, default=0.5, required=True)
  args = parser.parse_args()

  img = cv2.imread(args.image)
  img = cv2.resize(img, (500, 500))
  utils.noise_and_compare(img, args.fract)

if __name__ == ('__main__'):
  main()