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
    for(int i = 0; i != channels.size(); i++) {

        channels[i] = Channel(channels[i]).compress(k);

    }
    cv::merge(channels, compressedImage);
    std::cout << image.size() << " " << compressedImage.size() << std::endl;
    return compressedImage;

}
