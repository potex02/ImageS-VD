#include "Compresser.h"
#include<iostream>

Compresser::Compresser(std:: string path) {

    this->image = cv::imread(path);
    this->image.convertTo(this->image, CV_64F);
    if(this->image.empty()) {

        throw new std::exception();

    }

}
cv::Mat Compresser::getImage() {

    return this->image;

}
cv::Mat Compresser::compress(int k) {

    cv::Mat compressedImage;
    std::vector<cv::Mat> channels;

    cv::split(this->image, channels);
    for(cv::Mat i: channels) {

        double min, max;
        cv::Mat u, w, vt, sigma, checkValues;
        cv::SVD svd;

        svd.compute(i, w, u, vt);
        std::cout << "U:" << u.size() << std::endl;
        std::cout << "S:" << w.size() << std::endl;
        cv::minMaxLoc(w, &min , &max);
        std::cout << min << " " << max << std::endl;
        cv::compare(w, k, checkValues, cv::CMP_GT);
        w.copyTo(sigma, checkValues);
        sigma = cv::Mat::diag(sigma);
        std::cout << "Rows:\t" << sigma.rows << std::endl;
        std::cout << "k:\t" << k << std::endl;
        i = u * sigma * vt;

    }
    cv::merge(channels, compressedImage);
    std::cout << image.size() << " " << compressedImage.size() << std::endl;
    return compressedImage;

}
