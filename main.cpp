#include <iostream>
#include <opencv2/opencv.hpp>
#include "compresser.h"

using namespace std;
using namespace cv;

Mat compressImage(const Mat &image, int k);

int main(int argc, char **argv) {

    Mat compressedImage;
    int k;

    if(argc < 4) {

        cout << "Error. Bad arguments" << endl;
        return 1;

    }
    try {

        k = atoi(argv[3]);
        Compresser compresser = Compresser(argv[1]);
        cout << compresser.getImage().size() << endl;
        compressedImage = compresser.compress(k);
        imwrite(argv[2], compressedImage);

    } catch(exception e) {

        cout << e.what() << endl;

    }

    return 0;

}
