#include <iostream>
#include <fstream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

Mat compressImage(const Mat &image, int k);

int main(int argc, char **argv) {

    Mat image, compressedImage;
    int k;

    if(argc < 4) {

        cout << "Error. Bad arguments" << endl;
        return 1;

    }
    k = atoi(argv[3]);
    image = imread(argv[1]);
    cvtColor(image, image, COLOR_BGR2GRAY);
    image.convertTo(image, CV_64F);
    if(image.empty()) {

        cout << "Error. Please select an image" << endl;
        return 1;

    }
    cout << image.size() << endl;
    compressedImage = compressImage(image, k);
    imwrite(argv[2], compressedImage);
    return 0;

}
Mat compressImage(const Mat &image, int k) {

    double min, max;
    Mat u, w, vt, sigma, compressedImage, checkValues;
    SVD svd;

    svd.compute(image, w, u, vt);
    cout << "U:" << u.size() << endl;
    cout << "S:" << w.size() << endl;
    minMaxLoc(w, &min , &max);
    cout << min << " " << max << endl;
    compare(w, k, checkValues, CMP_GT);
    w.copyTo(sigma, checkValues);
    sigma = Mat::diag(sigma);
    cout << "Rows:\t" << sigma.rows << endl;
    cout << "k:\t" << k << endl;
    compressedImage = u * sigma * vt;
    cout << image.size() << " " << compressedImage.size() << endl;
    return compressedImage;

}
