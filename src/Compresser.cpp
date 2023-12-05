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
cv::Mat Compresser::compress(double k) {

    cv::Mat compressedImage;
    std::vector<cv::Mat> c;

    cv::split(this->image, c);
    for(int i = 0; i != c.size(); i++) {

        this->channels.emplace_back(c[i]);
        this->channels[i].decompose();
        c[i] = this->channels[i].compose(k);

    }
    cv::merge(c, compressedImage);
    std::cout << image.size() << " " << compressedImage.size() << std::endl;
    return compressedImage;

}
