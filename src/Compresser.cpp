#include "Compresser.h"

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
void Compresser::decompose() {

    std::vector<cv::Mat> c;

    cv::split(this->image, c);
    for(cv::Mat i: c) {

        this->channels.emplace_back(i);

    }

};
cv::Mat Compresser::compose(double k) {

    std::vector<cv::Mat> c;
    cv::Mat compressedImage;

    for(Channel i: this->channels) {

        c.emplace_back(i.compose(k));

    }
    cv::merge(c, compressedImage);
    return compressedImage;

};
