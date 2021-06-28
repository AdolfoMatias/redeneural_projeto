import glob2
import os
import sys
from pathlib import Path

rootPathTrain = "./dataset/train"
rootPathVal = "./dataset/valid"
rootPathTest = "./dataset/test"
TRAIN_FILE = "./train.txt"
VAl_FILE = "./val.txt"
TEST_FILE = "./test.txt"

def createFileWithImages(roothPath, file):
    jpg_files = [f for f in glob2.glob(rootPathTrain + "/**/*.jpg", recursive=True)]

    with open (TRAIN_FILE, "w") as train_file:
        train_file.write("\n".join(str(item) for item in jpg_files))

def createFileWithImages(roothPath, file):
    jpg_files = [f for f in glob2.glob(rootPathVal+ "/**/*.jpg", recursive=True)]
    
    with open (VAl_FILE, "w") as val_file:
        val_file.write("\n".join(str(item) for item in jpg_files))

def createFileWithImages(roothPath, file):
    jpg_files = [f for f in glob2.glob(rootPathTest+ "/**/*.jpg", recursive=True)]
    
    with open (TEST_FILE, "w") as test_file:
        val_file.write("\n".join(str(item) for item in jpg_files))



    """
    Crie o scrip para gerar traino e validação -> faça isso utilizando métodos e condicional para identidade da classe
    """
if __name__ == '__main__':
    createFileWithImages(rootPathTrain, TRAIN_FILE)
    createFileWithImages(rootPathVal, VAl_FILE)
    createFileWithImages(rootPathVal, TEST_FILE)


    