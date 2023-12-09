#include <iostream>
#include <opencv2/opencv.hpp>
#include <nlohmann/json.hpp>
#include "compresser.h"

using namespace std;
using namespace cv;

int main(int argc, char **argv) {

    Mat compressedImage;
    double k;

    if(argc < 4) {

        cout << "Error. Bad arguments" << endl;
        return 1;

    }
    try {

        k = atof(argv[3]);
        Compresser compresser = Compresser(argv[1]);
        compressedImage = compresser.compose(k);
        compresser.save();
        imwrite(argv[2], compressedImage);

    } catch(exception e) {

        cout << e.what() << endl;

    }

    return 0;

}
