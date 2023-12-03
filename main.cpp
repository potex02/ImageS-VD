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
    k = atoi(argv[3]);
    Compresser compresser = Compresser(argv[1]);
    cout << compresser.image.size() << endl;
    compressedImage = compressImage(compresser.image, k);
    imwrite(argv[2], compressedImage);
    return 0;

}
Mat compressImage(const Mat &image, int k) {

    Mat compressedImage;
    vector<Mat> channels;

    split(image, channels);
    for(Mat i: channels) {

        double min, max;
        Mat u, w, vt, sigma, checkValues;
        SVD svd;
        svd.compute(i, w, u, vt);
        cout << "U:" << u.size() << endl;
        cout << "S:" << w.size() << endl;
        minMaxLoc(w, &min , &max);
        cout << min << " " << max << endl;
        compare(w, k, checkValues, CMP_GT);
        w.copyTo(sigma, checkValues);
        sigma = Mat::diag(sigma);
        cout << "Rows:\t" << sigma.rows << endl;
        cout << "k:\t" << k << endl;
        i = u * sigma * vt;

    }
    merge(channels, compressedImage);
    cout << image.size() << " " << compressedImage.size() << endl;
    return compressedImage;

}
